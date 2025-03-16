import streamlit as st
import ollama
import pytesseract
import numpy as np
import cv2
from PIL import Image


# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image = Image.open(r"assets/gemma3_text.jpg")

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

print(extract_text(image))

def process_text_with_gemma3(text):         #function to process the extracted text with gemma3
    response= ollama.chat(
    model = 'gemma3:12b',
    messages = [{"role" : "user", "content" : text}] 
)
    return response['messages']
