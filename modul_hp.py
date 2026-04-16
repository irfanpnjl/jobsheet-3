class Handphone:
    def __init__(self, merk, tipe, harga, stok):
        self.merk = merk
        self.tipe = tipe
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Merk  : {self.merk}")
        print(f"Tipe  : {self.tipe}")
        print(f"Harga : Rp {self.harga:,}")
        print(f"Stok  : {self.stok} unit")

    def jual(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            total = jumlah * self.harga
            print(f"[*] Berhasil menjual {jumlah} unit {self.merk} {self.tipe}.")
            print(f"    Total Pembayaran: Rp {total:,}")
        else:
            print(f"[!] Gagal: Stok {self.merk} {self.tipe} tidak mencukupi! (Sisa stok: {self.stok})")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"[+] Stok {self.merk} {self.tipe} berhasil ditambah {jumlah} unit. Total sekarang: {self.stok}")