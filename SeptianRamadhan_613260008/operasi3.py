def tambah(a, b):
    """Mengembalikan hasil penjumlahan a + b"""
    return a + b

def kurang(a, b):
    """Mengembalikan hasil pengurangan a - b"""
    return a - b

def kali(a, b):
    """Mengembalikan hasil perkalian a * b"""
    return a * b

def bagi(a, b):
    """Mengembalikan hasil pembagian a / b.     Menangani pencegahan error saat pembagi bernilai nol.
    Mengembalikan hasil pembagian a / b.
    menangani pencegahan error saat pembagi bernilai nol.
    """
    if b == 0:
        return "Error: Pembagi tidak boleh bernilai nol!"
    return a / b

def cek_ganjil_genap(angka):
    """     Memeriksa sifat bilangan ganjil atau genap     menggunakan operator modulus (%)
    Memeriksa sifat bilangan ganjil dan genap
    menggunakan operator modulus (%)
    """
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    """Menghitung total akumulasi deret menggunakan perulangan for  
    Menghitung total akumulasi deret menggunakan perulangan for
    """
    suku = awal
    total = 0
    for i in range(n):
        total += suku
        suku += beda
    return total

