import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def show_medications(conn):
    window = tk.Toplevel()
    window.title("Medications")

    # Form fields
    tk.Label(window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Brand").grid(row=1, column=0)
    brand_entry = tk.Entry(window)
    brand_entry.grid(row=1, column=1)

    tk.Label(window, text="Description").grid(row=2, column=0)
    desc_entry = tk.Entry(window)
    desc_entry.grid(row=2, column=1)

    tk.Label(window, text="Expiry Date (YYYY-MM-DD)").grid(row=3, column=0)
    expiry_entry = tk.Entry(window)
    expiry_entry.grid(row=3, column=1)

    def add_medication():
        name = name_entry.get()
        brand = brand_entry.get()
        desc = desc_entry.get()
        expiry = expiry_entry.get()

        try:
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO medications (name, brand, description, expiry_date)
                VALUES (:1, :2, :3, :4)
            """, (name, brand, desc, expiry_date))
            conn.commit()
            cursor.close()
            messagebox.showinfo("Success", "Medication added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add medication: {e}")

    tk.Button(window, text="Add Medication", command=add_medication).grid(row=4, columnspan=2, pady=10)
