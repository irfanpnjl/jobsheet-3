import modul_hp

def main():
    print("=== SISTEM PENJUALAN HP SEDERHANA ===\n")
    
    hp1 = modul_hp.Handphone("Xiaomi", "17 Pro Max", 20000000, 10)
    hp2 = modul_hp.Handphone("Google", "Pixel 10 Pro", 22000000, 5)

    print("--- Data HP Tersedia ---")
    hp1.tampilkan_info()
    print("-" * 20)
    hp2.tampilkan_info()
    
    print("\n--- Transaksi ---")
    hp1.jual(2)
    hp2.jual(6)
    
    print("\n--- Restock Barang ---")
    hp2.tambah_stok(5)
    hp2.jual(6)
    
    print("\n--- Update Data HP ---")
    hp1.tampilkan_info()
    print("-" * 20)
    hp2.tampilkan_info()

if __name__ == "__main__":
    main()