def tambah (a, b):
    return a + b
def kurang (a, b):
    return a - b
def kali (a, b):
    return a * b
def bagi (a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return a / b

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda    
    return total