kehadiran  = int(input("Jumlah Kehadiran(1-14): "))
nilai = int(input("Nilai ujian(0-100): ")) 

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
        print("REMEDIAL - Nilai Ujian Kurang")
else:
    print("TIDAK LULUS - Kehadiran Kurang Dari 12")
          