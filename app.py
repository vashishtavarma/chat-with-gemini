from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

load_dotenv()

try:
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
except KeyError:
    st.error("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")

model = genai.GenerativeModel(model_name='gemini-2.5-flash')

st.title("Q&A with Gemini-2.5")

user_input = st.text_input("Ask a question:")
submit_button = st.button(label='Submit')


if submit_button and user_input:
    try:
        response = model.generate_content(user_input)
        st.subheader("Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error occurred: {e}")
elif submit_button:
    st.error("Please enter a question before submitting.")


