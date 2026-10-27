#modul fungsi mandiri

def tambah (a, b):
    """Mengambilkan hasil penjumalahan a + b"""
    return a + b

def kurang (a, b):
    """Mengambilkan hasil pengurangan a - b"""
    return a - b

def kali (a, b):
    """Mengambilkan hasil perkalian a * b"""
    return a * b

def bagi (a, b):
    """Mengambilkan hasil pembagian a / b. Mengenai pecahan error saat pembagi bernilai nol.
    Mengembalikan hasil pembagian a / b.
    Mengenai pecahan error saat pembagi bernilai nol.
    """

    if b == 0:
        return "Error: Pembagi tidak boleh nol."
    return a / b

def cek_ganjil_genap(angka):
    """Memerikasa sifat bilangan ganjil atau genap menggunakan operator modulus (%)."""
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    """Menghitung total akumulasi deret menggunakan perulangan for."""
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total

# Program utama
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Hasil tambah:", tambah(a, b))
print("Hasil kurang:", kurang(a, b))
print("Hasil kali:", kali(a, b))
print("Hasil bagi:", bagi(a, b))
