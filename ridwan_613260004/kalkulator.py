# ======================================================================
# PROGRAM UTAMA: KALKULATOR KONSOL INTERAKTIF & MODUL
# ======================================================================

import operasi3 as mm  

while True:
    print("\n" + "~" * 50)
    print("      APLIKASI KALKULATOR KONSOL MULTIFUNGSI        ")
    print("~" * 50)
    print(" [1] Operasi Aritmatika Dasar (+, -, *, /)")
    print(" [2] Pengecekan Bilangan Ganjil / Genap")
    print(" [3] Hitung Deret Aritmatika ")
    print(" [4] Cetak Tabel Perkalian Matriks (Nested Loop)")
    print(" [5] Keluar dari Program")
    print("~" * 50)

    menu_pilih = input("Silakan masukkan pilihan Anda (1-5): ")

    # ===================
    # KELUAR PROGRAM
    # ===================
    if menu_pilih == "5":
        print("\nTerima kasih telah menjalankan program ini.")
        break

    # =========================================
    # MENU 1: ARITMATIKA DASAR
    # =========================================
    elif menu_pilih == "1":
        print("\n--- SUB-MENU: ARITMATIKA DASAR ---")
        print(" 1. Penjumlahan")
        print(" 2. Pengurangan")
        print(" 3. Perkalian")
        print(" 4. Pembagian")

        jenis_op = input("Tentukan jenis operasi (1-4): ")

        if jenis_op not in ["1", "2", "3", "4"]:
            print("[INFO] Pilihan operasi tidak terdaftar.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        try:
            x = float(input("Masukkan nilai pertama : "))
            y = float(input("Masukkan nilai kedua   : "))
        except ValueError:
            print("[PERINGATAN] Masukan wajib berupa angka!")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        if jenis_op == "1":
            hasil = mm.tambah(x, y)
            print(f"Hasil: {x:g} + {y:g} = {hasil:g}")

        elif jenis_op == "2":
            hasil = mm.kurang(x, y)
            print(f"Hasil: {x:g} - {y:g} = {hasil:g}")

        elif jenis_op == "3":
            hasil = mm.kali(x, y)
            print(f"Hasil: {x:g} * {y:g} = {hasil:g}")  

        elif jenis_op == "4":
            if y == 0:
                print("[PERINGATAN] Operasi pembagian dengan angka nol (0) dilarang.")
            else:
                hasil = mm.bagi(x, y)
                print(f"Hasil: {x:g} / {y:g} = {hasil:g}")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # =========================================
    # MENU 2: CEK GANJIL / GENAP
    # =========================================
    elif menu_pilih == "2":
        print("\n--- SUB-MENU: CEK GANJIL / GENAP ---")

        try:
            bilangan = int(input("Masukkan bilangan bulat positif: "))
        except ValueError:
            print("[PERINGATAN] Input harus berupa bilangan bulat.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        if bilangan <= 0:
            print("[PERINGATAN] Nilai harus lebih besar dari 0.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        keterangan = mm.cek_ganjil_genap(bilangan)
        print(f"Hasil Analisis: Angka {bilangan} merupakan bilangan {keterangan}.")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ========================================
    # MENU 3: DERET ARITMATIKA
    # ========================================
    elif menu_pilih == "3":
        print("\n--- SUB-MENU: DERET ARITMATIKA ---")

        try:
            suku_awal = int(input("Masukkan suku awal (a) : "))
            beda_deret = int(input("Masukkan beda deret (b): "))
        except ValueError:
            print("[PERINGATAN] Suku awal dan beda harus berupa bilangan bulat.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        while True:
            try:
                jumlah_suku = int(input("Jumlah suku (n)        : "))
            except ValueError:
                print("[PERINGATAN] Masukan harus berupa angka bulat.")
                continue

            if jumlah_suku <= 0:
                print("[PERINGATAN] Jumlah suku (n) minimal 1.")
                continue
            break

        total_deret = mm.hitung_deret_aritmatika(suku_awal, beda_deret, jumlah_suku)
        print(f"Total Akumulasi Deret  = {total_deret}")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ===============================================
    # MENU 4: TABEL PERKALIAN NESTED LOOP
    # ===============================================
    elif menu_pilih == "4":
        print("\n--- SUB-MENU: TABEL PERKALIAN (1 - 3) ---")
        print("      1    2    3")

        for r in range(1, 4):
            print(f"{r}   |", end="")
            for c in range(1, 4):
                print(f"{r * c:4}", end="")
            print()

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ========================================
    # MENU TIDAK VALID
    # ========================================
    else:
        print("[PERINGATAN] Menu tidak dikenali. Pilih angka 1 sampai 5.")
        input("\nTekan Enter untuk kembali ke menu utama...")