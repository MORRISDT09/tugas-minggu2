import operasi03

while True:
    print("\n" + "="*45)
    print("APLIKASI KALKULATOR KONSOL ")
    print("="*45)
    print("1. Operasi Tersedia: + - * /")
    print("2. Cek Sifat Bilangan (Ganjil/Genap)")
    print("3. Hitung Deret Aritmatika (for & Akumulator)")
    print("4. Cek Tabel Perkalian (Nested Loop)")
    print("5. Keluar")
    print("="*45)

    pilihan = input("Masukkan pilihan (1-5): ")


    if pilihan == "5":
        print("\nTerimakasih telah menggunakan kalkulator ini.")
        break
    elif pilihan == "1":
        print("\n-----Sub-Menu-Operasi Dasar-----")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        operasi = input("Pilih operasi (A/B/C/D): ").upper()

        if operasi in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan angka pertama: ")
            inp2 = input("Masukkan angka kedua: ")

            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if operasi == "A":
                    hasil = operasi03.tambah(a, b)
                    print(f"Hasil: {a} + {b} = {hasil}")
                elif operasi == "B":
                    hasil = operasi03.kurang(a, b)
                    print(f"Hasil: {a} - {b} = {hasil}")
                elif operasi == "C":
                    hasil = operasi03.kali(a, b)
                    print(f"Hasil: {a} * {b} = {hasil}")
                elif operasi == "D":
                    hasil = operasi03.bagi(a, b)
                    print(f"Hasil: {a} / {b} = {hasil}")
            else:
                print("Peringatan: Masukan wajib berupa bilangan bulat!")
        else:
            print("Peringatan: Pilihan operasi tidak valid!")

    elif pilihan == "2":
        print("\n-----cek ganjil / genap (modulus %)-----")
        inp_angka = input("Masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi03.cek_ganjil_genap(angka)
            print(f"Angka {angka} tergolong bilangan {status}")
        else:
            print("Peringatan: Masukan harus berupa angka murni!")

    elif pilihan == "3":
        print("\n-----Hitung Deret Aritmatika-----")
        inp_awal = input("Suku Pertama (a): ")
        inp_beda = input("Beda Deret (b): ")
        inp_n = input("Banyak Suku (n): ")

        if inp_awal.isdigit() and inp_beda.isdigit() and inp_n.isdigit():
            awal = int(inp_awal)
            beda = int(inp_beda)
            n = int(inp_n)

            while n <= 0:
                print("Peringatan: Banyak suku (n) harus lebih dari 0!")
                inp_n = input("Silakan masukkan ulang Banyak Suku (n): ")

            total_deret = operasi03.hitung_deret_aritmatika(awal, beda, n)
            print(f"Total Jumlah Seluruh Deret = {total_deret}")
        else:
            print("Peringatan: Masukan harus berupa angka murni!")

    elif pilihan == "4":
        print("\n-----Matriks Tabel Perkalian 1-3 (Nested Loop)-----")
        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end=" ")
            print()

    else:
        print("Peringatan: Pilihan menu tidak valid!")