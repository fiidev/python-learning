# Latihan 3: Pewarisan / Inheritance - Sesimple mungkin
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
        print(f"{self.name} terkena {damage} damage. Sisa HP: {self.hp}")

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)  # hubungkan ke Parent
        self.mana = mana

    def info(self):
        print(f"{self.name} (Mage) | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup!")

# --- Main Program ---
print("--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

# --- Tugas Analisis 3 ---
# Jika super().__init__ dihapus/komentar:
# Error: AttributeError: 'Mage' object has no attribute 'name'
# Mengapa? Karena tanpa super(), data name/hp/power tidak dikirim ke Parent
# Peran super(): memanggil constructor Parent agar Child punya attribute Parent
