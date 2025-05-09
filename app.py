import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #f9fbe7;
        }
        .title {
            text-align: center;
            color: #33691e;
        }
        .upload-box {
            border: 2px dashed #8bc34a;
            padding: 20px;
            border-radius: 10px;
            background-color: #f1f8e9;
            margin-top: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='title'>كيف سيبدو وجهك بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)

st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("ارفع صورة (jpg أو png)", type=["jpg", "jpeg", "png"])
camera_input = st.camera_input("أو التقط صورة بالكاميرا")
st.markdown("</div>", unsafe_allow_html=True)

def apply_enhanced_smoking_effect(img):
    img = cv2.cvtColor(img,
