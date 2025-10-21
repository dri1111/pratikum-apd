fruits_dict = {}
fruit_id = 1

while True:
    print("\n=== Devil Fruits ===")
    print("1. Tambah Fruits")
    print("2. Lihat Fruits")
    print("3. Ubah Fruits")
    print("4. Hapus Fruits")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama_fruit = input("Masukkan nama fruits: ")
        fruits_dict[fruit_id] = nama_fruit
        print(f"Fruits '{nama_fruit}' berhasil ditambah dengan ID {fruit_id}.")
        fruit_id += 1

    elif pilihan == "2":
        print("\n=== Daftar Fruits ===")
        if not fruits_dict:
            print("Tidak ada fruits.")
        else:
            for id_fruit, nama in fruits_dict.items():
                print(f"{id_fruit}. {nama}")

    elif pilihan == "3":
        print("\n=== Ubah Fruits ===")
        if not fruits_dict:
            print("Tidak ada fruits untuk diubah.")
        else:
            for id_fruit, nama in fruits_dict.items():
                print(f"{id_fruit}. {nama}")
            
            id_ubah = input("Pilih ID fruits yang akan diubah: ")
            if id_ubah.isdigit():
                id_ubah = int(id_ubah)
                if id_ubah in fruits_dict:
                    nama_baru = input("Nama fruits baru: ")
                    fruits_dict[id_ubah] = nama_baru
                    print("Fruits berhasil diubah.")
                else:
                    print("ID tidak ditemukan.")
            else:
                print("Input harus angka.")

    elif pilihan == "4":
        print("\n=== Hapus Fruits ===")
        if not fruits_dict:
            print("Tidak ada fruits untuk dihapus.")
        else:
            for id_fruit, nama in fruits_dict.items():
                print(f"{id_fruit}. {nama}")
            
            id_hapus = input("Pilih ID fruits yang akan dihapus: ")
            if id_hapus.isdigit():
                id_hapus = int(id_hapus)
                if id_hapus in fruits_dict:
                    nama_dihapus = fruits_dict.pop(id_hapus)
                    print(f"Fruits '{nama_dihapus}' berhasil dihapus.")
                else:
                    print("ID tidak ditemukan.")
            else:
                print("Input harus angka.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")