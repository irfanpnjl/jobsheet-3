# Fungsi Built-in
# Fungsi print() adalah contoh fungsi built-in untuk mencetak output
print("Ini adalah contoh fungsi built-in")

# Fungsi len() adalah contoh fungsi built-in untuk menghitung panjang suatu objek
kata = "Pemrograman"
panjang_kata = len(kata)
print(f"Panjang kata '{kata}' adalah: {panjang_kata}")

# Fungsi max() adalah contoh fungsi built-in untuk mencari nilai maksimum dari sebuah daftar
angka = [10, 5, 30, 40, 25]
nilai_max = max(angka)
print(f"Nilai maksimum dalam daftar {angka} adalah: {nilai_max}")

# Fungsi User-Defined
# Fungsi dengan satu parameter (Menerima satu nilai input)
def cetak_kuadrat(angka):
    # Menghitung kuadrat dari angka yang diterima sebagai parameter
    print(f"Kuadrat dari {angka} adalah: {angka ** 2}")

# Fungsi dengan beberapa parameter (Menerima lebih dari satu nilai input)
def hitung_luas_persegi_panjang(panjang, lebar):
    # Menghitung luas persegi panjang
    return panjang * lebar

# Fungsi dengan beberapa tipe parameter (Menerima berbagai jenis data)
def info_mahasiswa(nama, umur, ipk):
    # Mencetak informasi mahasiswa
    print(f"Nama: {nama}, Umur: {umur}, IPK: {ipk}")

# Fungsi tanpa return value (Non-return value)
def sapa_pengguna(nama):
    # Fungsi ini hanya mencetak sapaan tanpa mengembalikan nilai
    print(f"Halo, {nama}! Selamat datang di dunia Python.")

# Fungsi dengan return value
def hitung_keliling_persegi(sisi):
    # Mengembalikan keliling persegi
    return 4 * sisi

# Pemanggilan fungsi dengan satu parameter
cetak_kuadrat(5)

# Pemanggilan fungsi dengan beberapa parameter
luas = hitung_luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang: {luas}")

# Pemanggilan fungsi dengan beberapa tipe parameter
info_mahasiswa("Budi", 22, 3.8)

# Pemanggilan fungsi tanpa return value
sapa_pengguna("Andi")

# Pemanggilan fungsi dengan return value
keliling = hitung_keliling_persegi(5)
print(f"Keliling persegi dengan sisi 5 adalah: {keliling}")
