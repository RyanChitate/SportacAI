import streamlit as st

st.title("📥 Downloads Center")

if 'processed_video_path' in st.session_state:
    with open(st.session_state['processed_video_path'], "rb") as f:
        st.download_button(label="Download Processed Video", data=f, file_name="enhanced_video.mp4", mime="video/mp4")

if 'report_path' in st.session_state:
    with open(st.session_state['report_path'], "rb") as f:
        st.download_button(label="Download Player Report", data=f, file_name="player_report.pdf", mime="application/pdf")
