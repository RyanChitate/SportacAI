import streamlit as st
from utils.report_generator import generate_report

st.title("📊 Generate Performance Reports")

if st.button("Generate Player Report"):
    report_path = generate_report()
    st.session_state['report_path'] = report_path
    st.success("Report generated successfully!")
    with open(report_path, "rb") as f:
        st.download_button(label="Download Report", data=f, file_name="player_report.pdf", mime="application/pdf")
