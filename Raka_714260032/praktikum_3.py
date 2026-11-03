awal = int(input("masukan suku pertama (a): "))
beda = int(input("masukan beda deret (b): "))

# 1. IMPLENTASI WHILE: Validasi input jumlah suku  agar harus positif (> 3)
banyak = int(input("masukan banyak suku (n): "))
while banyak <= 0:
    print("peringatan: banyak suku harus lebih dari 0!")
    banyak = int(input("silakan masukan ulang banyak suku (n): "))

# 2. IMPLENTASI FOR & AKUMULATOR: mencetak deret dan menjumlahkan totalnya 
suku = awal
total = 0 # celengan akumulator
print("barisan deret: ", end="")
for i in range(banyak):
    print(suku, end="")
    total += suku   # akumulasi penjumlahan bertahap
    suku += beda    # menyiapkan suatu berikutnya 

print(f"total jumlah seluruh deret = {total}")