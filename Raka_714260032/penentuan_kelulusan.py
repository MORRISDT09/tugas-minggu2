kehadiran = int(input("jumlah kehadiran (1-14): "))
nilai = int(input("nilai ujian (0-100) "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai memuaskan")
    else:
        print("REMEDIAL - Nilai Ujian Kurang")
else:
    print("TIDAK LULUS Kehadiran Kurang Dari 12")