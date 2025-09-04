def add_patient(conn, name, gender, dob, address, phone):
    cursor = conn.cursor()
    query = """
        INSERT INTO patients (name, gender, dob, address, phone)
        VALUES (:1, :2, :3, :4, :5)
    """
    cursor.execute(query, (name, gender, dob, address, phone))
    conn.commit()

def get_all_patients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()
