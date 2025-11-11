import sqlite3
import csv
import os

def init_db():
    #database path
    DB_PATH = os.path.join('data', 'database.db')
    CSV_PATH = os.path.join('data', 'inventory.csv')

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        code TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER
    )
    ''')

    # Load CSV data into the database
    with open(CSV_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT OR REPLACE INTO inventory (code, name, quantity)
                VALUES (?, ?, ?)
            ''', (row['code'], row['name'], int(row['quantity'])))

    # Commit and close
    connection.commit()
    connection.close()

    print("✅ SQLite database initialized from CSV!")