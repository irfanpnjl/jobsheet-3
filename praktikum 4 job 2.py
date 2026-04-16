# Kelas untuk menjelaskan atribut dan metode dalam kelas
class Mobil:
    def __init__(self, merk, warna, tahun, harga):
        # Atribut yang dimiliki oleh objek Mobil
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.harga = harga

    # Fungsi tanpa return value, hanya mencetak informasi
    def tampilkan_info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}, tahun {self.tahun}, harga: Rp {self.harga}")

    # Fungsi dengan satu parameter
    def diskon(self, persen_diskon):
        # Menghitung harga setelah diskon
        diskon_harga = self.harga * (persen_diskon / 100)
        harga_setelah_diskon = self.harga - diskon_harga
        print(f"Harga setelah diskon {persen_diskon}%: Rp {harga_setelah_diskon}")
        # Tidak mengembalikan nilai, hanya mencetak harga setelah diskon

    # Fungsi dengan return value, menghitung usia mobil berdasarkan tahun sekarang
    def hitung_usia(self, tahun_sekarang):
        usia = tahun_sekarang - self.tahun
        return usia

    # Fungsi dengan beberapa parameter
    def perbarui_harga(self, harga_baru, tahun_baru):
        self.harga = harga_baru
        self.tahun = tahun_baru
        print(f"Harga dan tahun mobil {self.merk} diperbarui menjadi Rp {self.harga} dan tahun {self.tahun}")

# Membuat objek mobil
mobil1 = Mobil("Toyota", "Hitam", 2015, 300000000)
mobil2 = Mobil("Honda", "Merah", 2018, 250000000)

# Menggunakan metode tanpa return value
mobil1.tampilkan_info()
mobil2.tampilkan_info()

# Menggunakan metode dengan satu parameter (diskon)
mobil1.diskon(10)
mobil2.diskon(15)

# Menggunakan metode dengan return value (hitung usia mobil)
usia_mobil1 = mobil1.hitung_usia(2025)
usia_mobil2 = mobil2.hitung_usia(2025)

print(f"Usia mobil1 pada tahun 2025: {usia_mobil1} tahun")
print(f"Usia mobil2 pada tahun 2025: {usia_mobil2} tahun")

# Menggunakan metode dengan beberapa parameter (perbarui harga dan tahun)
mobil1.perbarui_harga(280000000, 2022)
mobil2.perbarui_harga(240000000, 2021)