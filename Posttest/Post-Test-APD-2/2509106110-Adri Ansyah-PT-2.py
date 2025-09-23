Nim=input("Masukan Nim Anda: ")
Nama=input("Masukan Nama Anda: ")

Harga = int(input("Masukkan harga laptop: "))

print("\nPilih merek laptop:")
print("1. Acer (diskon 5%)")
print("2. Asus (diskon 7%)")
print("3. Lenovo (diskon 10%)")

pilihan = int(input("Masukkan pilihan (1-3): "))

match pilihan:
    case 1:
        merek, persen_diskon = "Acer", 5
    case 2:
        merek, persen_diskon = "Asus", 7
    case 3:
        merek, persen_diskon = "Lenovo", 10
    case _:
        merek, persen_diskon = "Tidak valid", 0

diskon = Harga * (persen_diskon / 100)
harga_akhir = Harga - diskon

print("\n===== STRUK PEMBELIAN =====")
print(f"Merek Laptop : {Nim}")
print(f"Merek Laptop : {Nama}")
print(f"Merek Laptop : {merek}")
print(f"Harga Awal   : Rp{Harga:,}")
print(f"Diskon       : {persen_diskon}% (Rp{int(diskon):,})")
print(f"Harga Akhir  : Rp{int(harga_akhir):,}")
print("============================")