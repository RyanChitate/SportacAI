from fpdf import FPDF
import os
import datetime

def generate_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="SportacAI - Player Performance Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Total Distance: 10.2 km", ln=True)
    pdf.cell(200, 10, txt="Max Speed: 32.5 km/h", ln=True)
    pdf.cell(200, 10, txt="Tactical Involvement: High", ln=True)
    pdf.cell(200, 10, txt="Opportunities Missed: 3", ln=True)
    pdf.cell(200, 10, txt="Improvement Tips: Faster reaction during transitions.", ln=True)

    report_path = os.path.join("outputs/reports", "player_report.pdf")
    pdf.output(report_path)
    return report_path
