# Panduan Glosarium Istilah (Indonesian Language Pack for VS Code)

Dokumen ini adalah pedoman penerjemahan istilah antarmuka (*UI*) untuk memastikan konsistensi, kemudahan pemahaman bagi developer pemula, dan keselarasan dengan istilah teknis yang lazim di industri teknologi Indonesia.

---

## 🎯 Prinsip Utama Penerjemahan

1. **Ramah Pemula (*Beginner Friendly*)**: Jangan gunakan istilah kaku yang justru terdengar asing.
2. **Pertahankan Istilah Teknis Universal**: Istilah pemrograman dan alat yang sudah menjadi standar global (seperti *Git Commit, Push, Pull, Branch, Debug, Terminal, Runtime, Framework*) sebaiknya tetap dipertahankan atau disandingkan dengan padanannya.
3. **Patuhi Format Akses Pintasan (*Mnemonics*)**: Huruf dengan awalan `&` atau `&&` (contoh: `&Berkas` atau `Berkas (&B)`) adalah *shortcut* tombol `Alt` di sistem operasi.
4. **Jaga Parameter / Placeholder**: Parameter dinamis seperti `{0}`, `{1}`, atau `%s` **tidak boleh diubah posisinya atau dihilangkan**.

---

## 📖 Kamus Standar Istilah

| Bahasa Inggris | Bahasa Indonesia | Catatan & Konteks |
| :--- | :--- | :--- |
| **File** | Berkas | Menu navigasi berkas |
| **Folder / Directory** | Folder / Direktori | Sesuai konteks |
| **Open File / Open Folder** | Buka Berkas / Buka Folder | |
| **Save / Save As** | Simpan / Simpan Sebagai... | |
| **Save All** | Simpan Semua | |
| **Close / Close All** | Tutup / Tutup Semua | |
| **Edit** | Ubah / Edit | |
| **Undo / Redo** | Urungkan / Ulangi | |
| **Cut / Copy / Paste** | Potong / Salin / Tempel | |
| **Find / Replace** | Cari / Ganti | |
| **View** | Tampilan | Menu 'View' di baris atas |
| **Explorer** | Penjelajah | Panel kiri penjelajah berkas |
| **Search** | Pencarian | |
| **Source Control** | Kontrol Versi | Git / Version control UI |
| **Run and Debug** | Jalankan dan Debug | |
| **Extensions** | Ekstensi | Plugin / Add-on VS Code |
| **Settings** | Pengaturan | Konfigurasi editor |
| **Preferences** | Preferensi | |
| **Keyboard Shortcuts** | Pintasan Papan Ketik | |
| **Command Palette** | Palet Perintah | `Ctrl+Shift+P` / `Cmd+Shift+P` |
| **Terminal** | Terminal | Jangan diterjemahkan menjadi 'stasiun' |
| **Output** | Output / Keluaran | |
| **Problems** | Masalah | Tab *Problems* pendeteksi error/warning |
| **Breakpoint** | Titik Henti (*Breakpoint*) | Di debugger |
| **Workspace** | Ruang Kerja | |
| **Repository** | Repositori | |
| **Commit** | Komit (*Commit*) | Operasi Git |
| **Branch** | Cabang (*Branch*) | |
| **Merge** | Gabungkan (*Merge*) | |
| **Pull / Push** | Tarik (*Pull*) / Dorong (*Push*) | Sertakan istilah aslinya jika perlu |
| **Stash** | Simpan Sementara (*Stash*) | Git stash |
| **Diff / Changes** | Perbedaan / Perubahan | Perbandingan kode |
| **Install / Uninstall** | Pasang / Pasang Ulang / Copot | Pemasangan ekstensi |
| **Enable / Disable** | Aktifkan / Nonaktifkan | |
| **Reload Window** | Muat Ulang Jendela | Perintah restart UI editor |
| **Help** | Bantuan | |
| **About** | Tentang | Informasi versi VS Code |

---

## 🚫 Yang TIDAK Boleh Diterjemahkan

* **Sintaks Kode**: `const`, `function`, `class`, `import`, `export`, dll.
* **Perintah CLI / Flag**: `npm run build`, `--verbose`, `git clone`, dll.
* **Nama Bahasa Pemrograman & Format**: TypeScript, Python, HTML, JSON, YAML, CSS, dll.
* **Nama Protokol / Standar**: HTTP, SSH, FTP, API, URL, URI, dll.

