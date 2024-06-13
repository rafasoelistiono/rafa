class Kasir:
    def __init__(self):
        self.barang = {}
        self.total_harga = 0

    def tambah_barang(self, nama, harga, jumlah):
        if nama in self.barang:
            self.barang[nama]['jumlah'] += jumlah
        else:
            self.barang[nama] = {'harga': harga, 'jumlah': jumlah}
        self.total_harga += harga * jumlah

    def hapus_barang(self, nama, jumlah):
        if nama in self.barang:
            if self.barang[nama]['jumlah'] <= jumlah:
                self.total_harga -= self.barang[nama]['harga'] * self.barang[nama]['jumlah']
                del self.barang[nama]
            else:
                self.barang[nama]['jumlah'] -= jumlah
                self.total_harga -= self.barang[nama]['harga'] * jumlah

    def tampilkan_total(self):
        print(f"Total Harga: Rp{self.total_harga}")

    def tampilkan_barang(self):
        for nama, info in self.barang.items():
            print(f"{nama}: {info['jumlah']} x Rp{info['harga']}")

    def reset(self):
        self.barang = {}
        self.total_harga = 0

def main():
    kasir = Kasir()
    while True:
        print("\n1. Tambah Barang\n2. Hapus Barang\n3. Tampilkan Total\n4. Tampilkan Barang\n5. Reset\n6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nama = input("Nama Barang: ")
            harga = int(input("Harga Barang: "))
            jumlah = int(input("Jumlah Barang: "))
            kasir.tambah_barang(nama, harga, jumlah)
        elif pilihan == '2':
            nama = input("Nama Barang: ")
            jumlah = int(input("Jumlah Barang: "))
            kasir.hapus_barang(nama, jumlah)
        elif pilihan == '3':
            kasir.tampilkan_total()
        elif pilihan == '4':
            kasir.tampilkan_barang()
        elif pilihan == '5':
            kasir.reset()
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
