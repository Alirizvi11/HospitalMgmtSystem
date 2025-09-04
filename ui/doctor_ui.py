import tkinter as tk
from tkinter import messagebox
from doctor import add_doctor

def show_doctor_window(conn):
    win = tk.Toplevel()
    win.title("Add Doctor")

    labels = ["Name", "Specialization", "Phone", "Email"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        try:
            add_doctor(conn, entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get())
            messagebox.showinfo("Success", "Doctor added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Doctor", command=submit).grid(row=4, columnspan=2)