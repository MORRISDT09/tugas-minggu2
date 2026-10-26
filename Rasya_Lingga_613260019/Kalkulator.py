#Aplikasi kalkulator Bemenu Interaktif

import operasi3 # Memanggil modul fungsi terpisah

while True:
    print("\n" + "="* 45)
    print("     APLIKASI KALKULATOR KONSOLE       ")
    print("="* 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (Ganjil/Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("="* 45)

    pilihan = input("Pilih menu (1-5): ")

    # Menu 5: KELUAR PROGRAM

    if pilihan == "5":
        print("\nTerima kasih telah menggunakan kalkulator konsol. program selesai!.")
        break

    # Menu 1: OPERASI ARITMATIKA DASAR
    
    # Aplikasi kalkulator menu interaktif

    import operasi3  # Memanggil modul fungsi terpisah

    while True:
        print("\n" + "=" * 45)
        print("     APLIKASI KALKULATOR KONSOLE       ")
        print("=" * 45)
        print("1. Operasi Aritmatika Dasar (+, -, *, /)")
        print("2. Cek Sifat Bilangan (Ganjil/Genap)")
        print("3. Hitung Deret Aritmatika (For & Akumulator)")
        print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
        print("5. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "5":
            print("\nTerima kasih telah menggunakan kalkulator konsol. Program selesai.")
            break

        elif pilihan == "1":
            print("\n--- Sub-Menu Operasi Dasar ---")
            print("A. Penjumlahan (+)")
            print("B. Pengurangan (-)")
            print("C. Perkalian (*)")
            print("D. Pembagian (/)")
            op = input("Pilih operasi (A/B/C/D): ").upper()

            if op not in ["A", "B", "C", "D"]:
                print("Peringatan: pilihan operasi tidak valid!")
                continue

            try:
                a = int(input("Masukan angka pertama: "))
                b = int(input("Masukan angka kedua: "))
            except ValueError:
                print("Peringatan: masukan wajib berupa bilangan bulat!")
                continue

            if op == "A":
                hasil = operasi3.tambah(a, b)
                print(f"Hasil Penjumlahan {a} + {b} = {hasil}")
            elif op == "B":
                hasil = operasi3.kurang(a, b)
                print(f"Hasil Pengurangan {a} - {b} = {hasil}")
            elif op == "C":
                hasil = operasi3.kali(a, b)
                print(f"Hasil Perkalian {a} * {b} = {hasil}")
            elif op == "D":
                if b == 0:
                    print("Peringatan: tidak dapat membagi dengan nol!")
                else:
                    hasil = operasi3.bagi(a, b)
                    print(f"Hasil Pembagian {a} / {b} = {hasil}")

        elif pilihan == "2":
            try:
                bilangan = int(input("Masukan bilangan bulat: "))
            except ValueError:
                print("Peringatan: masukan wajib berupa bilangan bulat!")
            else:
                sifat = "Genap" if bilangan % 2 == 0 else "Ganjil"
                print(f"Bilangan {bilangan} adalah {sifat}.")

        elif pilihan == "3":
            print("\n--- Hitung Deret Aritmatika ---")
            try:
                a = int(input("Suku Pertama (a): "))
                b = int(input("Beda (b): "))
                n = int(input("Jumlah Suku (n): "))
                while n <= 0:
                    print("Peringatan: banyak suku (n) harus lebih dari 0!")
                    n = int(input("Masukan ulang banyak suku (n): "))
            except ValueError:
                print("Peringatan: seluruh masukan wajib berupa bilangan bulat!")
            else:
                total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
                print(f"Total jumlah seluruh deret = {total_deret}")

        elif pilihan == "4":
            print("\n--- Tabel Perkalian 1 - 3 (Nested Loop) ---")
            for baris in range(1, 4):
                for kolom in range(1, 4):
                    print(f"{baris} x {kolom} = {baris * kolom}", end="  ")
                print()

        else:
            print("Pilihan tidak valid! Silahkan pilih menu 1-5.")
