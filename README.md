# 🇮🇩 Paket Bahasa Indonesia untuk Visual Studio Code (Modern)

> **Membuka akses pemrograman bagi seluruh pengembang Indonesia dengan antarmuka yang ramah, intuitif, dan terkini.**

[![CI Validation](https://github.com/nusantara-dev/vscode-language-pack-id/actions/workflows/ci.yml/badge.svg)](https://github.com/nusantara-dev/vscode-language-pack-id/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 💡 Latar Belakang & Masalah

Visual Studio Code adalah editor kode paling populer di dunia. Namun bagi pelajar pemula, siswa SMK, mahasiswa, maupun programmer yang baru memulai, antarmuka berbahasa Inggris seringkali menjadi tembok penghalang pertama.

Ekstensi Bahasa Indonesia resmi Microsoft sebelumnya (`MS-CEINTL.vscode-language-pack-id`) telah **dihentikan pengembangannya sejak tahun 2020** dan dipindahkan ke `vscode-loc-deprecated`. Akibatnya:
* Terdapat **lebih dari 18.000+ teks antarmuka baru** di VS Code modern yang tidak memiliki terjemahan sama sekali.
* Menu-menu baru, palet perintah, panel kontrol versi (*Git*), dan pengaturan editor tercampur aduk antara bahasa Indonesia dan Inggris.
* Banyak pemula kebingungan memahami fungsi-fungsi penting editor.

Proyek ini dibangun untuk **menghidupkan kembali, memodernisasi, dan memelihara** Paket Bahasa Indonesia untuk Visual Studio Code secara berkelanjutan dengan bantuan otomasi dan komunitas open source Indonesia.

---

## ⚡ Coba Langsung di VS Code Anda (Uji Coba Lokal 1 Menit)

Anda tidak perlu menunggu ekstensi ini rilis di Marketplace untuk mencobanya di komputer Anda!

### 1. Tautkan ekstensi ke instalasi VS Code lokal
Jalankan perintah berikut di terminal:
```bash
python3 scripts/install_local.py
```

### 2. Aktifkan Bahasa Indonesia di VS Code
1. Buka (atau muat ulang) aplikasi **Visual Studio Code**.
2. Tekan pintasan keyboard:
   * **macOS**: `Cmd + Shift + P`
   * **Windows / Linux**: `Ctrl + Shift + P`
3. Ketik perintah: **`Configure Display Language`** lalu tekan `Enter`.
4. Pilih opsi **`Bahasa Indonesia`**.
5. Klik tombol **Restart** saat diminta.
6. 🎉 **Selesai!** Seluruh antarmuka VS Code Anda kini tampil dalam Bahasa Indonesia.

---

## 📂 Struktur Repositori

```text
├── package.json              # Konfigurasi manifes Language Pack
├── GLOSSARY.md               # Pedoman baku istilah teknis pemrograman Indonesia
├── icon.png                  # Ikon resmi paket bahasa (128x128)
├── translations/
│   ├── main.i18n.json        # Terjemahan inti VS Code (Menu, Penjelajah, Pengaturan)
│   └── extensions/           # Terjemahan modul ekstensi bawaan (Git, Terminal, Debug, dll)
├── scripts/
│   ├── install_local.py      # Script penaut lokal (~/.vscode/extensions)
│   ├── validate.py           # Validasi integritas JSON & placeholder ({0}, {1})
│   ├── sync_upstream.py      # Sinkronisasi & deteksi teks baru dari rilis VS Code global
│   └── translate_ai.py       # Penerjemahan otomatis batch dengan AI (Gemini API)
└── .github/workflows/        # Automasi CI / CD GitHub Actions
```

---

## 🛠️ Cara Kerja Otomasi & Alur Pengembangan

### 1. Memeriksa String Terbaru dari Upstream
Untuk memeriksa teks baru apa saja yang ditambahkan pada rilis VS Code terbaru dan menghitung persentase terjemahan:
```bash
python3 scripts/sync_upstream.py
```
*Script ini akan membandingkan data lokal dengan upstream resmi Microsoft, menampilkan tingkat kelengkapan terjemahan, dan mengekspor teks yang belum diterjemahkan ke `translations/missing_translations.json`.*

### 2. Menerjemahkan Batch Otomatis Menggunakan AI
Ekstensi ini dilengkapi dengan script penerjemah otomatis cerdas yang memahami istilah *software engineering*:
```bash
export GEMINI_API_KEY="kunci-api-gemini-anda"
python3 scripts/translate_ai.py --limit-modules 5
```

### 3. Validasi Integritas File
Pastikan semua file JSON valid dan tidak ada placeholder yang rusak:
```bash
python3 scripts/validate.py
```

---

## 📖 Pedoman Terjemahan (*Glossary*)

Kami berpegang teguh pada prinsip bahwa **antarmuka harus mudah dipahami pemula tanpa menghilangkan istilah teknis universal**:

| Istilah Asli | Terjemahan | Keterangan |
| :--- | :--- | :--- |
| **File / Folder** | Berkas / Folder | Sesuai kelaziman & KBBI |
| **Save / Save As** | Simpan / Simpan Sebagai... | Sederhana & jelas |
| **Explorer** | Penjelajah | Panel berkas di sisi kiri |
| **Source Control** | Kontrol Versi | Panel Git |
| **Command Palette** | Palet Perintah | Pintasan `Ctrl+Shift+P` |
| **Terminal** | Terminal | Dipertahankan (bukan 'stasiun') |
| **Debug** | Debug | Dipertahankan (istilah baku pemrograman) |
| **Git Commit / Push** | Komit (*Commit*) / Dorong (*Push*) | Dipertahankan istilah Git aslinya |

Baca panduan lengkapnya di [GLOSSARY.md](GLOSSARY.md).

---

## 🚀 Memublikasikan ke Marketplace

Jika Anda ingin memaketkan dan merilis ekstensi ini ke Visual Studio Marketplace atau Open VSX:

1. Pasang alat pemaket resmi Microsoft:
   ```bash
   npm install -g @vscode/vsce
   ```
2. Buat paket biner `.vsix`:
   ```bash
   vsce package
   ```
3. Terbitkan langsung ke Visual Studio Marketplace:
   ```bash
   vsce publish
   ```

---

## 🤝 Berkontribusi

Kontribusi dari seluruh pengembang di Indonesia sangat disambut hangat!
1. Lakukan *Fork* repositori ini.
2. Buat *branch* fitur Anda (`git checkout -b fitur/terjemahan-terminal`).
3. Lakukan terjemahan dengan mematuhi [GLOSSARY.md](GLOSSARY.md).
4. Jalankan `python3 scripts/validate.py` untuk memastikan tidak ada kesalahan format.
5. Buat *Pull Request* baru!

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
Ikon globe merupakan aset milik Visual Studio Code / Microsoft Corporation.
