# 📸 Family Photo Captioner

A simple web application that uses **Generative AI** to automatically generate captions for uploaded family photos. Built with **Streamlit** for the interface and **BLIP (Salesforce)** for image captioning via Hugging Face Transformers.

---

## Demo

Upload an image → The AI generates a descriptive caption instantly!  

---

## Key Features

- Upload `.jpg`, `.jpeg`, or `.png` images  
- AI generates human-readable captions using **BLIP**  
- Frontend built with **Streamlit** for interactive display  
- Optional PDF export for image + caption (using `reportlab`)  
- Can be extended to **Text-to-Speech (TTS)** for audio captions  

---

## **Project Structure**

family-photo-captioner/


├─ app.py # Streamlit frontend

├─ captioner.py # AI caption generation backend

├─ requirements.txt # Python dependencies

---

## Setup Instructions

1. Activate your virtual environment:
..\.venv\Scripts\activate.bat   # Windows

2. Navigate to the project folder:
cd D:\family-photo-captioner\family-photo-captioner

3. Run the Streamlit app:
streamlit run app.py

4. Open the browser (default http://localhost:8501)

5. Upload an image → AI generates caption

---

## Generative AI Usage

- Uses **BLIP model (`blip-image-captioning-base`)** from Hugging Face Transformers  
- **Workflow:**
  1. Image uploaded by user → processed into tensors  
  2. Model generates token IDs → decoded into text caption  
- Model runs **locally** (no external API calls at runtime)  
- Streamlit caches the model for faster reloads  

---

## Requirements

- Python 3.9+  
- `streamlit` >= 1.36.0  
- `Pillow` >= 10.0.0  
- `transformers` >= 4.41.0  
- `torch` >= 2.2.0  
- `sentencepiece` >= 0.1.99  
- `reportlab` >= 4.1.0  

---

## Notes / Limitations

Model may sometimes produce vague or slightly incorrect captions
Works faster on GPU; CPU inference is slower
Images are processed locally — no cloud upload by default

---

## License & Credits

BLIP model by Salesforce via Hugging Face
Hugging Face Transformers library: https://huggingface.co/transformers/
Streamlit for UI: https://streamlit.io