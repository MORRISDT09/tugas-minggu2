import operasi3

while True:
    print()
    print("===== KALKULATOR KONSOL =====")
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Ganjil / Genap (Modulus %)")
    print("3. Hitung Deret Aritmatika (for & Akumulasi)")
    print("4. Hitung Deret Aritmatika (while)")
    print("5. Keluar")
    print()
    pilihan = input("PILIH menu [1-5]: ")

    if pilihan == "1":
        # OPSI 1: OPERASI ARITMATIKA DASAR
        print()
        print("--- Operasi Aritmatika Dasar ---")
        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(f"  {a} + {b} = {operasi3.tambah(a, b)}")
            print(f"  {a} - {b} = {operasi3.kurang(a, b)}")
            print(f"  {a} * {b} = {operasi3.kali(a, b)}")
            print(f"  {a} / {b} = {operasi3.bagi(a, b)}")
        except ValueError:
            print("Input harus angka!")
        except Exception as e:
            print(f"Terjadi error: {e}")

    elif pilihan == "2":
        # OPSI 2: CEK GANJIL / GENAP / MODULUS
        print()
        print("--- Cek Ganjil / Genap (Modulus %) ---")
        try:
            angka = int(input("Masukkan angka: "))
            hasil = operasi3.cek_ganjil_genap(angka)
            print(f"Angka {angka} adalah {hasil}")
        except ValueError:
            print("Input harus angka bulat!")
        except Exception as e:
            print(f"Terjadi error: {e}")

    elif pilihan == "3":
        # OPSI 3: HITUNG DERET ARITMATIKA (FOR)
        print()
        print("--- Hitung Deret Aritmatika (for) ---")
        try:
            awal = int(input("Nilai awal: "))
            beda = int(input("Beda: "))
            n = int(input("Jumlah suku (n): "))
            total = operasi3.hitung_deret_aritmatika(awal, beda, n)
            print(f"Total deret aritmatika: {total}")
        except ValueError:
            print("Input harus angka bulat!")
        except Exception as e:
            print(f"Terjadi error: {e}")

    elif pilihan == "4":
        # OPSI 4: HITUNG DERET ARITMATIKA (WHILE - MANUAL DI MAIN)
        print()
        print("--- Hitung Deret Aritmatika (while) ---")
        try:
            awal = int(input("Nilai awal: "))
            beda = int(input("Beda: "))
            n = int(input("Jumlah suku (n): "))
            
            total = 0
            suku = awal
            i = 0
            while i < n:
                total += suku
                suku += beda
                i += 1
            
            print(f"Total deret aritmatika: {total}")
        except ValueError:
            print("Input harus angka bulat!")
        except Exception as e:
            print(f"Terjadi error: {e}")

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan masukkan opsi 1 sampai 5.")