# Kontribusi

Terima kasih sudah mau berkontribusi ke repositori ini! 🎉

Repositori ini berisi materi dan latihan **Pemrograman Berorientasi Objek (OOP) pada Python** dari modul Koding dan Kecerdasan Artificial. Kontribusi kamu sangat membantu teman-teman yang sedang belajar.

## Jenis Kontribusi yang Diterima

- ✅ Solusi / pengerjaan latihan dan tugas analisis
- ✅ Perbaikan bug atau error pada kode
- ✅ Perbaikan materi, typo, atau dokumentasi
- ✅ Penambahan latihan/tugas baru yang relevan

## Alur Kontribusi

1. **Fork** repositori ini ke akun kamu.
2. **Clone** hasil fork ke komputer kamu.
3. Buat **branch baru** dengan nama yang deskriptif:
   ```bash
   git checkout -b feat/solusi-latihan3
   ```
   Konvensi prefix branch: `feat/` (fitur/solusi baru), `fix/` (perbaikan bug), `docs/` (dokumentasi).
4. Kerjakan perubahan kamu.
5. **Uji** file yang kamu ubah:
   ```bash
   python dasar.py
   python praktikum/latihan1.py
   ```
   Pastikan tidak ada error.
6. **Commit** dengan pesan yang jelas, ikuti konvensi repo:
   ```bash
   git add <file-yang-diubah>
   git commit -m "feat: solusi tugas analisis 3"
   ```
   Prefix commit: `feat:`, `fix:`, `docs:`, `init:`.
7. **Push** branch kamu:
   ```bash
   git push origin feat/solusi-latihan3
   ```
8. Buat **Pull Request** ke branch `main` — gunakan [template PR](.github/pull_request_template.md) yang sudah disediakan.

## Panduan Penulisan

- Gunakan **Bahasa Indonesia** untuk kode, komentar, dan dokumentasi.
- Jangan mengubah file di luar scope perubahan kamu.
- Jaga agar kode tetap sederhana dan mudah dipahami (repo ini untuk pembelajaran).
- Jika kamu menambahkan latihan baru, jelaskan instruksi dan pertanyaan analisisnya seperti format yang sudah ada di `README.md`.

## Melaporkan Masalah

- Temukan bug? Gunakan template [Laporan Bug](.github/ISSUE_TEMPLATE/bug_report.yml).
- Punya ide fitur? Gunakan template [Permintaan Fitur](.github/ISSUE_TEMPLATE/feature_request.yml).

## Struktur Repositori

```
├── dasar.py              # Latihan dasar class & objek
├── pilar-oop.py          # Latihan 4 pilar OOP (encapsulation, inheritance, dll)
├── praktikum/            # Latihan praktikum 1-6
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── ...
│   └── latihan6.py
└── README.md             # Rangkuman tugas & tantangan proyek
```

Selamat berkontribusi! 💪