#============================================
#Praktikum 3: DERET ARITMATIKA DAN AKUMULATOR
#============================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret    (b): "))

banyak = int(input("Masukkan Banyak Suku   (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silakan masukkan ulang Banyak Suku (n): "))


suku = awal
total = 0 

print("\nBarisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku   
    suku += beda     
print(f"\nTotal Jumlah Seluruh Deret = {total}")