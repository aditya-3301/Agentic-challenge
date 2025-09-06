import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai

# Function to extract text from PDF------------------------------------------
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
    return all_text, len(reader.pages)

#------------------------------------------

#Streamlit App
st.title("PDF Text Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

length = st.slider("Summary length (words)", 10, 150, 50,5)

text = ""
if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text, page_count= extract_pdf_text(uploaded_file)

    st.success(f"PDF loaded with {page_count} pages")

#API key
api_key = st.secrets.get("api_key")
if not api_key:
    st.error("API key not found. Add it to Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key.strip())

# Model
model = genai.GenerativeModel("models/gemini-1.5-flash")

if text:
    with st.spinner("Generating summary..."):
        try:
            response = model.generate_content(
                f"Give a summary of length {length} in bullet points\n{text}"
            )
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating summary: {e}")

#Sidebar
st.sidebar.header("Ask Questions about the PDF")

question = st.sidebar.text_input("Type your question here:")

if question:
    with st.spinner("Thinking..."):
        try:
            chat_response = model.generate_content(
                f"Answer the questions based on this PDF:\n\n{question}\n\nPDF Content:\n{text}"
            )
            st.sidebar.write(chat_response.text)
        except Exception as e:
            st.sidebar.error(f"Error generating answer: {e}")
