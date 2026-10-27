def tambah(a, b):
    """mengembalikan hasil penjumlahan a+b"""
    return a + b


def kurang(a, b):
    """mengembalikan hasil pengurangan a-b"""
    return a - b


def kali(a, b):
    """mengembalikan hasil perkalian a*b"""
    return a * b


def bagi(a, b):
    """mengembalikan hasil pembagian a/b dan menangani pencegahan error saat pembagi bernilai nol."""
    if b == 0:
        return "error: pembagi tidak boleh nol!"
    return a / b


def cek_ganjil_genap(angka):
    """memeriksa sifat bil ganjil atau genap menggunakan operator modulus (%)"""
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "ganjil"


def hitung_deret_aritmatika(awal, beda, n):
    """menghitung total akumulasi deret menggunakan perulangan for"""
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total
