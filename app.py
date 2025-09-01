import streamlit as st
from captioner import generate_caption

st.title("📸 Family Photo Captioner")
st.write("Upload a photo and get AI-generated captions!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)

    # Generate AI caption
    caption = generate_caption(uploaded_file)

    st.success("✅ Image uploaded successfully!")
    st.write("**AI Caption:** " + caption)



#  cd D:\family-photo-captioner\family-photo-captioner
#  ..\.venv\Scripts\activate.bat
#  streamlit run app.py