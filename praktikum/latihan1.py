# Latihan 1: Membuat Class Hero - Sesimple mungkin
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

# --- Main Program ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

print("--- Kondisi Awal ---")
hero1.info()
hero2.info()

# --- Tugas Analisis 1 ---
# Apa yang terjadi jika hero1.hp diubah jadi 500?
print("\n--- Tugas Analisis 1 ---")
hero1.hp = 500  # langsung ubah attribute (karena masih public)
print(hero1.hp)  # Output: 500
hero1.info()
# Jawaban: HP hero1 berubah jadi 500 karena attribute hp masih public/bisa diubah langsung.
# Tidak ada validasi, jadi cheat bisa terjadi.
