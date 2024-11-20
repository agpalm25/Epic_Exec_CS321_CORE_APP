"""
Test script for SQLite database creation and basic operations.

This script creates a SQLite database, ensures the necessary directory structure,
and creates a test table to verify database functionality.
"""

import sqlite3
import os
from typing import Optional

def create_test_database(db_path: str) -> None:
    """
    Create a test SQLite database and a sample table.

    Args:
        db_path (str): The path where the database file should be created.
    """
    # Ensure the instance directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    connection: Optional[sqlite3.Connection] = None
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            # Create a test table
            cursor.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)''')

            connection.commit()
        print(f"Successfully created database at {db_path}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()

def main() -> None:
    """Main function to run the database creation test."""
    db_path = 'instance/mydatabase.db'
    create_test_database(db_path)

if __name__ == "__main__":
    main()
