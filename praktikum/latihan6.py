# Latihan 6: Polymorphism - Sesimple mungkin
class Hero:
    def __init__(self, nama):
        self.nama = nama
    def serang(self):
        print("Hero menyerang tangan kosong.")

class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) Bola Api! Boom!")

class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) Panah! Jleb!")

class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) Pedang! Slash!")

# Tugas 6.1: Class baru tanpa ubah looping
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

pasukan = [Mage("Eudora"), Archer("Miya"), Fighter("Zilong"), Mage("Gord"), Healer("Angela")]

print("--- PERANG DIMULAI ---")
for pahlawan in pasukan:
    pahlawan.serang()

# Jawaban 6.1: Program lancar! Keuntungan polymorphism = tambah karakter baru
# tidak perlu ubah looping lama, cukup buat class baru.

# Tugas 6.2: Jika Archer method diubah jadi tembak_panah
# Error: Archer tidak override serang, jadi pakai serang() milik Parent (tangan kosong)
# atau jika loop panggil tembak_panah akan error.
# Jawaban: Nama method harus SAMA agar polymorphism berjalan.
