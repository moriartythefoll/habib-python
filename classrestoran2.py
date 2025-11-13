class Restoran:
    def __init__(self, namaRestoran):
        self.namaRestoran = namaRestoran
        self.daftarMeja = []
        self.daftarReservasi = []

    def tambahMeja(self, meja):
        self.daftarMeja.append(meja)

    def cariMejaTersedia(self, jumlah_orang):
        for meja in self.daftarMeja:
            if meja.status == "tersedia" and meja.kapasitas >= jumlah_orang:
                return meja
        return None

    def tampilkanMeja(self):
        print("\n=== Daftar Meja ===")
        for meja in self.daftarMeja:
            print(f"Meja {meja.nomorMeja} | Kapasitas: {meja.kapasitas} | Status: {meja.status}")
        print("====================")


class Meja:
    def __init__(self, nomorMeja, kapasitas):
        self.nomorMeja = nomorMeja
        self.kapasitas = kapasitas
        self.status = "tersedia"


class Reservasi:
    def __init__(self, idReservasi, meja, pelanggan, waktu):
        self.idReservasi = idReservasi
        self.meja = meja
        self.pelanggan = pelanggan
        self.waktu = waktu

    def konfirmasi(self):
        self.meja.status = "terisi"


class Pelanggan:
    def __init__(self, nama, nomorHP):
        self.nama = nama
        self.nomorHP = nomorHP

