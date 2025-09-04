
# def book_appointment(conn, patient_id, doctor_id, date, time):
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status)
#         VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, 'Scheduled')
#     """, (patient_id, doctor_id, date, time))
#     conn.commit()
# from datetime import datetime

# appointment_time = datetime.strptime("10:30", "%H:%M")
# cursor.execute("""
#     INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status)
#     VALUES (:1, :2, :3, :4, :5)
# """, [patient_id, doctor_id, appointment_date, appointment_time, status])
# def book_appointment(conn, patient_id, doctor_id, date, status='Scheduled',appointment_time=None):
    
#     cursor = conn.cursor()
#     appointment_time = datetime.strptime(appointment_time, "%H:%M")
#     cursor.execute("""
#         INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, appointment_time)
#         VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, 'Scheduled')
#     """, (patient_id, doctor_id, date, status, appointment_time))
#     conn.commit()
from datetime import datetime
import tkinter.messagebox as messagebox

def book_appointment(conn, patient_id, doctor_id, appointment_date , appointment_time):
    try:
        appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
        appointment_time = int(appointment_time)  # assuming it's just hour like '10'

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, appointment_time)
            VALUES (:1, :2, :3, :4)
        """, [patient_id, doctor_id, appointment_date, "Confirmed", appointment_time])
        conn.commit()
        messagebox.showinfo("Success", "Appointment booked successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
