def tambah(a, b):
    "mengembalikan hasil penjumlahan a + b"
    return a + b

def kurang(a, b):
    "mengembalikan hasil pengurangan a - b"
    return a - b

def kali(a, b):
    "mengembalikan hasil perkalian a * b"
    return a * b

def bagi(a, b):
    "mengembalikan hasil pembagian a / b"
    if b == 0:
        return "Error: Pembagian oleh nol tidak diperbolehkan"
    return a / b

def cek_ganjil_genap(angka):
    "mengembalikan True jika angka ganjil, False jika genap"
    return angka % 2 != 0
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "GANJIL"

def hitung_deret_aritmatika(awal, beda, n):
    "menghitung deret aritmatika dan mengembalikan list deret serta totalnya"
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total