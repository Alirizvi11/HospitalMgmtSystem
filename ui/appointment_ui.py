import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as messagebox
from appointment import book_appointment


def show_appointment_window(conn):
    win = tk.Toplevel()
    win.title("Book Appointment")

    labels = ["Patient ID", "Doctor ID", "Date (YYYY-MM-DD)", "Appointment_time (e.g. 10:00 AM)"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        try:
            book_appointment(conn, int(entries[0].get()), int(entries[1].get()), entries[2].get(), entries[3].get())
            messagebox.showinfo("Success", "Appointment booked")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Book", command=submit).grid(row=4, columnspan=2)