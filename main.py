import os
from src import InputOutput
from src import Tracking
from init_db import init_db
from src.db import fetch_all_items

DB_PATH = os.path.join('data', 'warehouse.db')

# Automatically initialize DB if it doesn't exist
if not os.path.exists(DB_PATH):
    init_db()

def main():
    io = InputOutput()

    while True:
        print("\n=== Warehouse Storage Management ===")
        print("1. Input barang")
        print("2. Output barang")
        print("3. Lihat stok")
        print("4. Keluar")
        choice = input("Choose option: ")

        if choice == "1":
            io.input_item()
        elif choice == "2":
            io.output_item()
        elif choice == "3":
            # fetch items from database
            items = fetch_all_items()
            tracker = Tracking()
            tracker.show_items()
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
