import streamlit as st
import pytesseract
from PIL import Image

st.title("InvoiceIQ – Invoice Processing")

uploaded = st.file_uploader("Upload Invoice", type=["png","jpg"])

if uploaded:
    img = Image.open(uploaded)
    text = pytesseract.image_to_string(img)

    st.image(img)
    st.subheader("Extracted Text")
    st.write(text)
