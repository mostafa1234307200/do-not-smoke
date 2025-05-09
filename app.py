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
            background-color: rgba(255
