import streamlit as st
from utils.video_processing import process_video_segment

st.title("🎬 Process & Enhance Match Segment")

if 'uploaded_video_path' in st.session_state:
    video_path = st.session_state['uploaded_video_path']
    st.video(video_path)

    st.subheader("Choose Overlays")
    trails = st.checkbox("Player Movement Trails")
    passing_lanes = st.checkbox("Suggested Passing Lanes")
    zones = st.checkbox("Tactical Zones")

    segment_mode = st.toggle("Process Only a Segment of the Match")
    
    start_minute = 0
    end_minute = None

    if segment_mode:
        start_minute = st.number_input("Start Minute", min_value=0, max_value=120, value=25)
        end_minute = st.number_input("End Minute", min_value=start_minute + 1, max_value=130, value=45)

    if st.button("Process Video"):
        processed_path = process_video_segment(
            video_path, trails, passing_lanes, zones, 
            segment_mode=segment_mode, start_min=start_minute, end_min=end_minute
        )
        st.session_state['processed_video_path'] = processed_path
        st.success("Video processed successfully!")
        st.video(processed_path)

else:
    st.warning("Please upload a video first.")
