class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat Private (hanya bisa diakses di dalam class ini)
        self.__hp = hp_awal

    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        # Kita pakai setter/getter bahkan di dalam class sendiri agar aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# --- Uji Coba
hero1 = Hero("Layla", 100)
# hero1.__hp = 9999      # GAGAL (Tidak akan mengubah hp asli)
# print(hero1.__hp)      # ERROR (Tidak bisa dibaca langsung)

hero1.set_hp(-50)         # Coba set negatif
print(hero1.get_hp())     # Output: 0 (Karena dicegat oleh logika Setter)