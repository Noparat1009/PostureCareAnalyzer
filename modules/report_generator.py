from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 16)
    c.drawString(50, height - 50, "PostureCare Analyzer Report")
    c.drawString(50, height - 100, "Summary: Your posture is good.")
    c.save()
