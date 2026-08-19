# Tugas & Latihan Analisis Modul OOP Python

Dokumen ini berisi rangkuman seluruh tugas analisis dan tantangan proyek dari modul **Koding dan Kecerdasan Artificial (Rekayasa Perangkat Lunak) - Pemrograman Berorientasi Objek pada Python**.

---

## 1. Tugas Analisis 1 (Latihan 1: Membuat Class Hero)

**Instruksi:**
- Apa yang terjadi jika kamu mengubah `hero1.hp` menjadi `500` setelah baris `hero1 = Hero(...)`?
- Coba lakukan `print(hero1.hp)`.

---

## 2. Tugas Analisis 2 (Latihan 2: Interaksi Antar Objek)

**Instruksi & Pertanyaan:**
- Perhatikan parameter `lawan` pada method `serang(self, lawan)`.
- Parameter tersebut menerima sebuah objek utuh, bukan hanya *string* nama. 
- **Mengapa ini penting?**

---

## 3. Tugas Analisis 3 (Latihan 3: Pewarisan / Inheritance)

**Eksperimen Fungsi `super()`:**
1. Pada class `Mage`, coba hapus (atau jadikan komentar `#`) baris kode `super().__init__(name, hp, attack_power)`.
2. Jalankan programnya.

**Pertanyaan:**
- Error apa yang muncul saat kamu mencoba melihat info Eudora (`eudora.info()`)?
- Mengapa error tersebut mengatakan `Mage object has no attribute 'name'`, padahal kita sudah mengirim nama `"Eudora"` saat pembuatan objek?
- Jelaskan peran fungsi `super()` dalam menghubungkan data dari class Anak (*Child Class*) ke class Induk (*Parent Class*)!

---

## 4. Tugas Analisis 4 (Latihan 4: Enkapsulasi)

### 1. Percobaan Hacking
- Coba tambahkan baris kode berikut di bagian paling bawah (luar class):
  ```python
  print(f"Mencoba akses paksa: {hero1._Hero__hp}")
  ```
- **Pertanyaan:** Apakah nilai HP muncul atau Error? Jika muncul, diskusikan mengapa Python masih mengizinkan akses ini (konsep *Name Mangling*) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik.

### 2. Uji Validasi
- Hapus logika `if` dan `elif` di dalam method `set_hp`, sehingga isinya hanya `self.__hp = nilai_baru`.
- Kemudian lakukan `hero1.set_hp(-100)`.
- **Pertanyaan:** Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method *Setter* sangat penting untuk menjaga integritas data dalam game!

---

## 5. Tugas Analisis 5 (Latihan 5: Abstraction & Interface)

### 1. Melanggar Kontrak
- Pada class `Hero`, hapus (atau jadikan komentar `#`) seluruh blok method:
  ```python
  def serang(self, target):
      ...
  ```
- Jalankan programnya.
- **Pertanyaan:** 
  - Error apa yang muncul?
  - Jelaskan dengan bahasamu sendiri arti pesan error `Can't instantiate abstract class Hero with abstract method...`!
  - Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?

### 2. Mencetak Cetakan
- Coba aktifkan baris kode `unit = GameUnit()`.
- **Pertanyaan:** 
  - Mengapa class `GameUnit` dilarang untuk dibuat menjadi objek?
  - Apa gunanya ada class `GameUnit` jika tidak bisa dibuat menjadi objek nyata?

---

## 6. Tugas Analisis 6 (Latihan 6: Polymorphism)

### 1. Uji Skalabilitas (Kemudahan Menambah Fitur)
- Tanpa mengubah satu huruf pun pada kode Looping (`for pahlawan in pasukan:`):
  1. Buat satu class baru bernama `Healer(Hero)`.
  2. Isi method `serang` milik `Healer` dengan:
     ```python
     print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")
     ```
  3. Masukkan objek `Healer` ke dalam list `pasukan`.
- **Pertanyaan:**
  - Apakah program berjalan lancar?
  - Apa keuntungan Polimorfisme bagi seorang programmer ketika harus meng-*update* game dengan karakter baru di masa depan?

### 2. Konsistensi Penamaan
- Ubah nama method `serang` pada class `Archer` menjadi `tembak_panah`.
- Jalankan program.
- **Pertanyaan:**
  - Apa yang terjadi?
  - Mengapa dalam konsep Polimorfisme nama method antara Parent Class dan berbagai Child Class harus persis sama?

---

