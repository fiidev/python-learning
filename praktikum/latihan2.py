# Method menyerang: Objek ini (self) menyerang objek lain (lawan)
def serang(self, lawan):
    print(f"{self.name} menyerang {lawan.name}!")
    lawan.diserang(self.attack_power)

# Method diserang: Menerima damage
def diserang(self, damage):
    self.hp -= damage
    print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)  # Layla menyerang Zilong
hero2.serang(hero1)  # Zilong membalas