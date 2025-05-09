import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

# إعدادات الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تصميم CSS مع إضافة صورة خلفية
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://your-image-url.com/background.jpg'); /* ضع رابط الصورة هنا */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        .title {
            text-align: center;
            color: #2e7d32;
        }
        .upload-section {
            background-color: rgba(255, 255, 255, 0.8); /* خلفية شفافة */
            padding: 20px;
            border-radius: 10px;
            border: 1px dashed #81c784;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h1 class='title'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow
