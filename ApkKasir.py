python
class Kasir:
    def __init__(self):
        self.stok_barang = {'barang_A': 10, 'barang_B': 15, 'barang_C': 20}
        self.pesanan = {}

    def tampilkan_menu(self):
        print("Stok Barang:")
        for item, stok in self.stok_barang.items():
            print(f"{item}: {stok}")

    def proses_pesanan(self, item, jumlah):
        if item in self.stok_barang and self.stok_barang[item] >= jumlah:
            self.stok_barang[item] -= jumlah
            if item in self.pesanan:
                self.pesanan[item] += jumlah
            else:
                self.pesanan[item] = jumlah
            print(f"Pesanan {item} sebanyak {jumlah} berhasil ditambahkan.")
        else:
            print(f"Stok {item} tidak mencukupi.")

    def tampilkan_pesanan(self):
        print("Pesanan Saat Ini:")
        for item, jumlah in self.pesanan.items():
            print(f"{item}: {jumlah}")

    def hitung_total(self):
        total = 0
        for item, jumlah in self.pesanan.items():
            total += jumlah  # Anda bisa menambahkan logika harga barang di sini
        print(f"Total Pembelian: {total}")


# Contoh Penggunaan
kasir_saya = Kasir()
kasir_saya.tampilkan_menu()

kasir_saya.proses_pesanan('barang_A', 3)
kasir_saya.proses_pesanan('barang_B', 2)

kasir_saya.tampilkan_pesanan()
kasir_saya.hitung_total()