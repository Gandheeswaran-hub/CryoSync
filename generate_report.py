from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

file_name = "Mineral_Oil_Cooling_Project_Report.pdf"

doc = SimpleDocTemplate(file_name, pagesize=A4)
styles = getSampleStyleSheet()
content = []

content.append(Paragraph(
    "<b>MINERAL OIL COOLING SIMULATION SYSTEM</b>",
    styles["Title"]
))
content.append(Spacer(1, 20))

content.append(Paragraph("<b>Project Lead:</b> Dhinagaran B", styles["Normal"]))
content.append(Paragraph("<b>Email:</b> dhinagaranboopathi", styles["Normal"]))
content.append(Paragraph("<b>GitHub:</b> dhina-528", styles["Normal"]))
content.append(Spacer(1, 20))

content.append(Paragraph("<b>Abstract</b>", styles["Heading2"]))
content.append(Paragraph(
    "This project presents a software-based simulation of PC cooling techniques "
    "including Air Cooling, Liquid Cooling, and Mineral Oil Cooling. "
    "The system visually demonstrates temperature reduction using graphs "
    "and gradient-based visualization.",
    styles["Normal"]
))
content.append(Spacer(1, 15))

content.append(Paragraph("<b>Objectives</b>", styles["Heading2"]))
content.append(Paragraph(
    "• Compare different PC cooling methods<br/>"
    "• Visualize temperature variation over time<br/>"
    "• Demonstrate efficiency of mineral oil cooling",
    styles["Normal"]
))
content.append(Spacer(1, 15))

content.append(Paragraph("<b>Technologies Used</b>", styles["Heading2"]))
content.append(Paragraph(
    "Python, Streamlit, NumPy, Matplotlib",
    styles["Normal"]
))
content.append(Spacer(1, 15))

content.append(Paragraph("<b>Results & Analysis</b>", styles["Heading2"]))
content.append(Paragraph(
    "The simulation results show that mineral oil cooling offers "
    "higher thermal stability and faster temperature reduction "
    "compared to air and liquid cooling techniques.",
    styles["Normal"]
))
content.append(Spacer(1, 15))

table_data = [
    ["Cooling Method", "Efficiency", "Cost", "Maintenance"],
    ["Air Cooling", "Low", "Low", "Easy"],
    ["Liquid Cooling", "Medium", "Medium", "Moderate"],
    ["Mineral Oil Cooling", "High", "High", "Low"]
]

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("ALIGN", (0,0), (-1,-1), "CENTER")
]))

content.append(table)
content.append(Spacer(1, 20))

content.append(Paragraph("<b>Conclusion</b>", styles["Heading2"]))
content.append(Paragraph(
    "Mineral oil cooling proves to be an effective and innovative solution "
    "for advanced PC thermal management, making it suitable for high-performance systems.",
    styles["Normal"]
))

doc.build(content)

print("PDF Generated Successfully!")
