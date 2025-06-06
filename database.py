import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            # host="localhost",
            # user="root",
            # password="",
            # port=3306,
            # database="xella-user"

            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASSWORD"),
            database=os.getenv("DBNAME"),
            port=3306
        )
        if connection.is_connected():
            print("✅ Connection successful!")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None
    

# connect_to_database()

