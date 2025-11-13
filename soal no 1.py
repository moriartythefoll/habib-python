# =========================================
# CLASS KAMAR (DETAIL KAMAR)
# =========================================
class Kamar:
    def __init__(self, nomor, tipe, harga):
        self.nomor = nomor
        self.tipe = tipe
        self.harga = harga
        self.status = "Kosong"

    def tampilkan_detail(self):
        print(f"Kamar {self.nomor} | Tipe: {self.tipe} | Harga: Rp{self.harga} | Status: {self.status}")


# =========================================
# CLASS PEMESANAN KAMAR
# =========================================
class PemesananKamar:
    def __init__(self, nama_tamu, kamar, lama_inap):
        self.nama_tamu = nama_tamu
        self.kamar = kamar
        self.lama_inap = lama_inap
        self.total_harga = self.hitung_total()
        self.status = "Belum Bayar"
        kamar.status = "Dipesan"

    def hitung_total(self):
        return self.kamar.harga * self.lama_inap

    def tampilkan_pemesanan(self):
        print("\n=== DATA PEMESANAN ===")
        print(f"Nama Tamu   : {self.nama_tamu}")
        print(f"Kamar       : {self.kamar.nomor} ({self.kamar.tipe})")
        print(f"Lama Inap   : {self.lama_inap} malam")
        print(f"Total Harga : Rp{self.total_harga}")
        print(f"Status      : {self.status}")


# =========================================
# CLASS PEMBAYARAN KAMAR
# =========================================
class PembayaranKamar:
    def __init__(self, pemesanan, metode):
        self.pemesanan = pemesanan
        self.metode = metode

    def proses_pembayaran(self):
        print("\n=== PEMBAYARAN ===")
        print(f"Metode Pembayaran : {self.metode}")
        print(f"Total Dibayar     : Rp{self.pemesanan.total_harga}")
        self.pemesanan.status = "Lunas"
        print("Status Pemesanan  : Lunas")


# =========================================
# PROGRAM UTAMA (OTOMATIS)
# =========================================
print("=== SISTEM RESERVASI HOTEL ===")

# 1️⃣ DETAIL KAMAR
kamar1 = Kamar(101, "Standard", 300000)
kamar2 = Kamar(102, "Deluxe", 500000)
kamar3 = Kamar(103, "Suite", 800000)

print("\nDaftar Kamar:")
kamar1.tampilkan_detail()
kamar2.tampilkan_detail()
kamar3.tampilkan_detail()

# 2️⃣ PEMESANAN OTOMATIS
pemesanan = PemesananKamar("Budi", kamar2, 3)
pemesanan.tampilkan_pemesanan()

# 3️⃣ PEMBAYARAN OTOMATIS
pembayaran = PembayaranKamar(pemesanan, "Transfer Bank")
pembayaran.proses_pembayaran()

# 4️⃣ DETAIL KAMAR SETELAH DIBAYAR
print("\n=== DETAIL AKHIR KAMAR ===")
kamar2.tampilkan_detail()
