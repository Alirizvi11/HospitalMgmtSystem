# import tkinter as tk
# from tkinter import messagebox
# import cx_Oracle

# # Function to insert data into the database
# def register_user():
#     username = entry_username.get()
#     password = entry_password.get()
#     email = entry_email.get()

#     if username == "" or password == "" or email == "":
#         messagebox.showwarning("Input Error", "All fields must be filled!")
#         return

#     try:
#         # Replace with your actual DB connection details
#         conn = cx_Oracle.connect('hospital/u1@192.168.56.50/PDBPRIM1')
#         cursor = conn.cursor()

#         # Insert the user data into the "users" table
#         cursor.execute("INSERT INTO users (username, password, email) VALUES (:1, :2, :3)",
#                        (username, password, email))
#         conn.commit()

#         messagebox.showinfo("Success", "User registered successfully!")
#         conn.close()
#     except cx_Oracle.DatabaseError as e:
#         messagebox.showerror("Database Error", f"Error: {e}")

# # Set up the window
# window = tk.Tk()
# window.title("User Registration")

# # Create labels and entries
# label_username = tk.Label(window, text="Username:")
# label_username.pack()
# entry_username = tk.Entry(window)
# entry_username.pack()

# label_password = tk.Label(window, text="Password:")
# label_password.pack()
# entry_password = tk.Entry(window, show="*")
# entry_password.pack()

# label_email = tk.Label(window, text="Email:")
# label_email.pack()
# entry_email = tk.Entry(window)
# entry_email.pack()

# # Register button
# register_button = tk.Button(window, text="Register", command=register_user)
# register_button.pack()

# # Run the application
# window.mainloop()