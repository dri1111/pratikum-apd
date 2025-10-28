fruits_dict = {}
fruit_id = 1
login_status = False

def tambah_fruit(id_fruit, nama, kemampuan, kelangkaan):
    global fruits_dict
    fruits_dict[id_fruit] = {
        "Nama": nama,
        "Kemampuan": kemampuan,
        "Kelangkaan": kelangkaan
    }


def tampilkan_semua():
    global fruits_dict
    print("\n=== Daftar Devil Fruits ===")
    if not fruits_dict:
        print("Tidak ada fruits.")
    else:
        for id_fruit, data in fruits_dict.items():
            print(f"{id_fruit}. {data['Nama']} | Kemampuan: {data['Kemampuan']} | Kelangkaan: {data['Kelangkaan']}")


def login():
    global login_status
    username_terdaftar = "Adri Ansyah"
    password_terdaftar = "2509106110"

    print("=== Login Dulu Sebelum Mengakses Program ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_terdaftar and password == password_terdaftar:
        login_status = True
        print("Login berhasil!\n")
    else:
        print("Login gagal! Username atau password salah.\n")

def menu_utama():
    global fruit_id, fruits_dict

    while True:
        print("\n=== Devil Fruits Menu ===")
        print("1. Tambah Fruits")
        print("2. Lihat Fruits")
        print("3. Ubah Fruits")
        print("4. Hapus Fruits")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        nama_fruit = ""
        kemampuan_fruit = ""
        kelangkaan_fruit = ""
        id_ubah = 0
        id_hapus = 0

        try:
            if pilihan == "1":
                nama_fruit = input("Masukkan nama fruit: ")
                kemampuan_fruit = input("Masukkan kemampuan fruit: ")
                kelangkaan_fruit = input("Masukkan tingkat kelangkaan (Umum/Langka/Legenda): ")

                tambah_fruit(fruit_id, nama_fruit, kemampuan_fruit, kelangkaan_fruit)
                print(f"Fruit '{nama_fruit}' berhasil ditambahkan dengan ID {fruit_id}.")
                fruit_id += 1

            elif pilihan == "2":
                tampilkan_semua()

            elif pilihan == "3":
                tampilkan_semua()
                if not fruits_dict:
                    continue
                id_ubah = int(input("Masukkan ID fruit yang akan diubah: "))
                if id_ubah in fruits_dict:
                    nama_baru = input("Nama baru: ")
                    kemampuan_baru = input("Kemampuan baru: ")
                    kelangkaan_baru = input("Kelangkaan baru: ")
                    fruits_dict[id_ubah] = {
                        "Nama": nama_baru,
                        "Kemampuan": kemampuan_baru,
                        "Kelangkaan": kelangkaan_baru
                    }
                    print("Fruit berhasil diubah!")
                else:
                    print("ID tidak ditemukan.")

            elif pilihan == "4":
                tampilkan_semua()
                if not fruits_dict:
                    continue
                id_hapus = int(input("Masukkan ID fruit yang akan dihapus: "))
                if id_hapus in fruits_dict:
                    hapus = fruits_dict.pop(id_hapus)
                    print(f"Fruit '{hapus['Nama']}' berhasil dihapus.")
                else:
                    print("ID tidak ditemukan.")

            elif pilihan == "5":
                print("Program selesai")
                break

            else:
                print("Pilihan tidak valid!")

        except ValueError:
            print("harus berupa angka pada ID atau menu.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

login()
if login_status:
    menu_utama()
else:
    print("Harap login terlebih dahulu.")