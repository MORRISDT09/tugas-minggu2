for baris in range(1, 4):
    for kolom in range (1, 4):
        print(f"{baris}x{kolom}={baris*kolom}" , end=" ")
        print() # pindah garis

# pengenalan list data nilai
nilai_maba = [12, 32-35]
nilai_maba.append(95) # menambah data di akhir
print("daftar nilai :", nilai_maba)
print("nilai tertinggi:", max(nilai_maba))