# Latihan 2: Interaksi Antar Objek - Sesimple mungkin
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# --- Main Program ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

# --- Tugas Analisis 2 ---
# Mengapa parameter 'lawan' menerima objek utuh bukan string?
# Jawaban: Karena dengan objek kita bisa akses SEMUA data & method lawan
# (lawan.name, lawan.hp, lawan.diserang()) bukan cuma namanya.
# Kalau cuma string, kita tidak bisa kurangi HP lawan.
