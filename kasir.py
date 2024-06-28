print("====== Program Kasir Sederhana ======")
print("SILAHKAN PILIH MENU")
print("1. Esteh = 5000 \n2. Esjeruk = 6000 \n3. Eskelapa = 7000 \n4. Eskrim = 10000 \n5. Esalpukat = 15000")
menu_harga = {"1": 5000,"2": 6000,"3": 7000,"4": 10000,"5": 15000}

pilihan = input("Mau yang mana (1-5)? ")
#str,int,bool,float



if pilihan in menu_harga:
    jumlah = int(input("Berapa banyak? "))
    total_harga = jumlah * menu_harga[pilihan]
    print("total harga untuk", jumlah, "porsi adalah rp", total_harga)
else:
    print("Pilihan tidak tersedia, silakan masukkan angka 1-5.")
