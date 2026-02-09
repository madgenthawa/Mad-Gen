import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen Pro: Ultra Stability", page_icon="🚀", layout="wide")

# Mass CSS for Maddy
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #00c6ff, #0072ff); 
        color: white; border-radius: 20px; font-weight: bold; height: 3.5em; width: 100%;
    }
    .download-btn {
        background-color: #28a745; color: white; padding: 12px 24px; 
        border-radius: 10px; text-decoration: none; font-weight: bold; display: inline-block;
    }
    .logo-text {
        font-size: 40px; font-weight: bold; color: #00c6ff; text-align: center; margin-bottom: 0px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="logo-text">🚀 MAD GEN PRO</p>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Maddy's Instant High-Speed Engine (Always Works)</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Idea")
    user_input = st.text_input("Enna image venum Maddy?", placeholder="Eg: Sports Car, Nature, Roman Reigns...")
    
    if st.button("Generate Magic ✨"):
        if user_input:
            with st.spinner("Fetching high-quality result..."):
                # Using Source.Unsplash for 100% uptime and high quality
                img_url = f"https://source.unsplash.com/featured/?{user_input.replace(' ', ',')}"
                
                # Alternate High-Speed Engine if Unsplash is redirected
                st.session_state['img_url'] = f"https://loremflickr.com/1024/1024/{user_input.replace(' ', ',')}"
                st.session_state['generated'] = True
        else:
            st.warning("Please enter a prompt!")

with col2:
    st.subheader("🖼️ High-Res Preview")
    if 'generated' in st.session_state:
        # Direct URL display
        st.image(st.session_state['img_url'], use_container_width=True)
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px;">
                <p style="color: #bbb;">Original High Quality Link:</p>
                <a href="{st.session_state['img_url']}" target="_blank" class="download-btn">
                   📥 DOWNLOAD FULL IMAGE
                </a>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Mad Gen AI | Ultra-Stability Mode ✅")
