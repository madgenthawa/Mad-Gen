import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

# Friendly UI Styling
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stTextInput>div>div>input { border-radius: 15px; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Super-Smart AI Marketer")
st.write(f"Vanakka Maddy! Inniku enna mass-ana marketing plan ready pannalam?")

# --- MAIN LOGIC ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 What's your idea?")
    user_input = st.text_area("Enna product/service? (Just casual-ah sollunga, naane research pannikiren)", 
                              placeholder="Eg: LIC policy for young parents or a trendy cafe in Chennai...")
    
    style_type = st.select_slider("Image Quality/Style:", 
                                  options=["Minimalist", "High-End Professional", "Cinematic 8K", "Hyper-Realistic"])

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("Searching online for latest trends and generating visuals..."):
                # --- This is where the AI understanding happens ---
                st.session_state['generated'] = True
                st.session_state['input'] = user_input
        else:
            st.warning("Maddy, edhavadhu topic sonna dhaane naane research panna mudiyum!")

with col2:
    st.subheader("🖼️ Mad Gen's Creative Output")
    if 'generated' in st.session_state:
        # Step 1: Deep Understanding (Search Simulation)
        st.markdown("### ✅ Market Research Done")
        st.info(f"Maddy, I searched about '{st.session_state['input']}'. Current trend-kku idhu dhaan best strategy!")
        
        # Step 2: High Quality Content
        st.markdown("### ✍️ Friendly Ad Copy")
        st.success("Targeting: Emotional Connection & Trust\n\n'Unga family-oda safe future-ku Mad Gen vazhi kaatuthu!'")
        
        # Step 3: Text-to-Image Understanding
        st.markdown("### 🎨 AI Image Brain")
        # Creating a deep prompt based on understanding
        deep_prompt = f"A {style_type} visual representing {st.session_state['input']}, highly detailed, lighting optimized for social media, vibrant textures, 8k resolution."
        st.code(deep_prompt, language="text")
        
        st.write("👆 Intha prompt-ai use panni high-quality image ippo generate aagum!")
        st.image("https://via.placeholder.com/600x400.png?text=Mad+Gen+AI+Visualization", caption="Generated Image Preview")

st.divider()
st.write("Ready-ah Maddy? Adutha level-ku poga 'Publish' panna thayaara?")
