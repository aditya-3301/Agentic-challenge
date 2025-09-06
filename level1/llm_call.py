import streamlit as st
import google.generativeai as genai

# Get the API key from Streamlit secrets
api_key = st.secrets.get("api_key")

if not api_key:
    st.error("API key not found. Please add it to your Streamlit secrets.")
    st.stop()

# Configure the Gemini API
genai.configure(api_key=api_key.strip())

# Set up the model (Gemini 1.5 Flash)
chat_model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit app
st.title("Gemini Chatbot")

user_question = st.text_input("What would you like to ask?")

if user_question:
    with st.spinner("Thinking..."):
        try:
            reply = chat_model.generate_content(user_question)
            st.markdown(f"**Gemini says:** {reply.text}")
        except Exception as error:
            st.error(f"Oops! Something went wrong: {error}")
