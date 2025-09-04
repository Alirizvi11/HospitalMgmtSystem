from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_bill_pdf(bill_data, filename="bill_receipt.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)

    c.drawString(50, 800, "🏥 Apollo Hospital - Bill Receipt")
    c.line(50, 795, 550, 795)

    y = 760
    for label, value in bill_data.items():
        c.drawString(50, y, f"{label}: {value}")
        y -= 25

    c.save()
