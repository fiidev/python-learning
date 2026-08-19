# Parent Class
class Hewan:
    def makan(self):
        print("Hewan ini sedang makan.")

# Child Class (Mewarisi Hewan)
class Burung(Hewan):
    def terbang(self):
        print("Burung sedang terbang.")

# Object
beo = Burung()
beo.makan()    # Mewarisi dari Hewan (Output: Hewan ini sedang makan.)
beo.terbang()  # Method milik sendiri

class AkunBank:
    def __init__(self, saldo):
        self.__saldo = saldo  # Private attribute

    def cek_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

rekening = AkunBank(1000)
rekening.setor(500)
print(rekening.cek_saldo())    # Output: 1500
# print(rekening.__saldo)      # Ini akan Error! Tidak bisa akses langsung.

class Anjing:
    def suara(self):
        return "Guk Guk!"

class Kucing:
    def suara(self):
        return "Meow!"

# Fungsi umum
def tes_suara(hewan):
    print(hewan.suara())

hewan1 = Anjing()
hewan2 = Kucing()

tes_suara(hewan1)  # Output: Guk Guk!
tes_suara(hewan2)  # Output: Meow!

from abc import ABC, abstractmethod

class Kendaraan(ABC):  # Class Abstrak
    @abstractmethod
    def bergerak(self):
        pass

class Mobil(Kendaraan):
    def bergerak(self):
        print("Berjalan dengan roda")

class Kapal(Kendaraan):
    def bergerak(self):
        print("Berlayar di air")

# k = Kendaraan()  # Ini akan Error! Class abstrak tidak bisa di-instansiasi.
m = Mobil()
m.bergerak()

from abc import ABC, abstractmethod

# Ini bertindak sebagai Interface
class TombolInterface(ABC):
    @abstractmethod
    def tekan(self):
        pass

# Class ini WAJIB punya method tekan()
class TombolMerah(TombolInterface):
    def tekan(self):
        print("Sistem Dimatikan!")

class TombolHijau(TombolInterface):
    def tekan(self):
        print("Sistem Dinyalakan!")