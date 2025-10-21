
Fruits= []

Devil_fruits = ""

while Devil_fruits != "5":
    print("\n=== Devil Fruits ===")
    print("1. Tambah Fruits")
    print("2. Lihat Fruits")
    print("3. Ubah Fruits")
    print("4. Hapus Fruits")
    print("5. Keluar")

    Devil_fruits = input("Pilih pemilihan fruits (1-5): ")

    if Devil_fruits == "1":
        nama_fruits = input("Masukkan nama fruits: ")
        Fruits.append(nama_fruits)
        print("Fruits berhasil ditambah.")

    elif Devil_fruits == "2":
        print("\n=== Daftar Fruits ===")
        i = 0
        while i < len(Fruits):
            print(i, ".", Fruits[i])
            i = i + 1

    elif Devil_fruits == "3":
        print("\n=== Ubah Fruits ===")
        i = 0
        while i < len(Fruits):
            print(i, ".", Fruits[i])
            i = i + 1

        index = int(input("pilih untuk mengubah Nama Fruits: "))
        fruits_baru = input("Fruits: ")
        Fruits[index] = fruits_baru
        print("fruits berhasil diubah.")

    elif Devil_fruits == "4":
        print("\n=== Hapus Data ===")
        i = 0
        while i < len(Fruits):
            print(i, ".",Fruits[i])
            i = i + 1

        index = int(input("Fruits yang mau hapus: "))
        Fruits.pop(index)
        print("Fruits berhasil dihapus.")

    elif Devil_fruits == "5":
        print()

    else:
        print("Pilihan tidak valid.")