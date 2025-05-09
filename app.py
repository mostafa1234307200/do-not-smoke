import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تنسيق واجهة الموقع
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='title'>كيف سيبدو وجهك بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)

st.markdown("<div
