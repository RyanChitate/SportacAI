import os
import streamlit as st

st.title("📤 Upload Match Footage")

uploaded_video = st.file_uploader("Upload your match video (.mp4 only)", type=["mp4"])

if uploaded_video:
    # Ensure the directory exists
    os.makedirs("outputs/videos", exist_ok=True)

    save_path = os.path.join('outputs/videos', uploaded_video.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    st.success(f"Uploaded successfully: {uploaded_video.name}")
    st.session_state['uploaded_video_path'] = save_path
