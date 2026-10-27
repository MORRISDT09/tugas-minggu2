def cek_prima(angka):
    is_prima = True  

    if angka < 2:
        is_prima = False
    else:
        for pembagi in range(2, angka):
            if angka % pembagi == 0:
                is_prima = False  
                break

    return is_prima



angka = int(input("Masukkan angka: "))

if cek_prima(angka):
    print(f"{angka} adalah BILANGAN PRIMA")
else:
    print(f"{angka} BUKAN bilangan prima")