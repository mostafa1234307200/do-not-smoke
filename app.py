import streamlit as st
import numpy as np
import cv2
import io

# إعدادات الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تصميم CSS
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
    image[mask > 0] = image[mask > 0] * 0.7  # جعل الشفاه أغمق قليلاً

    result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
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
        result_img = apply_smoking_effect_simple(img_np)
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
