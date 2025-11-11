import sqlite3
import os

DB_PATH = os.path.join('data', 'database.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def fetch_all_items():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT code, name, quantity FROM inventory")
    rows = cursor.fetchall()
    connection.close()
    return rows  # list of tuples

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
    cursor.execute("UPDATE inventory SET quantity=? WHERE code=?", (quantity, code))
    connection.commit()
    connection.close()