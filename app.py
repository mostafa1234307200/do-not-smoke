import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تنسيق واجهة الموقع
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

# عنوان الموقع
st.markdown("<h1 class='title'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='title'>كيف سيبدو وجهك بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)

# صندوق الرفع أو الكاميرا
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("ارفع صورة (jpg أو png)", type=["jpg", "jpeg", "png"])
camera_input = st.camera_input("أو التقط صورة بالكاميرا")
st.markdown('</div>', unsafe_allow_html=True)

# دالة التأثير
def apply_enhanced_smoking_effect(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # تأثير باهت للبشرة
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.subtract(l, 20)
    lab = cv2.merge((l, a, b))
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # تأثير على الشفاه والعينين
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_lips = cv2.inRange(hsv, (0, 30, 40), (20, 255, 255))
    mask_eyes = cv2
