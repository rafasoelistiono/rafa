panjang = int(input("Masukkan Panjang: "))
lebar = int(input("Masukkan Lebar: "))

luas = panjang*lebar

print("luas total: ", luas, "m")

if luas > 20 or luas < 15:
    print("proyek gagal")
else:
    print("proyek berhasil")