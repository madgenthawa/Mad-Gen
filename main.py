import streamlit as st
import time
import random

# ==========================================
# 1. APP CONFIGURATION & PRO THEME
# ==========================================
st.set_page_config(
    page_title="Mad Gen AI: Universal Pro",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    /* Logo & Header */
    .main-title {
        font-size: 3.8rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
        background: -webkit-linear-gradient(#FFD700, #FF8C00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
    }
    /* Sub-header */
    .subheader-text {
        font-size: 1.2rem;
        text-align: center;
        color: #aaa;
        margin-top: 5px;
        margin-bottom: 30px;
    }
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.8rem;
        background: linear-gradient(to right, #FF8C00, #FFD700);
        border: none;
        color: black; /* Changed to black for contrast */
        font-weight: bold;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(255, 140, 0, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 140, 0, 0.6);
    }
    /* Custom Download Link */
    .download-btn {
        display: inline-block;
        padding: 18px 35px;
        background: #28a745;
        color: white !important;
        border-radius: 40px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 25px;
        font-size: 1.1rem;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.4);
    }
    .download-btn:hover {
        background: #218838;
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(40, 167, 69, 0.6);
    }
    /* Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.07);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 30px;
    }
    /* Text Areas */
    .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 10px;
        padding: 15px;
    }
    /* Selectboxes */
    .stSelectbox>div>div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    .stSelectbox>div>div>div>span {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INBUILT BUSINESS LOGIC (Tamil Slogans)
# ==========================================
def get_tamil_slogan(query):
    query_lower = query.lower()
    lic_slogans = [
        "உங்கள் ஒவ்வொரு அசைவிலும் பாதுகாப்பு – LIC.",
        "LIC: வாழ்நாள் முழுவதும் உறுதுணை.",
        "சரியான முதலீடு, சிறந்த எதிர்காலம் – LIC Housing Finance.",
        "கனவுகள் நிஜமாக, LIC வீட்டு வசதி கடன்."
    ]
    thawa_slogans = [
        "தவா நிதி சேவை: உங்கள் நிதித் தேவைகளுக்கான ஒரே தீர்வு. 📈",
        "சொத்து அடமானக் கடன்: உங்கள் கனவுகளுக்கு நிதி ஆதாரம் – THAWA Financial.",
        "வேகமான சேவை, முழுமையான நம்பிக்கை.",
        "THAWA: உங்கள் நிதி வளர்ச்சிக்கு துணை."
    ]
    
    if "lic" in query_lower or "life insurance" in query_lower or "housing finance" in query_lower:
        return random.choice(lic_slogans)
    elif "thawa" in query_lower or "financial" in query_lower or "loan against property" in query_lower or "lap" in query_lower:
        return random.choice(thawa_slogans)
    else:
        return "உங்களுடைய தனித்துவமான படைப்பு இதோ! ✨"

# ==========================================
# 3. HEADER & LOGO (Mad Gen Branding)
# ==========================================
st.markdown('<h1 class="main-title">✨ MAD GEN PRO ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader-text">Maddy, naan enna kettaalum adha Generate panni tharuven!</p>', unsafe_allow_html=True)

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("📝 Your Creative Command")
    user_input = st.text_area(
        "Describe anything you want to see (e.g., Epic Dragon with lightning, A car wallpaper, LIC housing finance ad, Thawa financial loan poster):",
        placeholder="Type your idea for a high-quality image...",
        height=180
    )
    
    # Image style selector for diverse results
    style_option = st.selectbox(
        "Select your preferred style:",
        ["Photorealistic", "Cinematic", "Digital Art", "Abstract", "Cartoon", "Vibrant Marketing"]
    )
    
    # Quality enhancer
    quality_enhancer = st.slider("Image Quality Boost:", 0, 100, 75)
    
    if st.button("Unleash the Mad Gen Magic! 🚀"):
        if user_input:
            with st.spinner("Mad Gen is summoning your ultimate creation..."):
                seed = int(time.time()) # Unique seed for diverse images
                
                # Dynamic prompt building for universal generation
                final_prompt = f"{user_input}, {style_option} style, {quality_enhancer}% quality, 8k, ultra-detailed, professional grading, high resolution, stunning"
                
                # Using a stable image engine that handles diverse prompts
                # This direct URL method bypasses rate limits and timeout issues
                # Note: For highly specific brand logos (like Thawa), you'd typically upload them.
                img_url = f"https://image.pollinations.ai/prompt/{final_prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.session_state['current_img_url'] = img_url
                st.session_state['generated'] = True
                st.session_state['current_slogan'] = get_tamil_slogan(user_input)
        else:
            st.warning("Please enter a command to generate your image, Maddy!")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("✨ Your Masterpiece & Slogan")
    if 'generated' in st.session_state:
        # Display the generated image directly via URL for stability
        st.image(st.session_state['current_img_url'], use_container_width=True, caption=f"Generated: {user_input}")
        
        # Display the relevant Tamil slogan
        st.success(f"**அதிர்ஷ்டவசமான தமிழ் ஸ்லோகன்:** {st.session_state['current_slogan']}")
        
        # Universal Download Button
        st.markdown(f"""
            <div style="text-align: center;">
                <p style="color: #ccc; font-size: 0.95rem; margin-bottom: 10px;">Click below to download in Original HD Quality:</p>
                <a href="{st.session_state['current_img_url']}" target="_blank" class="download-btn">
                   📥 DOWNLOAD YOUR MASTERPIECE
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Your amazing image and a catchy Tamil slogan will appear here!")

# ==========================================
# 5. FOOTER
# ==========================================
st.divider()
st.markdown("<p style='text-align:center; opacity:0.7;'>Mad Gen AI | Powered by Maddy's Vision 🚀 | Universal Stability Activated ✅</p>", unsafe_allow_html=True)
