kehadiran = int(input("jumlah kehadiran (1-14): "))
nilai = int(input("nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - nilai memuaskan")
    else:
        print("REMEDIAL - nilai ujian kurang")
else:
    print("TIDAK LULUS - kehadiran kurang dari 12")