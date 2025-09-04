import tkinter as tk
from tkinter import messagebox
from billing import generate_bill

def show_billing_window(conn):
    win = tk.Toplevel()
    win.title("Generate Bill")

    tk.Label(win, text="Patient ID").grid(row=0, column=0)
    tk.Label(win, text="Amount").grid(row=1, column=0)

    entry_pid = tk.Entry(win)
    entry_amt = tk.Entry(win)
    entry_pid.grid(row=0, column=1)
    entry_amt.grid(row=1, column=1)

    def submit():
        try:
            generate_bill(conn, int(entry_pid.get()), float(entry_amt.get()))
            messagebox.showinfo("Success", "Bill generated")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Generate", command=submit).grid(row=2, columnspan=2)