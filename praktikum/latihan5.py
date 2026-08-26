# Latihan 5: Abstraction & Interface - Sesimple mungkin
from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya Hero: {self.nama}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya Monster: {self.jenis}")

# --- Uji Coba ---
h = Hero("Alucard")
m = Monster("Serigala")
h.info()
m.info()
h.serang("Monster")
m.serang("Hero")

# --- Tugas Analisis 5.1: Melanggar Kontrak ---
# Jika method serang di Hero dihapus -> Error:
# Can't instantiate abstract class Hero with abstract method serang
# Artinya: Hero janji punya serang tapi tidak ditepati, jadi tidak boleh dibuat objek
# Konsekuensi: kontrak interface wajib dipenuhi semua child

# --- Tugas Analisis 5.2: Mencetak Cetakan ---
# unit = GameUnit() -> Error: tidak bisa buat objek dari abstract class
# Gunanya GameUnit: sebagai cetakan/kontrak agar semua Unit punya method yang sama
