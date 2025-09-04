import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas

def show_report_ui(conn):
    window = tk.Toplevel()
    window.title("Generate Report")

    tk.Label(window, text="Click to generate patient report").pack(pady=10)

    def generate_report():
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name, age, gender, contact FROM patients")
            data = cursor.fetchall()
            cursor.close()

            c = canvas.Canvas("patient_report.pdf")
            c.setFont("Helvetica", 14)
            c.drawString(100, 800, "Patient Report")

            y = 760
            for row in data:
                line = f"Name: {row[0]}, Age: {row[1]}, Gender: {row[2]}, Contact: {row[3]}"
                c.drawString(100, y, line)
                y -= 20

            c.save()
            messagebox.showinfo("Success", "Report generated: patient_report.pdf")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {e}")

    tk.Button(window, text="Generate PDF", command=generate_report).pack(pady=5)
