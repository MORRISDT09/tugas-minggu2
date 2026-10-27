import operasi3

while True:
    print("\n" + "=" * 45)
    print("APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. operasi aritmatika dasar (+,-,*,/)")
    print("2. cek sifat bilangan (ganjil/genap)")
    print("3. hitung deret aritmatika (for & akumulator)")
    print("4. cetak tabel perkalian matriks (nested loop)")
    print("5. keluar")
    print("=" * 45)

    pilihan = input("pilih menu(1-5): ")

    if pilihan == "5":
        print("\nTerimakasih telah menggunakan kalkulator konsol. Program selesai.")
        break

    # Menu 1
    elif pilihan == "1":
        print("\n--- sub-menu operasi dasar ---")
        print("a. penjumlahan(+)")
        print("b. pengurangan (-)")
        print("c. perkalian(*)")
        print("d. pembagian(/)")

        op = input("pilih operasi(A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("memasukkan angka pertama: ")
            inp2 = input("memasukkan angka kedua: ")

            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if op == "A":
                    hasil = operasi3.tambah(a, b)
                    print(f"hasil {a} + {b} = {hasil}")
                elif op == "B":
                    hasil = operasi3.kurang(a, b)
                    print(f"hasil {a} - {b} = {hasil}")
                elif op == "C":
                    hasil = operasi3.kali(a, b)
                    print(f"hasil {a} * {b} = {hasil}")
                elif op == "D":
                    hasil = operasi3.bagi(a, b)
                    print(f"hasil {a} / {b} = {hasil}")
            else:
                print("peringatan: masukkan wajib berupa bilangan bulat!")
        else:
            print("peringatan: pilihan operasi tidak valid")

    # Menu 2
    elif pilihan == "2":
        print("\n--- Cek Ganjil / Genap (Modulus %) ---")
        inp_angka = input("Masukkan angka bulat positif: ")
        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"Hasil: Angka {angka} tergolong bilangan {status}")
        else:
            print("Peringatan: Masukan harus berupa angka murni!")

    # Menu 3
    elif pilihan == "3":
        print("\n--- Hitung Deret Aritmatika ---")
        inp_a = input("Suku Pertama (a): ")
        inp_b = input("Beda Deret (b): ")
        inp_n = input("Banyak Suku (n): ")
        
        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit(): 
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("Peringatan: Banyak suku (n) harus lebih dari 0!")
                n = int(input("Masukkan ulang banyak suku (n): "))
            
            total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
            print(f"Total Jumlah Seluruh Deret = {total_deret}")
        else:
            print("Peringatan: Seluruh masukan wajib berupa angka bulat!")

    # Menu 4
    elif pilihan == "4":
        print("\n--- Matriks Tabel Perkalian 1 (Nested Loop) ---")
        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end="")
            print()

    else:
        print("pilihan tidak valid! silahkan masukkan opsi 1 sampai 5")