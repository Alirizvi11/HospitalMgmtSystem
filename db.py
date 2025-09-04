import cx_Oracle

def get_connection():
    try:
        print("🔗 Connecting to Oracle Database...")
        connection = cx_Oracle.connect("u1/u1@192.168.56.50:1521/pdbprim1")
        print("✅ Connected to Oracle Database successfully!")
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("❌ Oracle DB Error:")
        print("  Code:", error.code)
        print("  Message:", error.message)
        print("  Context:", error.context)
        return None
