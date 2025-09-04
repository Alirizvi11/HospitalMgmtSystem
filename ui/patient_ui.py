import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from patient import add_patient  # Backend function

def show_patient_window(conn):
    window = tk.Toplevel()
    window.title("Add Patient")

    # Labels
    tk.Label(window, text="Name").grid(row=0, column=0)
    tk.Label(window, text="Gender").grid(row=1, column=0)
    tk.Label(window, text="DOB (YYYY-MM-DD)").grid(row=2, column=0)
    tk.Label(window, text="Phone").grid(row=3, column=0)
    tk.Label(window, text="Address").grid(row=4, column=0)

    # Entry fields
    entry_name = tk.Entry(window)
    entry_gender = tk.Entry(window)
    entry_dob = tk.Entry(window)
    entry_phone = tk.Entry(window)
    entry_address = tk.Entry(window)

    entry_name.grid(row=0, column=1)
    entry_gender.grid(row=1, column=1)
    entry_dob.grid(row=2, column=1)
    entry_phone.grid(row=3, column=1)
    entry_address.grid(row=4, column=1)

    def submit():
        try:
            # Input validation
            name = entry_name.get().strip()
            gender = entry_gender.get().strip()
            dob_str = entry_dob.get().strip()
            phone_str = entry_phone.get().strip()
            address = entry_address.get().strip()

            if not all([name, gender, dob_str, phone_str, address]):
                messagebox.showerror("Error", "All fields are required")
                return

            # Convert DOB and Phone
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            phone = int(phone_str)

            # Call backend
            add_patient(conn, name, gender, dob, address, phone)
            messagebox.showinfo("Success", "Patient added successfully")
            window.destroy()

        except ValueError:
            messagebox.showerror("Error", "Invalid date or phone format")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Add Patient", command=submit).grid(row=5, columnspan=2, pady=10)
