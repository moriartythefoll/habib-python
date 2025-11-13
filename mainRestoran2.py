from classrestoran2 import Restoran, Meja, Reservasi, Pelanggan

resto = Restoran("Restoran Sederhana")

# Tambah meja
resto.tambahMeja(Meja(1, 2))
resto.tambahMeja(Meja(2, 4))
resto.tambahMeja(Meja(3, 6))

id_res = 1

while True:
    print("\n=== SISTEM RESERVASI RESTORAN ===")
    print("1. Lihat meja")
    print("2. Buat reservasi")
    print("3. Keluar")

    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        resto.tampilkanMeja()

    elif menu == "2":
        nama = input("Nama pelanggan: ")
         # VALIDASI INPUT JUMLAH ORANG
        while True:
            try:
                no = int(input("Nomor Hp: "))
                break
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka saja.\n")
        # no = input("Nomor HP: ")

        # VALIDASI INPUT JUMLAH ORANG
        while True:
            try:
                orang = int(input("Jumlah orang: "))
                break
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka saja.\n")
        # VALIDASI INPUT WAKTU
        while True:
            try:
                waktu =input("Waktu reservasi (misal 19:00) : ")
                break
            except ValueError:
                print("❌ Input tidak valid masukkan angka saja.\n")
        # waktu = input("Waktu reservasi (misal 19:00): ")

        pelanggan = Pelanggan(nama, no)
        meja_tersedia = resto.cariMejaTersedia(orang)

        if meja_tersedia:
            reservasi = Reservasi(id_res, meja_tersedia, pelanggan, waktu)
            reservasi.konfirmasi()
            resto.daftarReservasi.append(reservasi)
            id_res += 1

            print("\n✅ Reservasi Berhasil!")
            print(f"Meja: {meja_tersedia.nomorMeja}")
            print(f"Atas nama: {pelanggan.nama}")
            print(f"Waktu: {waktu}")
        else:
            print("\n❌ Tidak ada meja tersedia!")

    elif menu == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Menu tidak valid!")
