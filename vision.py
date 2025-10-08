from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()

try:
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
except KeyError:
    st.error("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")

model = genai.GenerativeModel(model_name='gemini-2.5-pro')

st.title("Image Captioning with Gemini-2.5-Pro")

input_text = st.text_input("Enter a description for the image:")
uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])
submit_button = st.button(label='Submit')

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

if submit_button:
    response = None
    if input_text and image:
        response = model.generate_content(
            [input_text, image]
        )
    elif input_text:
        response = model.generate_content([input_text])
    elif image:
        response = model.generate_content(
            [image]
        )
    else:
        st.write("Please provide either text input, an image, or both.")

    if response:
        st.subheader("Response:")
        st.write(response.text)
    else:
        st.write("Please provide either text input, an image, or both.")