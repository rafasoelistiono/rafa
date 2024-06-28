def cari_typo(teks, huruf_seharusnya, huruf_typo):
    hasil = teks.replace(huruf_typo, huruf_seharusnya)
    return hasil

# Contoh penggunaan fungsi
teks_asli = input("Masukkan teks: ")
huruf_seharusnya = input("Huruf yang seharusnya: ")
huruf_typo = input("Huruf typo: ")

teks_diperbaiki = cari_typo(teks_asli, huruf_seharusnya, huruf_typo)
print("Teks yang sudah diperbaiki:", teks_diperbaiki)

