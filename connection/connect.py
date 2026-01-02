import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
config = {
    'host' : os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute('SELECT * FROM Jonas')
result = cursor.fetchall()

cursor.close()
conn.close()