import sqlite3
import os

DB_PATH = os.path.join('data', 'database.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def fetch_all_items():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT code, name, quantity FROM inventory WHERE quantity > 0")
    rows = cursor.fetchall()
    connection.close()
    return rows


def add_item(code, name, quantity):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT OR REPLACE INTO inventory (code, name, quantity) VALUES (?, ?, ?)",
                   (code, name, quantity))
    connection.commit()
    connection.close()

def update_quantity(code, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    if quantity > 0:
        cursor.execute("UPDATE inventory SET quantity=? WHERE code=?", (quantity, code))
    else:
        # Delete the item if quantity <= 0
        cursor.execute("DELETE FROM inventory WHERE code=?", (code,))

    connection.commit()
    connection.close()
