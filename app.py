import streamlit as st
import ollama
import pytesseract
import numpy as np
import cv2
import pdfplumber

from PIL import Image
from docx import Document

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

def process_text_with_gemma3(text):         #function to process the extracted text with gemma3
    response= ollama.chat(
    model = 'gemma3:12b',
    messages = [{"role" : "user", "content" : text}] 
)
    return response['messages']

#Streamlit UI
st.title("OCR and Structured Text Extraction with Gemma-3 Vision")

user_text = st.text_area("Or enter your text manually: ")       #Giveing text input 

uploaded_image = st.file_uploader("Upload an image", type=["jpeg", "webp", "jpg", "png"]) #Uploading the image
uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"]) #Uploading the Video
uploaded_document = st.file_uploader("Upload your Document (DOCX, PDF, TXT)", type = ["docx", "pdf", "txt"])

def extract_data_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()     #Extracting text from each page
    return text

def extract_data_from_docs(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_data_from_text(text_file):
    text = text_file.read().decode("utf-8")
    return text

#To capture the video from webcam
input_video = st.checkbox("Use webcam video stream", value=False)
video_frame = None

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Upload Image", use_column_width=True)

    img_cv = np.array(image)        #Converting the image to openCV format
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RBG2BGR)

    #Extracted text using the tesseract
    extracted_text = extract_text(image)
    st.subheader("Extracted Text: ")
    st.text(extracted_text)

elif uploaded_video is not None:
    video_bytes = uploaded_video.read()
    video_path = "/tmp/uploaded_video.mp4"      #Saving the video temporarily

    with open(video_path, "wb") as f:
        f.write(video_bytes) 

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        st.error("Error Opening Video File.")
    else:
        frame_counter = 0
        while capture.isOpened():
            ret, frame = capture.read()
            frame_counter += 1

            if not ret or frame_counter > 30:       # Limiting to 30 frames for performance
                break
            
            # Converting the frame to PIL Image for Streamlit display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            
            # Display video stream in Streamlit
            st.image(pil_image, caption="Video Frame", use_column_width=True)

            # Extract text using OCR from the video frame
            extracted_text = extract_text(pil_image)
            st.subheader("Extracted Text From Frame")
            st.text(extracted_text)

            # Processing structured text with Gemma-3 Vision
            structured_text = process_text_with_gemma3(extracted_text)
            st.subheader("Extracted Data Output")
            st.text(structured_text)

            # Option to break the loop after showing a few frames or stop it manually
            if st.button("Stop Video"):
                capture.release()
                st.text("Video Stream Stopped")
                break

elif uploaded_document is not None:
    document_type = uploaded_document.type
    extracted_text = ""

    if document_type == "application/pdf":
        extracted_text = extract_data_from_pdf(uploaded_document)
    elif document_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        extracted_text = extract_data_from_docs(uploaded_document)
    elif document_type == "text/plain":
        extracted_text = extract_data_from_text(uploaded_document)

    st.subheader("Extracted Text From Document")
    st.text(extracted_text)

else:
    extracted_text = "Please give the input (Text or Document or Image or Video) to Process."

# Use extracted text or user input text for processing
final_text = user_text if user_text else extracted_text

if st.button("Extract Structured Data") and final_text:
    structured_text = process_text_with_gemma3(final_text)
    st.subheader("Structured Data Output")
    st.text(structured_text)