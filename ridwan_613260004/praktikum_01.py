kehadiran = int(input("jumlah kehadiran (1-14): "))
nilai = int(input("nilai akhir (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
else:
        print("REMEDIAL - Nilai  Ujian Kurang ")
        
        print("TIDAK LULUS - Kehadiran Kurang dari 12")
