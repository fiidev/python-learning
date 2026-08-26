# Latihan 4: Enkapsulasi - Sesimple mungkin
class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # private

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP max 1000")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"{self.nama} kena {damage} damage. Sisa HP: {self.get_hp()}")

# --- Uji Coba ---
hero1 = Hero("Layla", 100)
hero1.set_hp(-50)
print(hero1.get_hp())  # 0

print("\n--- Tugas Analisis 4.1: Hacking ---")
print(f"Mencoba akses paksa: {hero1._Hero__hp}")  # Muncul! karena Name Mangling
# Jawaban: Muncul, tidak error. Python cuma ubah nama jadi _Hero__hp (name mangling)
# Tetap tidak boleh dipakai karena melanggar enkapsulasi.

print("\n--- Tugas Analisis 4.2: Uji Validasi ---")
# Jika if/elif dihapus dan cuma self.__hp = nilai_baru
# Maka hero1.set_hp(-100) akan buat HP = -100 (tidak masuk akal)
# Setter penting untuk validasi agar data tidak rusak/cheat
hero1.set_hp(-100)
print(f"HP setelah set -100: {hero1.get_hp()} (dicegat jadi 0)")
