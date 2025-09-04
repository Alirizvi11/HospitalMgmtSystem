# import tkinter as tk
# from ui import  appointment_ui,patient_ui ,billing_ui, doctor_ui, medications_ui, report_ui  # ✅ Import your modules

# def show_dashboard(conn):
#     dashboard = tk.Tk()
#     dashboard.title("Dashboard")

#     tk.Label(dashboard, text="Welcome to Hospital Dashboard", font=("Arial", 16)).pack(pady=10)

#     # ✅ Add Patient (opens register_ui)
#    # tk.Button(dashboard, text="Register", width=20, command=lambda: register_ui.show_register(conn)).pack(pady=5)

#     # ✅ View Appointments
#     tk.Button(dashboard, text="View Appointments", width=20, command=lambda: appointment_ui.show_appointments(conn)).pack(pady=5)

#     # ✅ Add Patient Button
#     tk.Button(dashboard, text="Add Patient", width=20, command=lambda: patient_ui.show_patient_window(conn)).pack(pady=5)

#     # ✅ Billing
#     tk.Button(dashboard, text="Billing", width=20, command=lambda: billing_ui.show_billing(conn)).pack(pady=5)

#     # ✅ Doctor Info
#     tk.Button(dashboard, text="Doctor Info", width=20, command=lambda: doctor_ui.show_doctor_info(conn)).pack(pady=5)
 
#     # ✅ Medications
#     tk.Button(dashboard, text="Medications", width=20, command=lambda: medications_ui.show_medications(conn)).pack(pady=5)

#     # ✅ report generation
#     tk.Button(dashboard, text="Generate Report", width=20, command=lambda: report_ui.show_report_ui(conn)).pack(pady=5)

#     # ✅ Logout
#     tk.Button(dashboard, text="Logout", width=20, command=dashboard.destroy).pack(pady=5)

#     dashboard.mainloop()

import tkinter as tk
from ui import patient_ui, appointment_ui, billing_ui, doctor_ui, report_ui, medications_ui
# from PIL import Image, ImageTk
from ui import appointment_ui



# def show_dashboard(conn):
#     dashboard = tk.Toplevel()
#     dashboard.title("Hospital Dashboard")
#     dashboard.geometry("800x600")

#     bg = Image.open("assets/dashboard_bg.jpg").resize((800, 600))
#     bg_img = ImageTk.PhotoImage(bg)
#     bg_label = tk.Label(dashboard, image=bg_img)
#     bg_label.image = bg_img
#     bg_label.place(x=0, y=0)

#     tk.Label(dashboard, text="Welcome to Apollo Dashboard", font=("Helvetica", 18, "bold"), bg="#ffffff").pack(pady=20)

# def styled_button(text, command):
#     btn = tk.Button(dashboard, text=text, command=command, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=20)
#     btn.pack(pady=5)
#     return btn


def show_dashboard(conn):
    dashboard = tk.Toplevel()
    dashboard.title("Hospital Dashboard")
    dashboard.geometry("800x600")

    tk.Label(dashboard, text="Welcome to Dashboard", font=("Helvetica", 16)).pack(pady=20)

    def styled_button(text, command):
        btn = tk.Button(dashboard, text=text, command=command, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=20)
        btn.pack(pady=5)
        return btn

    styled_button("Add Patient", lambda: patient_ui.show_patient_window(conn))
    styled_button("View Appointments", lambda: appointment_ui.show_appointment_window(conn))
    styled_button("Billing", lambda: billing_ui.show_billing_window(conn))
    styled_button("Doctor Info", lambda: doctor_ui.show_doctor_window(conn))
    styled_button("Generate Report", lambda: report_ui.show_report_ui(conn))
    styled_button("Medications", lambda: medications_ui.show_medications(conn))
    styled_button("Logout", dashboard.destroy)


# styled_button("Add Patient", lambda: patient_ui.show_patient_window(conn))
# styled_button("View Appointments", lambda: appointment_ui.show_appointments(conn))
# styled_button("Billing", lambda: billing_ui.show_billing(conn))
# styled_button("Doctor Info", lambda: doctor_ui.show_doctor_info(conn))
# styled_button("Generate Report", lambda: report_ui.show_report_ui(conn))
# styled_button("Medications", lambda: medications_ui.show_medications(conn))
# styled_button("Logout", dashboard.destroy)
# dashboard.mainloop()
