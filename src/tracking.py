from src.db import fetch_all_items

class Tracking:
    def __init__(self):
        pass

    def show_items(self):
        print("\n=== Daftar Barang ===")
        items = fetch_all_items()
        if not items:
            print("Belum ada barang.")
            return

        for code, name, qty in items:
            print(f"{code} | {name} | Stok: {qty}")
