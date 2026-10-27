# NESTED LOOP & PENGOLAHAN LIST

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris * kolom}", end=" ")
    print()  # Pindah ke baris

#2. Pengenalan lis data
nilai_maba = [12, 32-35]
nilai_maba.append(95)   #Menambah data di akhir

print("Daftar Nilai :", nilai_maba)
print("Nilai Tertinggi :", max(nilai_maba))