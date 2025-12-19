from src.db import fetch_all_items, add_item, update_quantity
from src.utils import export_db_to_csv

class InputOutput:

    def __init__(self):
        pass

    def input_item(self):
        code = input("Masukkan kode barang: ")
        name = input("Masukkan nama barang: ")
        qty = int(input("Masukkan jumlah: "))

        add_item(code, name, qty)
        export_db_to_csv()  # << automatically update CSV
        print(f"Barang {name} ditambahkan ke database dan CSV diperbarui.")
        

    def output_item(self):
        code = input("Masukkan kode barang yang keluar: ")

        items = fetch_all_items()
        for db_code, name, quantity in items:
            if db_code == code:
                qty = int(input("Jumlah keluar: "))
                if qty <= quantity:
                    new_quantity = quantity - qty
                    update_quantity(code, new_quantity)  # this will delete if 0
                    export_db_to_csv()  # update CSV to reflect deletion
                    print(f"{qty} unit {name} dikeluarkan, stok diperbarui.")
                else:
                    print("Stok tidak cukup.")
                break
        else:
            print("Barang tidak ditemukan.")
