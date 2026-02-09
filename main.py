import streamlit as st
import requests
import io

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI: Ultra HQ", page_icon="🖼️", layout="wide")

# Custom UI Styling for Maddy
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #0f0c29, #302b63, #24243e); color: white; }
    .stButton>button { 
        border-radius: 20px; background: #FF4B4B; color: white; font-weight: bold; 
        width: 100%; border: none; height: 3.5em; transition: 0.3s;
    }
    .stButton>button:hover { background: #ff3333; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Ultra High-Quality Wallpapers")
st.write("Vanakka Maddy! Inbuilt high-res coding ippo activate aayiduchu. No more 3-byte files!")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎨 Your Creative Request")
    user_input = st.text_input("Enna creative image venum? (Eg: 8k Roman Reigns wallpaper, Cinematic Car...)", 
                                placeholder="Type your idea here...")
    
    # Inbuilt styles for HQ results
    quality_mode = st.selectbox("Select Quality Engine:", 
                                ["Ultra-Realistic 8K", "Cinematic Masterpiece", "Studio Lighting Professional", "Digital Art HQ"])

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("AI is building your high-quality wallpaper..."):
                # INBUILT PROMPT ENGINEERING: Background-la quality parameters add panroam
                final_prompt = f"{user_input}, {quality_mode}, extremely detailed, 8k resolution, photorealistic, masterpiece, vivid colors, sharp focus, 16k wallpaper quality"
                
                # Using a high-stability engine
                img_url = f"https://pollinations.ai/p/{final_prompt.replace(' ', '%20')}?width=1920&height=1080&seed=777&model=flux"
                
                try:
                    # FIXING THE 3-BYTE ISSUE: Fetching real binary data
                    response = requests.get(img_url, timeout=40)
                    if response.status_code == 200:
                        # Storing real data in session
                        st.session_state['real_img_data'] = response.content
                        st.session_state['display_url'] = img_url
                        st.session_state['generated'] = True
                    else:
                        st.error("Server busy-ah irukku Maddy. Refresh panni thirumba Magic Pannunga!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ High-Res Preview")
    if 'generated' in st.session_state:
        # Show image in UI
        st.image(st.session_state['display_url'], caption="Mad Gen Premium Result")
        
        # PROPER DOWNLOAD BUTTON: Converts binary data to a real file
        # Idhu dhaan 3 bytes-ai 3 MB-ah maathum!
        st.download_button(
            label="📥 DOWNLOAD HD WALLPAPER (Original Quality)",
            data=st.session_state['real_img_data'],
            file_name=f"mad_gen_wallpaper.png",
            mime="image/png"
        )

st.divider()
st.caption("Mad Gen AI | Inbuilt Wallpaper Engine v2.0 ✅")
