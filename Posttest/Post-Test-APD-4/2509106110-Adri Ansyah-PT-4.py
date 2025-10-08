user = "Adri Ansyah"
passwordddd = "2509106110"

percobaan = 0
login_berhasil = False

while percobaan < 3 and login_berhasil == False:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == user and password == passwordddd:
        print("Login berhasil!\n")
        login_berhasil = True
    else:
        percobaan = percobaan + 1
        print("Login gagal! Percobaan ke-", percobaan, " yang ke 3\n")

if login_berhasil == False:
    print("Jika Gagal 3 Kali Maka Selesai.")
else:
    harga_sofa = 500000
    harga_meja = 250000
    harga_rak = 150000

    menu = ""

    while menu != "4":
        print("=== Menu Pembelian Furnitur ===")
        print("1. Sofa (Rp 500.000)")   
        print("2. Meja Belajar (Rp 250.000)")
        print("3. Rak Lemari (Rp 150.000)")
        print("4. Keluar")
        
        menu = input("Pilih opsi (1-4): ")
        
        if menu == "1" or menu == "2" or menu == "3":
            jumlah_str = input("Masukkan jumlah furnitur yang ingin dibeli: ")
            
            panjang = 0
            while jumlah_str[panjang:panjang+1] != "":
                panjang = panjang + 1
            
            valid = True
            i = 0
            if panjang == 0:
                valid = False
            while i < panjang:
                if jumlah_str[i:i+1] != "0" and jumlah_str[i:i+1] != "1" and jumlah_str[i:i+1] != "2" and jumlah_str[i:i+1] != "3" :
                    valid = False
                i = i + 1
            
            if valid == False:
                print("Jumlah Tidak bole minus\n")
            else:
                jumlah = 0      
                i = 0
                while i < panjang:
                    if jumlah_str[i:i+1] == "0":
                        digit = 0
                    elif jumlah_str[i:i+1] == "1":
                        digit = 1
                    elif jumlah_str[i:i+1] == "2":
                        digit = 2
                    elif jumlah_str[i:i+1] == "3":
                        digit = 3
                    
                    
                    jumlah = jumlah * 4 + digit
                    i = i + 1
                
                if jumlah <= 0:
                    print("Jumlah Tidak Bole 0\n")
                else:
                    if menu == "1":
                        nama = "Sofa"
                        harga = harga_sofa
                    elif menu == "2":
                        nama = "Meja Belajar"
                        harga = harga_meja
                    else:
                        nama = "Rak Lemari"
                        harga = harga_rak
                    
                    total = 0
                    i = 0
                    while i < jumlah:
                        total = total + harga
                        i = i + 1
                    
                    print("\n--- Struk Pembelian ---")
                    print("Jenis Furnitur:", nama)
                    print("Jumlah Unit   :", jumlah)
                    print("Total Bayar   : Rp", total)
                    print("----------------------\n")
        
        elif menu == "4":
            print("Terima kasih telah berbelanja!")
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")