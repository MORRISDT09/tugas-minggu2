#DERET ARITMATIKA

print("=== Deret Aritmatika === PROGRAM HITUNG DERET ARITMATIKA ====")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret (b): "))

#1. IMPLEMENTASI WHILE: Validasi input jumlah jumlah suku agar harus positif ( > 0)
banyak = int(input("Masukkan banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silakan Masukkan Ulang Banyak Suku (n): "))

#2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0 # Celengan Aktulator

print("Barisan Deret:", end=" ")
for i in range(banyak):
    print(suku, end=" ")
    total += suku      # Akumulasi penjumlahan terhadap
    suku += beda       # Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")