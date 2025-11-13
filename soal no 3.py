class RekeningBank:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.riwayat = []   # catat transaksi sederhana

    def setor(self, jumlah):
        self.saldo += jumlah
        self.riwayat.append(("SETOR", jumlah))

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup!")
        else:
            self.saldo -= jumlah
            self.riwayat.append(("TARIK", jumlah))

    def info(self):
        print("\n=== INFO REKENING ===")
        print("Pemilik:", self.pemilik)
        print("Saldo  :", self.saldo)
        print("Riwayat Transaksi:")
        if len(self.riwayat) == 0:
            print("- Belum ada transaksi")
        else:
            for jenis, jumlah in self.riwayat:
                print(f"- {jenis}: {jumlah}")
        print("======================\n")



# ==============================
# CLASS BARU (1) → Transaksi
# ==============================
class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah


# ==============================
# CLASS BARU (2) → Bank
# ==============================
class Bank:
    def __init__(self, nama):
        self.nama = nama
        self.rekening_list = []

    def tambahRekening(self, rekening):
        self.rekening_list.append(rekening)



# ==============================
# TEST PROGRAM (dari soal)
# ==============================
r1 = RekeningBank("Budi", 100000)
r1.info()
r1.setor(50000)
r1.info()
r1.tarik(200000)
r1.tarik(30000)
r1.info()
