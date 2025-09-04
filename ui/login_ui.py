import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from ui.dashboard_ui import show_dashboard
import tkinter.messagebox as messagebox
# show_dashboard(conn)



# def show_login_window(root, conn):
#     root.geometry("800x600")
#     root.title("Apollo Hospital Login")

#     # 🖼️ Background Image
#     bg = Image.open("assets/login_bg.jpg").resize((800, 600))
#     bg_img = ImageTk.PhotoImage(bg)
#     bg_label = tk.Label(root, image=bg_img)
#     bg_label.image = bg_img
#     bg_label.place(x=0, y=0)

#     # 📦 Login Box Frame
#     login_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
#     login_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)

#     tk.Label(login_frame, text="Login", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

#     # 🧑‍💻 Username Icon + Entry
#     user_img = Image.open("assets/user_icon.png").resize((20, 20))
#     user_icon = ImageTk.PhotoImage(user_img)
#     tk.Label(login_frame, image=user_icon, bg="#ffffff").pack()
#     username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
#     username_entry.pack(pady=5)

#     # 🔒 Password Icon + Entry
#     lock_img = Image.open("assets/lock_icon.png").resize((20, 20))
#     lock_icon = ImageTk.PhotoImage(lock_img)
#     tk.Label(login_frame, image=lock_icon, bg="#ffffff").pack()
#     password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
#     password_entry.pack(pady=5)

#     # ✅ Login Button with Hover
#     login_btn = tk.Button(login_frame, text="Login", bg="#4CAF50", fg="white", font=("Helvetica", 12))
#     login_btn.pack(pady=10)

#     def on_enter(e): login_btn.config(bg="#45a049")
#     def on_leave(e): login_btn.config(bg="#4CAF50")
#     login_btn.bind("<Enter>", on_enter)
#     login_btn.bind("<Leave>", on_leave)

# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     try:
#         cursor = conn.cursor()
#         cursor.execute("SELECT password FROM users WHERE username = :1", [username])
#         result = cursor.fetchone()
#         cursor.close()

#         if result and result[0] == password:
#             messagebox.showinfo("Login Success", f"Welcome {username}!")
#             root.withdraw()  # ✅ Hide login window
#             from ui.dashboard_ui import show_dashboard
#             show_dashboard(conn)  # ✅ Open dashboard
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))
#     login_btn.config(command=login)  # ✅ Bind login function to button

#     #login_btn.config(command=login)

# # def show_login_window(root, conn):
# #     root.geometry("600x400")
# #     bg = Image.open("assets/login_bg.jpg").resize((600, 400))
# #     bg_img = ImageTk.PhotoImage(bg)
# #     bg_label = tk.Label(root, image=bg_img)
# #     bg_label.image = bg_img
# #     bg_label.place(x=0, y=0)

# #     tk.Label(root, text="Login", font=("Helvetica", 20, "bold"), bg="#ffffff").place(x=250, y=50)
def show_login_window(root, conn):
    root.geometry("800x600")
    root.title("Apollo Hospital Login")

    # Background
    bg = Image.open("assets/login_bg.jpg").resize((800, 600))
    bg_img = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(x=0, y=0)

    # Login Frame
    login_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    login_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)

    tk.Label(login_frame, text="Login", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)

    # Username
    user_img = Image.open("assets/user_icon.png").resize((20, 20))
    user_icon = ImageTk.PhotoImage(user_img)
    tk.Label(login_frame, image=user_icon, bg="#ffffff").pack()
    username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
    username_entry.pack(pady=5)

    # Password
    lock_img = Image.open("assets/lock_icon.png").resize((20, 20))
    lock_icon = ImageTk.PhotoImage(lock_img)
    tk.Label(login_frame, image=lock_icon, bg="#ffffff").pack()
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=5)

    # Login Button
    login_btn = tk.Button(login_frame, text="Login", bg="#4CAF50", fg="white", font=("Helvetica", 12))
    login_btn.pack(pady=10)

    def on_enter(e): login_btn.config(bg="#45a049")
    def on_leave(e): login_btn.config(bg="#4CAF50")
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)

    # ✅ Define login function inside so it can access entries and conn
    def login():
        username = username_entry.get()
        password = password_entry.get()

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = :1", [username])
            result = cursor.fetchone()
            cursor.close()

            if result and result[0] == password:
                messagebox.showinfo("Login Success", f"Welcome {username}!")
                root.withdraw()
                from ui.dashboard_ui import show_dashboard
                show_dashboard(conn)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    login_btn.config(command=login)
