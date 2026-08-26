# Tugas & Latihan Analisis Modul OOP Python — ✅ SELESAI

Dokumen ini berisi rangkuman seluruh tugas analisis dan tantangan proyek dari modul **Koding dan Kecerdasan Artificial (Rekayasa Perangkat Lunak) - Pemrograman Berorientasi Objek pada Python**.

> Semua praktikum sudah dikerjakan dengan code sesimple mungkin. Jalankan: `python praktikum/latihan1.py` s/d `python praktikum/myedotel.py`

---

## 1. Tugas Analisis 1 (Latihan 1: Membuat Class Hero)

**Instruksi:**
- Apa yang terjadi jika kamu mengubah `hero1.hp` menjadi `500` setelah baris `hero1 = Hero(...)`?
- Coba lakukan `print(hero1.hp)`.

**Jawaban & Bukti (`praktikum/latihan1.py`):**
```python
hero1.hp = 500
print(hero1.hp) # 500
```
HP berubah jadi 500 karena `hp` masih public tanpa validasi. Rawan cheat. Solusi: pakai Enkapsulasi `__hp` + setter di latihan 4.

**Output:**
```
Hero: Layla | HP: 500 | Power: 15
```

---

## 2. Tugas Analisis 2 (Latihan 2: Interaksi Antar Objek)

**Pertanyaan:** Perhatikan parameter `lawan` pada method `serang(self, lawan)`. Parameter tersebut menerima sebuah objek utuh, bukan hanya *string* nama. **Mengapa ini penting?**

**Jawaban (`praktikum/latihan2.py`):**
Karena dengan objek kita bisa akses SEMUA data & method lawan: `lawan.name`, `lawan.hp`, `lawan.diserang()`. Kalau cuma string, kita tidak bisa kurangi HP lawan.
```python
def serang(self, lawan):
    print(f"{self.name} menyerang {lawan.name}!")
    lawan.diserang(self.attack_power) # butuh objek!
```

---

## 3. Tugas Analisis 3 (Latihan 3: Pewarisan / Inheritance)

**Eksperimen `super()`:**
1. Hapus baris `super().__init__(name, hp, attack_power)` di `Mage`.
2. Jalankan `eudora.info()`.

**Jawaban (`praktikum/latihan3.py`):**
- **Error:** `AttributeError: 'Mage' object has no attribute 'name'`
- **Mengapa?** Walau kita kirim `"Eudora"` ke `Mage()`, data tidak sampai ke Parent `Hero` karena `super().__init__()` tidak dipanggil. Jadi `self.name` tidak pernah dibuat.
- **Peran `super()`:** Menghubungkan Child ke Parent — memanggil constructor Parent agar Child mewarisi `name`, `hp`, `attack_power` tanpa tulis ulang.

---

## 4. Tugas Analisis 4 (Latihan 4: Enkapsulasi)

### 1. Percobaan Hacking
```python
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
```
**Jawaban:** Nilai HP **muncul**, tidak Error. Python cuma melakukan *Name Mangling* (`__hp` -> `_Hero__hp`). Tetap **tidak boleh** dipakai karena melanggar enkapsulasi dan standar clean code.

### 2. Uji Validasi
Hapus `if/elif` di `set_hp` jadi `self.__hp = nilai_baru` lalu `hero1.set_hp(-100)`.
**Jawaban:** HP jadi `-100` (tidak masuk akal, hero mati minus). **Setter penting** untuk validasi: cegah HP negatif/cheat 9999, jaga integritas data game. (`praktikum/latihan4.py`)

---

## 5. Tugas Analisis 5 (Latihan 5: Abstraction & Interface)

### 1. Melanggar Kontrak
Hapus `def serang(self, target):` di `Hero`.
**Jawaban:**
- **Error:** `Can't instantiate abstract class Hero with abstract method serang`
- **Artinya:** `Hero` janji punya `serang` karena ikut kontrak `GameUnit`, tapi tidak ditepati → tidak boleh dibuat objek.
- **Konsekuensi:** Semua child wajib implementasi method abstract, kalau lupa program error.

### 2. Mencetak Cetakan
`unit = GameUnit()`
**Jawaban:**
- **Mengapa dilarang?** `GameUnit` abstract — hanya cetakan, belum lengkap.
- **Gunanya?** Sebagai kontrak/interface agar `Hero` & `Monster` dipaksa punya method yang sama (`serang`, `info`) → konsisten.

(`praktikum/latihan5.py`)

---

## 6. Tugas Analisis 6 (Latihan 6: Polymorphism)

### 1. Uji Skalabilitas
Buat `Healer(Hero)` tanpa ubah loop `for pahlawan in pasukan:`.
**Jawaban:** Program **lancar**. Keuntungan polymorphism: tambah karakter baru tinggal buat class baru, tidak perlu ubah kode lama (loop lama tetap jalan).
```python
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")
```

### 2. Konsistensi Penamaan
Ubah `serang` di `Archer` jadi `tembak_panah`.
**Jawaban:** Yang terpanggil jadi `Hero.serang()` (tangan kosong) atau error. **Nama harus sama persis** agar polymorphism bisa panggil method yang tepat via loop yang sama.

(`praktikum/latihan6.py`)

---

## 7. Tugas Proyek Integrasi (Challenge): Sistem Manajemen Kamar Hotel "MyEdotel" — ✅ SELESAI

**File:** `praktikum/myedotel.py` (91 baris, sesimple mungkin)

### Ketentuan Terpenuhi:
1. **Abstraction:** `KamarHotel(ABC)` + `@abstractmethod tampilkan_detail()` & `hitung_harga_total()`
2. **Encapsulation:** `__stok` & `__harga` private + `get_stok()`, `get_harga()`, `tambah_stok()` validasi negatif
3. **Inheritance:** `KamarDeluxe` (fasilitas, pajak 10%) & `KamarStandard` (kapasitas, pajak 5%) mewarisi `KamarHotel`
4. **Polymorphism:** Override method sama tapi isi beda + `proses_transaksi(daftar_pesanan)` polymorphism

### Cara Jalankan:
```bash
python praktikum/myedotel.py
```

### Output (Sesuai Target 100%):
```text
SETUP DATA KAMAR
Berhasil menambahkan stok Kamar Deluxe Sea View: 10 unit.
Gagal update stok Kamar Standard Superior! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok Kamar Standard Superior: 20 unit.

STRUK PEMESANAN
1. [DELUXE] Kamar Deluxe Sea View | Fasilitas: Private Pool
  Harga/Malam: Rp 1.500.000 | Pajak (10%): Rp 150.000
   Menginap: 2 malam | Subtotal: Rp 3.300.000
2. [STANDARD] Kamar Standard Superior | Kapasitas: 2 Orang
  Harga/Malam: Rp 500.000 | Pajak (5%): Rp 25.000
   Menginap: 1 malam | Subtotal: Rp 525.000

TOTAL TAGIHAN: Rp 3.825.000
```

### Rubrik Nilai:
| Kriteria | Poin | Status |
| :--- | :---: | :--- |
| Keamanan (Encapsulation) | 25 | ✅ `__stok` private & tervalidasi |
| Struktur (Abstraction) | 25 | ✅ pakai `abc`, `KamarHotel` tidak bisa di-init |
| Logika (Polymorphism) | 25 | ✅ pajak 10% vs 5% beda method sama |
| Fungsionalitas | 25 | ✅ output sesuai skenario |
