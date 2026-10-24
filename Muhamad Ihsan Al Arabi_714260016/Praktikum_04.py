#============================================
#Praktikum 4: NESTED LOOP DAN PENGOLAHAN LIST
#============================================

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom} = {baris*kolom}", end=" ")
    print()  

nilai_maba = [12, 32-35]
nilai_maba.append(95)

print("Daftar Nilai Mahasiswa Baru:", nilai_maba)
print("Nilai Mahasiswa Baru Terbesar:", max(nilai_maba))