import streamlit as st
import time
import random

# ==========================================
# 1. APP CONFIGURATION & PRO THEME
# ==========================================
st.set_page_config(
    page_title="Mad Gen AI: Global Creative Engine",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS Injection (UI/UX Mass-up)
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    /* Logo & Header */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(#FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5rem;
        background: linear-gradient(to right, #FF416C, #FF4B2B);
        border: none;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(255, 65, 108, 0.6);
    }
    /* Custom Download Link */
    .download-btn {
        display: inline-block;
        padding: 15px 30px;
        background: #28a745;
        color: white !important;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        transition: 0.3s;
    }
    .download-btn:hover { background: #218838; }
    /* Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255,
