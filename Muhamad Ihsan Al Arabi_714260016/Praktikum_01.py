#====================================
#Praktikum 1: NESTED IF (EVALUASI KELULUSAN)
#====================================

kehadiran = int(input("Masukkan jumlah kehadiran (1-14): "))    
nilai = int(input("nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >=75:
        print("LULUS-Nilai Memuaskan")
    else:
        print("REMEDIAL-Nilai Ujian Kurang ")
else:
    print("TIDAK LULUS-Kehadiran Kurang dari 12 kali")
    