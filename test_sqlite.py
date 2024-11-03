import sqlite3
import os

db_path = 'instance/mydatabase.db'

# Ensure the instance directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create a test table
    cursor.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)''')
    
    conn.commit()
    print(f"Successfully created database at {db_path}")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
