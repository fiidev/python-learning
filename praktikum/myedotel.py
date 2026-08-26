# Challenge: MyEdotel - Sistem Manajemen Kamar Hotel - Sesimple mungkin
from abc import ABC, abstractmethod

def rupiah(n):
    return f"Rp {n:,}".replace(",", ".")

class KamarHotel(ABC):
    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.__harga = harga
        # stok private, set diam-diam tanpa print (biar output sesuai contoh)
        self.__stok = stok if stok >= 0 else 0

    def get_stok(self):
        return self.__stok

    def get_harga(self):
        return self.__harga

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        self.__stok += jumlah
        print(f"Berhasil menambahkan stok {self.nama}: {self.get_stok()} unit.")
        return True

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, malam):
        pass

class KamarDeluxe(KamarHotel):
    def __init__(self, nama, stok, harga, fasilitas):
        super().__init__(nama, stok, harga)
        self.fasilitas = fasilitas

    def tampilkan_detail(self):
        pajak = self.get_harga() * 10 // 100
        print(f"[DELUXE] {self.nama} | Fasilitas: {self.fasilitas}")
        print(f"  Harga/Malam: {rupiah(self.get_harga())} | Pajak (10%): {rupiah(pajak)}")

    def hitung_harga_total(self, malam):
        pajak = self.get_harga() * 10 // 100
        return (self.get_harga() + pajak) * malam

class KamarStandard(KamarHotel):
    def __init__(self, nama, stok, harga, kapasitas):
        super().__init__(nama, stok, harga)
        self.kapasitas = kapasitas

    def tampilkan_detail(self):
        pajak = self.get_harga() * 5 // 100
        print(f"[STANDARD] {self.nama} | Kapasitas: {self.kapasitas}")
        print(f"  Harga/Malam: {rupiah(self.get_harga())} | Pajak (5%): {rupiah(pajak)}")

    def hitung_harga_total(self, malam):
        pajak = self.get_harga() * 5 // 100
        return (self.get_harga() + pajak) * malam

# Polymorphism: proses transaksi campuran (polymorphism)
def proses_transaksi(daftar):
    total = 0
    print("\nSTRUK PEMESANAN")
    for i, (kamar, malam) in enumerate(daftar, 1):
        # print nomor + detail (polymorphism: tiap kamar tampil beda)
        print(f"{i}. ", end="")
        kamar.tampilkan_detail()
        subtotal = kamar.hitung_harga_total(malam)
        print(f"   Menginap: {malam} malam | Subtotal: {rupiah(subtotal)}")
        total += subtotal
    print(f"\nTOTAL TAGIHAN: {rupiah(total)}")
    return total

# --- Alur Program (User Story) ---
if __name__ == "__main__":
    print("SETUP DATA KAMAR")
    deluxe = KamarDeluxe("Kamar Deluxe Sea View", 0, 1500000, "Private Pool")
    standard = KamarStandard("Kamar Standard Superior", 0, 500000, "2 Orang")

    # Sesuai contoh output
    deluxe.tambah_stok(10)      # Berhasil 10
    standard.tambah_stok(-5)    # Gagal negatif
    standard.tambah_stok(20)    # Berhasil 20

    # Tamu pesan 2 malam Deluxe + 1 malam Standard
    pesanan = [(deluxe, 2), (standard, 1)]
    proses_transaksi(pesanan)
