def generate_bill(conn, patient_id, amount, bill_date, paid_status='Unpaid'):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bills (patient_id, amount, bill_date, paid_status)
        VALUES (:1, :2, SYSDATE, 'Unpaid')
    """, (patient_id, amount, bill_date, paid_status))
    conn.commit()