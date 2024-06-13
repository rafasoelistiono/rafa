# Menghitung Massa Tubuh Index (BMI)
tinggi_badan = float(input("Masukkan tinggi badan (dalam meter): "))
berat_badan = float(input("Masukkan berat badan (dalam kilogram): "))

bmi = berat_badan / (tinggi_badan ** 2)

print("Massa Tubuh Index (BMI) Anda adalah:", bmi)
if bmi < 18.5:
    print("Berat badan kurang")
elif bmi >= 18.5 and bmi < 24.9:
    print("Berat badan normal")
elif bmi >= 24.9 and bmi < 29.9:
    print("Berat badan berlebih")
else:
    print("Obesitas")

