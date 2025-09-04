def add_doctor(conn, name, specialization, phone, email):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doctors (name, specialization, phone, email)
        VALUES (:1, :2, :3, :4)
    """, (name, specialization, phone, email))
    conn.commit()