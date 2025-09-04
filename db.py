import cx_Oracle

# Replace with your actual database credentials
username = 'u1'
password = 'u1'
host = '192.168.56.50'         # or IP address of DB server
port = 1521
service_name = 'PDBPRIM1'      # or 'xe', 'pdborcl', etc.

# Build the DSN (Data Source Name)

def get_connection():
  try:
    dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
    print("🔗 Connecting to Oracle Database...")
    # Create the database connection
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("✅ Connected to Oracle Database successfully!")
    return connection
    # (Optional) Run a test query
   #
  except cx_Oracle.DatabaseError as e:
    print("❌ Database connection error:", e)
    return None