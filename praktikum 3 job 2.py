# Kelas Buku untuk merepresentasikan buku di perpustakaan
class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = "Tersedia"  # Status buku, default adalah Tersedia

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {self.status}")

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print(f"Buku '{self.judul}' telah dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def kembalikan(self):
        if self.status == "Dipinjam":
            self.status = "Tersedia"
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.")

# Membuat objek dari kelas Buku
buku1 = Buku("Pemrograman Python", "John Doe", 2021)
buku2 = Buku("Data Science untuk Pemula", "Jane Smith", 2020)

# Menggunakan metode objek Buku
buku1.tampilkan_info()
buku1.pinjam()

# Mengubah status buku dan menampilkan informasi
buku1.kembalikan()
buku1.pinjam()
buku1.tampilkan_info()

# Kelas Mahasiswa untuk merepresentasikan Mahasiswa dalam kelas
# Definisi kelas
class Mahasiswa:
    # Konstruktor (__init__) untuk menginisialisasi atribut objek
    def __init__(self, nama, nim, umur):
        self.nama = nama  # Atribut objek nama
        self.nim = nim    # Atribut objek nim
        self.umur = umur  # Atribut objek umur

    # Metode untuk menampilkan informasi mahasiswa
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur} tahun")

    # Metode untuk mengubah umur mahasiswa
    def ubah_umur(self, umur_baru):
        self.umur = umur_baru

# Membuat objek (instance) dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Andi", "12345", 20)
mahasiswa2 = Mahasiswa("Budi", "67890", 22)

# Menggunakan metode dari kelas Mahasiswa
mahasiswa1.tampilkan_info()
print()  # Baris kosong
mahasiswa2.tampilkan_info()

# Mengubah umur mahasiswa1 menggunakan metode ubah_umur
mahasiswa1.ubah_umur(21)

# Menampilkan info mahasiswa setelah umur diubah
print("\nSetelah mengubah umur mahasiswa1:")
mahasiswa1.tampilkan_info()