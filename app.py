import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

# إعداد الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تنسيق
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff;
        }
        .title {
            text-align: center;
            color: #0d47a1;
        }
        .upload-box {
            background-color: #ffffffcc;
            padding: 20px;
            border-radius: 10px;
            border: 2px dashed #90caf9;
        }
    </style>
