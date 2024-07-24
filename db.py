import mysql.connector
from config import Config

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
            )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def execute_query(query, params=None):
    try:
        connection = connect_to_database()
        cursor = connection.cursor(buffered=True)
        cursor.execute(query, params)
        connection.commit()
        return cursor.fetchall() if query.lower().startswith('select') else None
    except mysql.connector.Error as err:
        print(err)
        return None
