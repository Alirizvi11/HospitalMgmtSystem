import tkinter as tk
from tkinter import messagebox
from billing import generate_bill, get_bill_by_patient
from services.pdf_generator import generate_bill_pdf  # Adjust path if needed

def show_billing_window(conn):
    win = tk.Toplevel()
    win.title("Generate Bill")

    # Labels
    tk.Label(win, text="Patient ID").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Amount").grid(row=1, column=0, padx=10, pady=5)

    # Entry fields
    entry_pid = tk.Entry(win)
    entry_amt = tk.Entry(win)
    entry_pid.grid(row=0, column=1, padx=10, pady=5)
    entry_amt.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        try:
            pid = int(entry_pid.get().strip())
            amt = float(entry_amt.get().strip())

            if pid <= 0 or amt <= 0:
                messagebox.showerror("Error", "Patient ID and Amount must be positive numbers")
                return

            generate_bill(conn, pid, amt)
            messagebox.showinfo("Success", "Bill generated successfully")

        except ValueError:
            messagebox.showerror("Error", "Invalid input format. Use numbers only.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def download_pdf():
        try:
            pid = int(entry_pid.get().strip())
            bills = get_bill_by_patient(conn, pid)
            if not bills:
                messagebox.showerror("Error", "No bill found for this patient")
                return

            bill = bills[0]  # Latest bill
            bill_data = {
                "Bill ID": bill[0],
                "Amount": bill[1],
                "Date": bill[2].strftime('%Y-%m-%d'),
                "Status": bill[3],
                "Patient Name": bill[4],
                "Gender": bill[5],
                "Address": bill[6]
            }

            generate_bill_pdf(bill_data)
            messagebox.showinfo("Success", "PDF receipt generated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {e}")

    # Buttons
    tk.Button(win, text="Generate", command=submit).grid(row=2, columnspan=2, pady=10)
    tk.Button(win, text="Download Bill PDF", command=download_pdf).grid(row=3, columnspan=2, pady=10)
