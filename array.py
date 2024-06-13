# Membuat dan mengakses elemen array
buah = ["apel", "pisang", "jeruk"]

# Mengakses elemen array
print(buah[0])  # Output: apel
print(buah[1])  # Output: pisang
print(buah[2])  # Output: jeruk

# Menambahkan elemen ke array
buah.append("mangga")
print(buah)  # Output: ['apel', 'pisang', 'jeruk', 'mangga']

# Menghapus elemen dari array dengan nilai
buah.remove("pisang")
print(buah)  # Output: ['apel', 'jeruk', 'mangga']

# Menghapus elemen dari array dengan indeks
del buah[1]
print(buah)  # Output: ['apel', 'mangga']

# Mengakses elemen dengan loop
for item in buah:
    print(item)
# Output:
# apel
# mangga

# Menggunakan list comprehension
# Membuat list dengan list comprehension
angka = [x for x in range(10)]
print(angka)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Membuat list dengan list comprehension dengan kondisi
genap = [x for x in range(10) if x % 2 == 0]
print(genap)  # Output: [0, 2, 4, 6, 8]

# Menggunakan array dua dimensi
# Membuat array dua dimensi
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mengakses elemen array dua dimensi
print(matrix[0][0])  # Output: 1
print(matrix[1][2])  # Output: 6
print(matrix[2][1])  # Output: 8

# Mengakses elemen dengan loop
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9 

# Menghitung panjang array
print(len(buah))  # Output: 2
print(len(matrix))  # Output: 3

# Mengurutkan array
angka = [5, 3, 8, 6, 2]
angka.sort()
print(angka)  # Output: [2, 3, 5, 6, 8]

# Mengurutkan array secara terbalik
angka.sort(reverse=True)
print(angka)  # Output: [8, 6, 5, 3, 2]

# Menggunakan metode array lain
# Menambahkan beberapa elemen
buah.extend(["nanas", "kiwi"])
print(buah)  # Output: ['apel', 'mangga', 'nanas', 'kiwi']

# Menemukan indeks dari elemen
index_apel = buah.index("apel")
print(index_apel)  # Output: 0

# Menghitung jumlah elemen tertentu
jumlah_mangga = buah.count("mangga")
print(jumlah_mangga)  # Output: 1

# Contoh Kasus 1: Menghitung rata-rata nilai siswa
nilai = [80, 90, 70, 85, 95]

# Menghitung total nilai
total_nilai = sum(nilai)

# Menghitung rata-rata nilai
rata_rata = total_nilai / len(nilai)
print(f"Rata-rata nilai siswa: {rata_rata}")
# Output: Rata-rata nilai siswa: 84.0

# Contoh Kasus 2: Menghitung jumlah kemunculan setiap elemen dalam list
buah = ["apel", "pisang", "jeruk", "apel", "jeruk", "apel"]

# Menghitung jumlah kemunculan setiap elemen
jumlah_apel = buah.count("apel")
jumlah_pisang = buah.count("pisang")
jumlah_jeruk = buah.count("jeruk")

print(f"Apel: {jumlah_apel}")
print(f"Pisang: {jumlah_pisang}")
print(f"Jeruk: {jumlah_jeruk}")
# Output:
# Apel: 3
# Pisang: 1
# Jeruk: 2

# Contoh Kasus 3: Membalik urutan array
angka = [1, 2, 3, 4, 5]

# Membalik urutan array
angka.reverse()
print(angka)  # Output: [5, 4, 3, 2, 1]