## 7. Tugas Proyek Integrasi (Challenge): Sistem Manajemen Kamar Hotel "MyEdotel"

**Format Pengerjaan:** Berkelompok berpasangan sebangku.

### Skenario
MyEdotel adalah edukasi hotel (*edotel*) sekolah yang membutuhkan sistem backend sederhana untuk mengelola data kamar. Saat ini fokus pada **Kamar Deluxe** dan **Kamar Standard**.  
Data stok kamar dan harga sewa harus terlindungi (tidak bisa diubah sembarangan). Selain itu, setiap tipe kamar memiliki cara perhitungan pajak dan cara menampilkan fasilitas yang berbeda.

### Ketentuan Teknis (Rules)

1. **Abstraction (Kerangka Dasar):**
   - Buat Abstract Class `KamarHotel` (tidak boleh diinstansiasi langsung).
   - Memiliki Abstract Method:
     - `tampilkan_detail()`: Untuk menampilkan info kamar.
     - `hitung_harga_total(jumlah_malam)`: Untuk menghitung harga sewa + pajak.

2. **Encapsulation (Keamanan Data):**
   - Atribut sensitif diatur dalam parent class: nama kamar, stok, dan harga dasar.
   - Gunakan Private Attribute (`__`) untuk `stok` (jumlah kamar tersedia) dan `harga_dasar` (tarif per malam).
   - Buat Getter untuk melihat stok.
   - Buat Setter / method `tambah_stok(jumlah)` untuk mengubah stok dengan validasi: **stok tidak boleh negatif**.

3. **Inheritance (Pewarisan):**
   - Buat class anak `KamarDeluxe` dan `KamarStandard` yang mewarisi `KamarHotel`.
   - **`KamarDeluxe`**:
     - Atribut tambahan: `fasilitas` (contoh: `"Private Pool"`).
     - Pajak sewa: **10%** dari harga dasar.
   - **`KamarStandard`**:
     - Atribut tambahan: `kapasitas` (contoh: `"2 Orang"`).
     - Pajak sewa: **5%** dari harga dasar.

4. **Polymorphism (Fleksibilitas):**
   - Implementasikan (override) method `tampilkan_detail()` dan `hitung_harga_total(jumlah_malam)` dengan isi yang berbeda pada `KamarDeluxe` dan `KamarStandard`.
   - **Fitur Pemesanan:** Buat fungsi di luar class bernama `proses_transaksi(daftar_pesanan)`. Fungsi ini menerima list berisi campuran objek `KamarDeluxe` dan `KamarStandard`, lalu menjumlahkan total tagihan secara otomatis.

### Alur Program (User Story)
1. Admin membuat data kamar (1 Kamar Deluxe, 1 Kamar Standard).
2. Admin mencoba mengisi stok kamar dengan angka negatif (Program harus menolak/memberi peringatan).
3. Tamu memesan 2 malam Kamar Deluxe dan 1 malam Kamar Standard.
4. Program menampilkan detail kamar yang dipesan dan total tagihan akhir (termasuk pajak masing-masing).

### Contoh Target Output Program
```text
SETUP DATA KAMAR
Berhasil menambahkan stok Kamar Deluxe: 10 unit.
Gagal update stok Kamar Standard! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok Kamar Standard: 20 unit.

STRUK PEMESANAN
1. [DELUXE] Kamar Deluxe Sea View | Fasilitas: Private Pool
   Harga Dasar/Malam: Rp 1.500.000 | Pajak (10%): Rp 150.000
   Menginap: 2 malam | Subtotal: Rp 3.300.000
2. [STANDARD] Kamar Standard Superior | Kapasitas: 2 Orang
   Harga Dasar/Malam: Rp 500.000 | Pajak (5%): Rp 25.000
   Menginap: 1 malam | Subtotal: Rp 525.000

TOTAL TAGIHAN: Rp 3.825.000
```

### Rubrik Penilaian Proyek
| Kriteria | Poin | Detail |
| :--- | :---: | :--- |
| **Keamanan (Encapsulation)** | 25 | `stok` tidak bisa diakses langsung dan tervalidasi. |
| **Struktur (Abstraction)** | 25 | Menggunakan modul `abc` dan `KamarHotel` / Parent tidak bisa di-init. |
| **Logika (Polymorphism)** | 25 | Perhitungan pajak berbeda antara Kamar Deluxe & Kamar Standard meski methodnya sama. |
| **Fungsionalitas** | 25 | Program berjalan sesuai skenario output. |