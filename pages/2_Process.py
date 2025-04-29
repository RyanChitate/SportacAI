import streamlit as st
from utils.video_processing import process_video

st.title("🎬 Process & Enhance Video")

if 'uploaded_video_path' in st.session_state:
    video_path = st.session_state['uploaded_video_path']
    
    st.video(video_path)

    st.subheader("Choose Overlays")
    trails = st.checkbox("Player Movement Trails")
    passing_lanes = st.checkbox("Suggested Passing Lanes")
    zones = st.checkbox("Dynamic Zones")

    if st.button("Process Video"):
        processed_path = process_video(video_path, trails, passing_lanes, zones)
        st.session_state['processed_video_path'] = processed_path
        st.success("Video processed successfully!")
        st.video(processed_path)
else:
    st.warning("Please upload a video first.")
