import psycopg2

DB_HOST = 'localhost'
DB_PORT = '6455'
DB_NAME = 'db-2024-database'
DB_USER = 'postgres'
DB_PASSWORD = 'db2024'

TABLES_SQL_FILE = './postgres/tables.sql'

def execute_sql_file(conn, file_path):
    with open(file_path, 'r') as f:
        sql = f.read()
    with conn.cursor() as cursor:
        cursor.execute(sql)
    print("SQL script executed successfully.")

def init_db():
    try:
        conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
        )
        print(f"Connected to the database {DB_NAME} on {DB_HOST}:{DB_PORT}")

        execute_sql_file(conn, TABLES_SQL_FILE)

        conn.commit()
        conn.close()
        print(f"Connection to {DB_NAME} closed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    init_db()
