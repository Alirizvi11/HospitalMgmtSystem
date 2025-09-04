import tkinter as tk
from PIL import Image, ImageTk
import time

def show_welcome():
    root = tk.Tk()
    root.title("Welcome")
    root.geometry("600x400")
    root.configure(bg="#ffffff")

    # Background image
    bg = Image.open("assets/welcome_bg.jpg")
    bg = bg.resize((600, 400))
    bg_img = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(x=0, y=0)

    # Welcome text
    tk.Label(root, text="Welcome to Apollo Hospital System", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#2c3e50").pack(pady=30)

    # Fade-in effect
    for i in range(0, 100, 5):
        root.attributes("-alpha", i/100)
        root.update()
        time.sleep(0.02)

    # Auto-close after 3 seconds
    root.after(3000, root.destroy)
    root.mainloop()
