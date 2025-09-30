
Nama_Mahasiswa = "Adri Ansyah"
NIM_Mahasiswa = "2509106110"

nama = input("Masukkan Nama: ")
nim  = input("Masukkan NIM : ")

if nama == Nama_Mahasiswa and nim == NIM_Mahasiswa:
    print("\nLogin Telah berhasil.")
    print("UKT Anda sebesar Rp 6.000.000\n")

    print("Pilihan pembayaran:")
    print("1. Lunas (1%)")
    print("2. Cicilan 2x semester (5%)")
    print("3. Cicilan 4x semester (8%)")
    print("4. Cicilan 6x semester (12%)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        bayar = 0.01 * 6000000
        total = 6000000 + bayar
        print("\n=== Pembayaran Lunas ===")
        print("Biaya UKT :", bayar)
        print("Pembayaran Kuliah Mahasiswa :", total)

    elif pilihan == "2":
        bayar = 0.05 * 6000000
        total = 6000000 + bayar
        cicilan = total / 2
        print("\n=== Pembayaran Cicilan 2x ===")
        print("Biaya UKT :", bayar)
        print("Pembayaran Kuliah Mahasiswa :", total)
        print("Cicilan per Semester :", cicilan)

    elif pilihan == "3":
        bayar = 0.08 * 6000000
        total = 6000000 + bayar
        cicilan = total / 4
        print("\n=== Pembayaran Cicilan 4x ===")
        print("Biaya UKT :", bayar)
        print("Pembayaran Kuliah Mahasiswa :", total)
        print("Cicilan per Semester :", cicilan)

    elif pilihan == "4":
        bayar = 0.12 * 6000000
        total = 6000000 + bayar
        cicilan = total / 6
        print("\n=== Pembayaran Cicilan 6x ===")
        print("Biaya UKT :", bayar)
        print("Pembayaran Kuliah Mahasiswa :", total)
        print("Cicilan per Semester :", cicilan)

    else:
        print("Pilihan tidak valid.")

else:
    print("\nLogin gagal! Nama atau NIM salah.")