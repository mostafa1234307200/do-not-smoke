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
st.markdown("<h1 class='title'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='title'>كيف سيبدو وجهك بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)

# رفع الصورة
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("ارفع صورة (jpg أو png)", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# دالة التأثير البسيط
def apply_smoking_effect_simple(image_np):
    image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # إضافة تأثير خفيف بتغيير التباين (زيادة اللمعان أو التدرج البسيط)
    image = cv2.convertScaleAbs(image, alpha=1.2, beta=20)

    # تعديل بسيط على لون الشفاه
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([160, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    image[mask > 0] = image[mask > 0] * 0.7  # جعل الشفاه أغمق قلي
