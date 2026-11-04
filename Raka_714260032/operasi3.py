def tambah(a, b):
    """mengembalikan hasil pengrangan a - b"""
    return a + b

def kurang(a, b):
    """mengembalikan hasil pengurangan a - b"""
    return a - b

def kali(a, b):
    """mengembalikan hasil perkalian a * b"""
    return a * b

def bagi(a, b):
    """mengembalikan hasil pembagian a / b.     menangani pencegahan error saat pembagi bernilai nol.
    mengembalikan hasil pembagian a / b
    menangani pencegahan error saat pembagi bernilai nol.
    """
    if b == 0:
        return "error: pembagi tidak boleh bernilai nol!"
    return a / b

def cek_ganjil_genap(angka):
    """     memeriksa sifat bilangan ganjil atau genap menggunakan operator modulus (%)     
    memeriksa sifat bilangan ganjil atau genap 
    menggunakan operator modulus (%)
    """
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "GANJIL"

def hitung_deret_aritmatika(awal, beda, n):
    """ menghitung total akumulasi deret menggunakan perulangan for """
    """  menghitung total akumulasi deret menggunakan  perulangan for """

    total = 0
    suku = awal 
    for i in range(n):
        total += suku
        suku += beda
        return total