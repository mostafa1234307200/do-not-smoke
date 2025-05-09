import streamlit as st
import numpy as np
import cv2
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تنسيق CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff;
        }
        .title {
            text-align: center;
            color: #2e7d32;
        }
        .upload-section {
            background-color: #e8f5e9;
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

# رفع الصورة أو التقاطها
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("ارفع صورة (jpg أو png)", type=["jpg", "jpeg", "png"])
camera_input = st.camera_input("أو التقط صورة بالكاميرا")
st.markdown('</div>', unsafe_allow_html=True)

# دالة التأثير (علامات شيخوخة بسيطة + تغيير الشفاه)
def apply_smoking_effect(image_np):
    image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # تغييم بسيط حول العينين والفم
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    aged = cv2.addWeighted(image, 0.92, edges_colored, 0.15, 0)

    # تغميق الشفاه قليلاً
    hsv = cv2.cvtColor(aged, cv2.COLOR_BGR2HSV)
    lips_mask = cv2.inRange(hsv, (160, 50, 50), (180, 255, 255))
    aged[lips_mask > 0] = aged[lips_mask > 0] * 0.5

    result = cv2.cvtColor(aged, cv2.COLOR_BGR2RGB)
    return result

# المعالجة والعرض
input_image = None
if uploaded_file:
    input_image = Image.open(uploaded_file).convert("RGB")
elif camera_input:
    input_image = Image.open(camera_input).convert("RGB")

if input_image:
    st.image(input_image, caption="صورتك الأصلية", use_column_width=True)

    img_np = np.array(input_image)
    with st.spinner("تطبيق التأثير..."):
        result_img = apply_smoking_effect(img_np)
        st.image(result_img, caption="بعد 30 سنة من التدخين", use_column_width=True)
