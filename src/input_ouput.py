# src/input_output.py
from src.db import fetch_all_items, add_item, update_quantity

class InputOutput:

    def __init__(self):
        pass  # no need for self.items anymore

    def input_item(self):  # add new item
        code = input("Masukkan kode barang: ")
        name = input("Masukkan nama barang: ")
        qty = int(input("Masukkan jumlah: "))

        add_item(code, name, qty)  # insert into SQLite
        print(f"Barang {name} ditambahkan ke database.")

    def output_item(self):  # remove item from stock
        code = input("Masukkan kode barang yang keluar: ")

        items = fetch_all_items()
        for db_code, name, quantity in items:
            if db_code == code:
                qty = int(input("Jumlah keluar: "))
                if qty <= quantity:
                    new_quantity = quantity - qty
                    update_quantity(code, new_quantity)  # update SQLite
                    print(f"{qty} unit {name} dikeluarkan.")
                else:
                    print("Stok tidak cukup.")
                break
        else:
            print("Barang tidak ditemukan.")
