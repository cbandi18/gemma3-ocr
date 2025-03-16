import io
import base64
import streamlit as st
import ollama
from PIL import Image

import pytesseract

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

image = Image.open("assets\gemma3_text.jpg")
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)

response = ollama.chat(
    model = 'gemma3:12b',
    messages = [{"role" : "user", "content" : extracted_text}]
    
)
print(extracted_text)