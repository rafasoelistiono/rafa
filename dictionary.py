# Membuat dictionary dan mengakses nilainya
mahasiswa = {
    "nama": "Rafa Rally Soelistiono",
    "usia": 20,
    "jurusan": "Ilmu Komputer",
    "universitas": "Universitas Indonesia"
}

# Mengakses nilai dalam dictionary
print(mahasiswa["nama"])       # Output: Rafa Rally Soelistiono
print(mahasiswa["usia"])       # Output: 20
print(mahasiswa["jurusan"])    # Output: Ilmu Komputer
print(mahasiswa["universitas"])# Output: Universitas Indonesia

# Menambahkan dan menghapus elemen dalam dictionary
# Menambahkan elemen baru
mahasiswa["angkatan"] = 2022
print(mahasiswa)
# Output: {'nama': 'Rafa Rally Soelistiono', 'usia': 20, 'jurusan': 'Ilmu Komputer', 'universitas': 'Universitas Indonesia', 'angkatan': 2022}

# Menghapus elemen
del mahasiswa["usia"]
print(mahasiswa)
# Output: {'nama': 'Rafa Rally Soelistiono', 'jurusan': 'Ilmu Komputer', 'universitas': 'Universitas Indonesia', 'angkatan': 2022}

# Menggunakan loop untuk mengakses dictionary
# Loop melalui keys dan values
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
# Output:
# nama: Rafa Rally Soelistiono
# jurusan: Ilmu Komputer
# universitas: Universitas Indonesia
# angkatan: 2022

# Menggunakan metode dictionary
# Mendapatkan semua keys
keys = mahasiswa.keys()
print(keys)
# Output: dict_keys(['nama', 'jurusan', 'universitas', 'angkatan'])

# Mendapatkan semua values
values = mahasiswa.values()
print(values)
# Output: dict_values(['Rafa Rally Soelistiono', 'Ilmu Komputer', 'Universitas Indonesia', 2022])

# Mendapatkan semua items
items = mahasiswa.items()
print(items)
# Output: dict_items([('nama', 'Rafa Rally Soelistiono'), ('jurusan', 'Ilmu Komputer'), ('universitas', 'Universitas Indonesia'), ('angkatan', 2022)])

# Menggunakan dictionary dengan list dan nested dictionary
# List of dictionaries
kelas = [
    {"nama": "Rafa", "nilai": 85},
    {"nama": "Andi", "nilai": 90},
    {"nama": "Budi", "nilai": 75}
]

# Mengakses elemen dalam list of dictionaries
for siswa in kelas:
    print(f"Nama: {siswa['nama']}, Nilai: {siswa['nilai']}")
# Output:
# Nama: Rafa, Nilai: 85
# Nama: Andi, Nilai: 90
# Nama: Budi, Nilai: 75

# Nested dictionary
universitas = {
    "UI": {
        "lokasi": "Depok",
        "fakultas": ["Ilmu Komputer", "Teknik", "Ekonomi"]
    },
    "UGM": {
        "lokasi": "Yogyakarta",
        "fakultas": ["Kedokteran", "Hukum", "Sastra"]
    }
}

# Mengakses nested dictionary
print(universitas["UI"]["lokasi"])              # Output: Depok
print(universitas["UGM"]["fakultas"][0])        # Output: Kedokteran
