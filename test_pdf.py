from reportlab.pdfgen import canvas

c = canvas.Canvas("test_report.pdf")
c.drawString(100, 750, "Hospital Report Test")
c.save()

print("✅ PDF generated successfully!")
