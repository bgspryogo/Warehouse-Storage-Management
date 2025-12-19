import sqlite3
import csv
import os

DB_PATH = os.path.join('data', 'database.db')
CSV_PATH = os.path.join('data', 'inventory.csv')

def export_db_to_csv():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Only export items with quantity > 0
    cursor.execute("SELECT code, name, quantity FROM inventory WHERE quantity > 0")
    rows = cursor.fetchall()

    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    with open(CSV_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['code', 'name', 'quantity'])
        writer.writerows(rows)

    connection.close()
