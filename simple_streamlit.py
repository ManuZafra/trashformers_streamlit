import streamlit as st
import cv2
import torch

st.title("Test de dependencias")
st.write(f"Versión de OpenCV: {cv2.__version__}")
st.write(f"CUDA disponible: {torch.cuda.is_available()}")
st.write(f"Versión de PyTorch: {torch.__version__}")
