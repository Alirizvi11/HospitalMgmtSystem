def validate_login(username, password, conn):
    cursor = conn.cursor()
    query = """
        SELECT ROLE FROM USERS
        WHERE USERNAME = :1 AND PASSWORD = :2
    """
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result[0] if result else None
