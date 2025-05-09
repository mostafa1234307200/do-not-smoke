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
            background-color: #e0f2f1;
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
    # تحويل الصورة إلى صورة بتدرجات الرمادي لتحاكي الشيخوخة والتأثيرات
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    
    # زيادة التباين والتشويش قليلاً
    enhanced_image = cv2.convertScaleAbs(gray_image, alpha=1.3, beta=30)
    
    # إعادة الصورة إلى الشكل الأصلي
    return enhanced_image

# المعالجة والعرض
input_image = None
if uploaded_file:
    input_image = Image.open(uploaded_file).convert("RGB")

if input_image:
    # عرض الصورة الأصلية
    st.image(input_image, caption="صورتك الأصلية", use_column_width=True)

    # تحويل الصورة إلى مصفوفة
    img_np = np.array(input_image)
    
    # تطبيق التأثير على الصورة
    result_img = apply_smoking_effect_simple(img_np)
    
    # عرض الصورة بعد التأثير
    st.image(result_img, caption="بعد 30 سنة من التدخين", use_column_width=True)

    # حفظ الصورة الناتجة كملف لاستخدامه لاحقًا
    result_pil = Image.fromarray(result_img)

    # تحويل الصورة إلى بايتات لتحميلها
    img_byte_arr = io.BytesIO()
    result_pil.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    # زر لتحميل الصورة
    st.download_button(
        label="تحميل الصورة الناتجة",
        data=img_byte_arr,
        file_name="smoking_effect_image.png",
        mime="image/png"
    )
