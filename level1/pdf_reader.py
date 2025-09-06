import logging

# Suppress all pypdf warnings since some compressed/optimised pdf files get pointing warnings
logging.getLogger("pypdf").setLevel(logging.ERROR)


import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai

# Function to extract text from PDF
#--------------------------------------------------------------------------------------------------------
def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    texts = []
    for page in reader.pages:
        try:
            t = page.extract_text() or ""
        except Exception:
            t = ""
        texts.append(t)
    all_text = "\n\n\n".join(texts)
    return all_text, len(reader.pages), len(all_text)

# Streamlit App
st.title("PDF Text Summarizer")

#Assigns uploaded file to what the file uploader recieved.
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

#Summary length
length = st.slider("Summary length (words)", 10, 150, 50)

text=""
if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text, page_count, char_count = extract_pdf_text(uploaded_file)

    st.success(f"PDF loaded: {page_count} pages, {char_count} characters")
#--------------------------------------------------------------------------------------------------------


# Configure API key
api_key = st.secrets.get("api_key")
if not api_key:
    st.error("API key not found, Add it to Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key.strip())

# Initialize the model, choose version
model = genai.GenerativeModel("models/gemini-1.5-flash")

if text:
    if "summary_text" not in st.session_state or st.session_state.get("last_file_name") != uploaded_file.name or st.session_state.get("last_length") != length:
        with st.spinner("Generating summary..."):
            try:
                response = model.generate_content(f"Give a summary of length {length} in bullet points\n{text}")
                st.session_state.summary_text = response.text
                st.session_state.last_file_name = uploaded_file.name
                st.session_state.last_length = length
            except Exception as e:
                st.error(f"Error generating response: {e}")
    st.write(st.session_state.summary_text)


# ---- Sidebar Chatbot ----
st.sidebar.header("Ask Questions about the PDF")

user_query = st.sidebar.text_input("Type your question here:")

if user_query:
    with st.spinner("Thinking..."):
        try:
            chat_response = model.generate_content(
                f"Answer the question based only on this PDF and if anything else given, generate a small answer telling only to ask about the pdf:\n\n{user_query}\n\nPDF Content:\n{text}"
                # Bypasses to the above prompt do exist but for the time being lets assume that this ai only about the PDF.
            )
            st.sidebar.write(chat_response.text)
        except Exception as e:
            st.sidebar.error(f"Error generating answer: {e}")
