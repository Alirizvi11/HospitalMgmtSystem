def generate_bill(conn, patient_id, amount, paid_status='Unpaid'):
    cursor = conn.cursor()
    query = """
        INSERT INTO billing (patient_id, amount, billing_date, payment_status)
        VALUES (:1, :2, SYSDATE, :3)
    """
    cursor.execute(query, (patient_id, amount, paid_status))
    conn.commit()

def get_bill_by_patient(conn, patient_id):
    cursor = conn.cursor()
    query = """
        SELECT b.bill_id, b.amount, b.billing_date, b.payment_status,
               p.name, p.gender, p.address
        FROM billing b
        JOIN patients p ON b.patient_id = p.patient_id
        WHERE b.patient_id = :1
        ORDER BY b.billing_date DESC
    """
    cursor.execute(query, (patient_id,))
    return cursor.fetchall()
