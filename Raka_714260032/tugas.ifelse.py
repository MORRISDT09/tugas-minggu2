# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Muhammad Raka Nizami Aliansyah
# NIM   : 714260032
# Kelas : D4 TI 1A
# ==================================================

nilai = float(input("Masukkan nilai akhir Anda (0-100): "))

print("=========================================")

if nilai < 0 or nilai > 100:
    print("Kesalahan: Nilai harus berada dalam rentang 0 hingga 100.")
else:
    if nilai >= 80:
        huruf = "A"
        status = "LULUS"
    elif nilai >= 70:
        huruf = "B"
        status = "LULUS"
    elif nilai >= 60:
        huruf = "C"
        status = "LULUS"
    elif nilai >= 50:
        huruf = "D"
        status = "TIDAK LULUS"
    else:
        huruf = "E"
        status = "TIDAK LULUS"

    print(f"Nilai Anda  : {nilai:.1f}")
    print(f"Huruf Mutu  : {huruf}")
    print(f"Status      : {status}")

print("=========================================")
print("Terima kasih telah menggunakan program ini.")