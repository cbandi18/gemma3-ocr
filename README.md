# gemma3-ocr
This project leverages Gemma-3 vision capabilities and Streamlit to create a 100% locally running computer vision app that can perform both OCR and extract structured text from the image.

🚀 **OCR and Structured Text Extraction Using Gemma 3 Vision & Ollama**  

Google recently launched Gemma 3 , an open-source model that runs efficiently on a single CPU/TPU while delivering powerful performance. This project demonstrates text extraction from images, documents, and videos, leveraging OCR (Tesseract), OpenCV, and Gemma 3 Vision, all running locally with Ollama.  

## 🌟 Features  

✅ **Supports Multiple Inputs**:  
- 📜 **Text** input  
- 🖼️ **Images** (JPEG, PNG, JPG, WebP)  
- 📄 **Documents** (PDF, DOCX, TXT)  
- 🎥 **Videos** (MP4, AVI, MOV, MKV)  

✅ **Runs Entirely on CPU** - No need for GPUs! 💡  
✅ **Gemma 3 Vision Integration** - Structured text processing  
✅ **Tesseract OCR & OpenCV** - Image & Video text extraction  
✅ **Interactive UI with Streamlit** 🎨  

## 🛠️ Installation  

1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/cbandi18/gemma3-ocr.git
cd gemma3-ocr
```

2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3️⃣ **Install & Configure Ollama**  
- Download & Install **Ollama**: [https://ollama.ai](https://ollama.ai)  
- Pull the **Gemma 3 Vision Model**:  
```sh
ollama pull gemma3:latest
```

4️⃣ **Install & Set Up Tesseract OCR**  
- Download **Tesseract OCR** from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)  
- Set the path in your script (`pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"`)

## 🚀 Running the Project  

```sh
streamlit run app.py
```

## 📌 Demo Video  
🎬 **Watch the project demo:** https://shorturl.at/hTDay

## 🔥 Future Improvements  
🔹 Enhance video processing speed  
🔹 Optimize OCR pipeline for better accuracy  
🔹 Expand support for multilingual text extraction  

## 🤝 Contributing  
Feel free to **fork** this repository, create a branch, and submit a **pull request**! Contributions are welcome.  

## 📜 License  
This project is open-source and available under the **MIT License**.