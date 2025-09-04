def add_patient(conn, name, gender, dob, address,phone):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (name, gender, dob, address,phone)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5)
    """, (name, gender, dob, address ,phone))
    conn.commit()

def get_all_patients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()