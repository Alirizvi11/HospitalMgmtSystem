import tkinter as tk
from ui.login_ui import show_login_window
from db import get_connection
from ui.welcome_ui import show_welcome
show_welcome()


def main():
    conn = get_connection()

    if conn is None:
        print("❌ Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dual")
        print("Test query result:", cursor.fetchone())
        cursor.close()
    except Exception as e:
        print("❌ Error running test query:", e)

    # ✅ Do NOT close the connection here
    # conn.close()  ← ❌ Remove this
    conn = get_connection()
   
 

    if conn:
     root = tk.Tk()
     root.title("Hospital Management System")
     show_login_window(root, conn)
     root.mainloop()




if __name__ == "__main__":
    main()