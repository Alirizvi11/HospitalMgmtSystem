import tkinter as tk
from tkinter import messagebox
from patient import add_patient

def show_patient_window(conn):
    window = tk.Toplevel()
    window.title("Add Patient")

    tk.Label(window, text="Name").grid(row=0, column=0)
    tk.Label(window, text="Gender").grid(row=1, column=0)
    tk.Label(window, text="DOB (YYYY-MM-DD)").grid(row=2, column=0)
    tk.Label(window, text="Address").grid(row=4, column=0)
    tk.Label(window, text="Phone").grid(row=3, column=0)

    entry_name = tk.Entry(window)
    entry_gender = tk.Entry(window)
    entry_dob = tk.Entry(window)
    entry_address = tk.Entry(window)
    entry_phone = tk.Entry(window)

    entry_name.grid(row=0, column=1)
    entry_gender.grid(row=1, column=1)
    entry_dob.grid(row=2, column=1)
    entry_address.grid(row=4, column=1)
    entry_phone.grid(row=3, column=1)

    def submit():
        try:
            add_patient(conn, entry_name.get(), entry_gender.get(), entry_dob.get(), entry_address.get(),entry_phone.get())
            messagebox.showinfo("Success", "Patient added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Add Patient", command=submit).grid(row=5, columnspan=2)