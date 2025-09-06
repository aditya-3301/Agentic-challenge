import streamlit as st
import google.generativeai as genai

# Configure API key
api_key = st.secrets.get("api_key")
if not api_key:
    st.error("API key not found, Add it to Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key.strip())

# Initialize the model, choose version
model = genai.GenerativeModel("models/gemini-1.5-flash")

    
st.title("Gemini-Chatbot")

input = st.text_input("Ask me anything:")

if input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(input)
            st.write(response.text)
        except Exception as e: # Exception Handling
            st.error(f"Error generating response: {e}")