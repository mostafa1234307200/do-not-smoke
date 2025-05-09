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
