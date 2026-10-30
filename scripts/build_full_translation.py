#!/usr/bin/env python3
"""
Generator Lengkap Indonesian Language Pack untuk Visual Studio Code Modern & Antigravity.
Mengekstrak seluruh kunci & pesan dari instalasi resmi VS Code (nls.metadata.json),
memperbaiki seluruh mnemonik (&&), menerjemahkan menu utama, sesi, kustomisasi,
antarmuka AI/Copilot, serta ekstensi bawaan.
"""

import os
import sys
import json
import re

# 1. Kamus Frasa Bersih (Clean Exact Phrases) - Baik teks biasa maupun teks dengan &&
EXACT_PHRASES = {
    # Top Menus
    "File": "Berkas",
    "Edit": "Ubah",
    "Selection": "Pilihan",
    "View": "Tampilan",
    "Go": "Buka",
    "Run": "Jalankan",
    "Terminal": "Terminal",
    "Window": "Jendela",
    "Help": "Bantuan",
    "Code": "Code",

    # File Menu Actions
    "New Text File": "Berkas Teks Baru",
    "New File": "Berkas Baru",
    "New File...": "Berkas Baru...",
    "New Window": "Jendela Baru",
    "New Window with Profile": "Jendela Baru dengan Profil",
    "Open": "Buka",
    "Open...": "Buka...",
    "Open File": "Buka Berkas",
    "Open File...": "Buka Berkas...",
    "Open Folder": "Buka Folder",
    "Open Folder...": "Buka Folder...",
    "Open Workspace": "Buka Ruang Kerja",
    "Open Workspace...": "Buka Ruang Kerja...",
    "Open Workspace from File...": "Buka Ruang Kerja dari Berkas...",
    "Open Recent": "Buka Terkini",
    "More...": "Lainnya...",
    "Reopen Closed Editor": "Buka Kembali Editor yang Ditutup",
    "Clear Recently Opened": "Bersihkan Daftar Terkini",
    "Clear Recent": "Bersihkan Daftar Terkini",
    "Add Folder to Workspace...": "Tambahkan Folder ke Ruang Kerja...",
    "Save Workspace As...": "Simpan Ruang Kerja Sebagai...",
    "Duplicate Workspace": "Duplikasikan Ruang Kerja",
    "Duplicate Workspace in New Window": "Duplikasikan Ruang Kerja di Jendela Baru",
    "Save": "Simpan",
    "Save As...": "Simpan Sebagai...",
    "Save All": "Simpan Semua",
    "Save All in Group": "Simpan Semua dalam Grup",
    "Save All Files": "Simpan Semua Berkas",
    "Auto Save": "Simpan Otomatis",
    "Preferences": "Preferensi",
    "Settings": "Pengaturan",
    "Revert File": "Kembalikan Berkas",
    "Close Editor": "Tutup Editor",
    "Close All Editors": "Tutup Semua Editor",
    "Close Folder": "Tutup Folder",
    "Close Window": "Tutup Jendela",
    "Close Workspace": "Tutup Ruang Kerja",
    "Exit": "Keluar",
    "Share": "Bagikan",

    # Edit Menu Actions
    "Undo": "Urungkan",
    "Redo": "Ulangi",
    "Cut": "Potong",
    "Copy": "Salin",
    "Paste": "Tempel",
    "Find": "Cari",
    "Replace": "Ganti",
    "Find in Files": "Cari dalam Berkas",
    "Replace in Files": "Ganti dalam Berkas",
    "Toggle Line Comment": "Alihkan Komentar Baris",
    "Toggle Block Comment": "Alihkan Komentar Blok",
    "Emmet: Expand Abbreviation": "Emmet: Perluas Singkatan",

    # Selection Menu Actions
    "Select All": "Pilih Semua",
    "Expand Selection": "Perluas Pilihan",
    "Shrink Selection": "Ciutkan Pilihan",
    "Copy Line Up": "Salin Baris ke Atas",
    "Copy Line Down": "Salin Baris ke Bawah",
    "Move Line Up": "Pindahkan Baris ke Atas",
    "Move Line Down": "Pindahkan Baris ke Bawah",
    "Duplicate Selection": "Duplikasikan Pilihan",
    "Add Cursor Above": "Tambah Kursor di Atas",
    "Add Cursor Below": "Tambah Kursor di Bawah",
    "Add Cursors to Line Ends": "Tambah Kursor ke Akhir Baris",
    "Add Next Occurrence": "Tambah Kemunculan Berikutnya",
    "Add Previous Occurrence": "Tambah Kemunculan Sebelumnya",
    "Select All Occurrences": "Pilih Semua Kemunculan",

    # View Menu Actions
    "Command Palette...": "Palet Perintah...",
    "Open View...": "Buka Tampilan...",
    "Appearance": "Tampilan Editor",
    "Editor Layout": "Tata Letak Editor",
    "Explorer": "Penjelajah",
    "Search": "Pencarian",
    "Source Control": "Kontrol Versi",
    "Run and Debug": "Jalankan dan Debug",
    "Extensions": "Ekstensi",
    "Output": "Keluaran (Output)",
    "Debug Console": "Konsol Debug",
    "Problems": "Masalah",
    "Toggle Full Screen": "Alihkan Layar Penuh",
    "Toggle Zen Mode": "Alihkan Mode Zen",
    "Toggle Centered Layout": "Alihkan Tata Letak Rata Tengah",
    "Zoom In": "Perbesar",
    "Zoom Out": "Perkecil",
    "Reset Zoom": "Atur Ulang Perbesaran",
    "Toggle Word Wrap": "Alihkan Pembungkusan Kata",
    "Toggle Minimap": "Alihkan Minimap",
    "Toggle Breadcrumbs": "Alihkan Breadcrumbs",
    "Toggle Status Bar": "Alihkan Bilah Status",
    "Toggle Activity Bar": "Alihkan Bilah Aktivitas",
    "Toggle Primary Side Bar": "Alihkan Bilah Sisi Utama",
    "Toggle Secondary Side Bar": "Alihkan Bilah Sisi Sekunder",
    "Toggle Panel": "Alihkan Panel",

    # Go Menu Actions
    "Back": "Kembali",
    "Forward": "Maju",
    "Last Edit Location": "Lokasi Ubahan Terakhir",
    "Switch Editor": "Beralih Editor",
    "Next Editor": "Editor Berikutnya",
    "Previous Editor": "Editor Sebelumnya",
    "Go to File...": "Buka Berkas...",
    "Go to Symbol in Workspace...": "Buka Simbol di Ruang Kerja...",
    "Go to Symbol in Editor...": "Buka Simbol di Editor...",
    "Go to Line/Column...": "Buka Baris/Kolom...",
    "Go to Definition": "Buka Definisi",
    "Go to Declaration": "Buka Deklarasi",
    "Go to Type Definition": "Buka Definisi Tipe",
    "Go to Implementations": "Buka Implementasi",
    "Go to References": "Buka Referensi",
    "Go to Next Problem": "Buka Masalah Berikutnya",
    "Go to Previous Problem": "Buka Masalah Sebelumnya",

    # Run Menu Actions
    "Start Debugging": "Mulai Debugging",
    "Run Without Debugging": "Jalankan Tanpa Debugging",
    "Stop Debugging": "Hentikan Debugging",
    "Restart Debugging": "Mulai Ulang Debugging",
    "Open Configurations": "Buka Konfigurasi",
    "Add Configuration...": "Tambah Konfigurasi...",
    "Toggle Breakpoint": "Alihkan Titik Henti (Breakpoint)",
    "New Breakpoint": "Titik Henti Baru",
    "Enable All Breakpoints": "Aktifkan Semua Titik Henti",
    "Disable All Breakpoints": "Nonaktifkan Semua Titik Henti",
    "Remove All Breakpoints": "Hapus Semua Titik Henti",

    # Terminal Menu Actions
    "New Terminal": "Terminal Baru",
    "Split Terminal": "Bagi Terminal",
    "Run Task...": "Jalankan Tugas...",
    "Run Build Task...": "Jalankan Tugas Build...",
    "Run Active File": "Jalankan Berkas Aktif",
    "Run Selected Text": "Jalankan Teks Terpilih",

    # Help Menu Actions
    "Welcome": "Selamat Datang",
    "Show All Commands": "Tampilkan Semua Perintah",
    "Documentation": "Dokumentasi",
    "Editor Playground": "Taman Bermain Editor",
    "Show Release Notes": "Tampilkan Catatan Rilis",
    "Keyboard Shortcuts Reference": "Referensi Pintasan Papan Ketik",
    "Video Tutorials": "Tutorial Video",
    "Tips and Tricks": "Tip dan Trik",
    "Join Us on YouTube": "Bergabung di YouTube",
    "Search Feature Requests": "Cari Permintaan Fitur",
    "Report Issue": "Laporkan Masalah",
    "View License": "Lihat Lisensi",
    "Privacy Statement": "Pernyataan Privasi",
    "Toggle Developer Tools": "Alihkan Alat Pengembang",
    "Open Process Explorer": "Buka Penjelajah Proses",
    "Check for Updates...": "Periksa Pembaruan...",
    "About": "Tentang",

    # Antigravity & AI UI Panels
    "Sessions": "Sesi",
    "Session": "Sesi",
    "New Session": "Sesi Baru",
    "Automations": "Otomasi",
    "Automation": "Otomasi",
    "Create Automation": "Buat Otomasi",
    "New Automation": "Otomasi Baru",
    "Chats": "Obrolan",
    "Chat": "Obrolan",
    "Customizations": "Kustomisasi",
    "Overview": "Ringkasan",
    "Plugins": "Plugin",
    "Plugin": "Plugin",
    "Canvases": "Kanvas",
    "Canvas": "Kanvas",
    "MCP Servers": "Server MCP",
    "Skills": "Keahlian (Skills)",
    "Skill": "Keahlian (Skill)",
    "Instructions": "Instruksi",
    "Instruction": "Instruksi",
    "Agents": "Agen",
    "Agent": "Agen",
    "Hooks": "Kait (Hooks)",
    "Hook": "Kait (Hook)",
    "Tools": "Alat",
    "Tool": "Alat",
    "Changes": "Perubahan",
    "Files": "Berkas",
    "This Computer": "Komputer Ini",
    "Cabang (Branch)": "Cabang",
    "Branch": "Cabang",
    "Copilot": "Copilot",
    "Chat with Copilot": "Mengobrol dengan Copilot",
    "Time to lock in, {0}": "Waktunya fokus koding, {0}",
    "Time to lock in": "Waktunya fokus koding",
    "Pitch your idea": "Tulis ide atau tugas Anda...",
    "Review Migrations": "Tinjau Migrasi",
    "Review Plan": "Tinjau Rencana",
    "Interactive": "Interaktif",
    "Manual permissions": "Izin manual",
    "Auto": "Otomatis",
    "Standard": "Standar",
    "Full Access": "Akses Penuh",
    "Default Permissions": "Izin Bawaan",
    "Balance": "Seimbang",
    "Efficiency": "Efisiensi",
    "High": "Tinggi",
    "Low": "Rendah",
    "Medium": "Sedang",
    "Ask anything, @ to mention, / for actions": "Tanyakan apa saja, ketik @ untuk menyebutkan, / untuk tindakan",

    # Dialog Buttons & Common UI
    "OK": "OK",
    "Cancel": "Batal",
    "Yes": "Ya",
    "No": "Tidak",
    "Apply": "Terapkan",
    "Close": "Tutup",
    "Close All": "Tutup Semua",
    "Close Others": "Tutup Lainnya",
    "Close Saved": "Tutup yang Tersimpan",
    "Keep Open": "Biarkan Terbuka",
    "Copy Path": "Salin Jalur",
    "Copy Relative Path": "Salin Jalur Relatif",
    "Reveal in Finder": "Tampilkan di Finder",
    "Reveal in File Explorer": "Tampilkan di Penjelajah Berkas",
    "Open to the Side": "Buka di Samping",
    "Select for Compare": "Pilih untuk Membandingkan",
    "Compare with Selected": "Bandingkan dengan yang Dipilih",
    "Delete Permanently": "Hapus Secara Permanen",
    "Move to Trash": "Pindahkan ke Tong Sampah",
    "Rename": "Ganti Nama",
    "Format Document": "Format Dokumen",
    "Format Selection": "Format Pilihan",
    "Refactor...": "Refaktor...",
    "Source Action...": "Tindakan Sumber...",
    "Quick Fix...": "Perbaikan Cepat...",
    "Peek Definition": "Intip Definisi",
    "Find All References": "Cari Semua Referensi",
    "Rename Symbol": "Ganti Nama Simbol",
    "Change All Occurrences": "Ubah Semua Kemunculan",
    "Collapse All": "Ciutkan Semua",
    "Expand All": "Perluas Semua",
    "Refresh": "Segarkan",
    "Filter": "Saring",
    "Clear": "Bersihkan",
    "Install": "Pasang",
    "Uninstall": "Copot",
    "Disable": "Nonaktifkan",
    "Enable": "Aktifkan",
    "Reload": "Muat Ulang",
    "Reload Window": "Muat Ulang Jendela",
    "Restart": "Mulai Ulang",
    "Loading...": "Memuat...",
    "No results found": "Tidak ada hasil ditemukan",
    "Type to search": "Ketik untuk mencari"
}

# 2. Peta Mnemonic Khusus (& atau &&)
MNEMONIC_MAP = {
    "New File": "&&Berkas Baru...",
    "New Window": "Jendela &&Baru",
    "Open...": "&&Buka...",
    "Open File...": "&&Buka Berkas...",
    "Open Folder...": "Buka &&Folder...",
    "Open Workspace from File...": "Buka Ruang &&Kerja dari Berkas...",
    "Open Recent": "Buka &&Terkini",
    "Add Folder to Workspace...": "T&&ambahkan Folder ke Ruang Kerja...",
    "Save Workspace As...": "Simpan Ruang Kerja Seb&&agai...",
    "Save": "&&Simpan",
    "Save As...": "Simpan Seb&&agai...",
    "Save All": "Simpan Sem&&ua",
    "Auto Save": "Simpan &&Otomatis",
    "Revert File": "Kem&&balikan Berkas",
    "Close Editor": "&&Tutup Editor",
    "Close Folder": "Tutup &&Folder",
    "Close Window": "Tutup &&Jendela",
    "Close Workspace": "Tutup Ruang &&Kerja",
    "Undo": "&&Urungkan",
    "Redo": "&&Ulangi",
    "Cut": "Po&&tong",
    "Copy": "&&Salin",
    "Paste": "&&Tempel",
    "Find": "&&Cari",
    "Replace": "&&Ganti",
    "Select All": "Pilih &&Semua",
    "Yes": "&&Ya",
    "No": "&&Tidak",
    "Close": "&&Tutup"
}

# 3. Pola Kalimat (Sentence Pattern Rules)
PATTERNS = [
    (r"^Controls whether the editor should automatically (.+)\.$", r"Mengontrol apakah editor harus otomatis \1."),
    (r"^Controls whether the editor should (.+)\.$", r"Mengontrol apakah editor harus \1."),
    (r"^Controls whether the editor (.+)\.$", r"Mengontrol apakah editor \1."),
    (r"^Controls whether (.+)\.$", r"Mengontrol apakah \1."),
    (r"^Controls whether (.+)$", r"Mengontrol apakah \1"),
    (r"^Controls if (.+)\.$", r"Mengontrol jika \1."),
    (r"^Controls if (.+)$", r"Mengontrol jika \1"),
    (r"^Controls the (.+)\.$", r"Mengontrol \1."),
    (r"^Controls the (.+)$", r"Mengontrol \1"),
    (r"^Configure the (.+)\.$", r"Mengonfigurasi \1."),
    (r"^Configure (.+)\.$", r"Mengonfigurasi \1."),
    (r"^When enabled, (.+)\.$", r"Saat diaktifkan, \1."),
    (r"^When set to (.+), (.+)\.$", r"Saat disetel ke \1, \2."),
    (r"^The maximum number of (.+)\.$", r"Jumlah maksimum \1."),
    (r"^The minimum number of (.+)\.$", r"Jumlah minimum \1."),
    (r"^The number of (.+)\.$", r"Jumlah \1."),
    (r"^Timeout in milliseconds (.+)\.$", r"Batas waktu dalam milidetik \1."),
    (r"^Are you sure you want to delete (.+)\?$", r"Apakah Anda yakin ingin menghapus \1?"),
    (r"^Are you sure you want to permanently delete (.+)\?$", r"Apakah Anda yakin ingin menghapus secara permanen \1?"),
    (r"^Are you sure you want to (.+)\?$", r"Apakah Anda yakin ingin \1?"),
    (r"^Do you want to save the changes you made to (.+)\?$", r"Apakah Anda ingin menyimpan perubahan yang dibuat pada \1?"),
    (r"^Do you want to (.+)\?$", r"Apakah Anda ingin \1?"),
    (r"^Failed to (.+)\.$", r"Gagal \1."),
    (r"^Unable to (.+)\.$", r"Tidak dapat \1."),
    (r"^Cannot (.+)\.$", r"Tidak dapat \1."),
    (r"^An error occurred while (.+)\.$", r"Terjadi kesalahan saat \1."),
    (r"^Error while (.+)\.$", r"Kesalahan saat \1."),
    (r"^Successfully (.+)\.$", r"Berhasil \1."),
    (r"^Click to (.+)\.$", r"Klik untuk \1."),
    (r"^Click to (.+)$", r"Klik untuk \1"),
    (r"^Press (.+) to (.+)\.$", r"Tekan \1 untuk \2."),
    (r"^No (.+) found\.$", r"Tidak ada \1 yang ditemukan."),
    (r"^No (.+) found$", r"Tidak ada \1 ditemukan"),
    (r"^Go to (.+)$", r"Buka \1"),
    (r"^Show (.+)$", r"Tampilkan \1"),
    (r"^Hide (.+)$", r"Sembunyikan \1"),
    (r"^Toggle (.+)$", r"Alihkan \1"),
    (r"^Open (.+)$", r"Buka \1"),
    (r"^Close (.+)$", r"Tutup \1"),
    (r"^Delete (.+)$", r"Hapus \1"),
    (r"^Remove (.+)$", r"Hapus \1"),
    (r"^Clear (.+)$", r"Bersihkan \1"),
    (r"^Reset (.+)$", r"Atur Ulang \1"),
    (r"^Copy (.+)$", r"Salin \1"),
    (r"^Paste (.+)$", r"Tempel \1"),
    (r"^Cut (.+)$", r"Potong \1"),
    (r"^Select (.+)$", r"Pilih \1"),
    (r"^Create (.+)$", r"Buat \1"),
    (r"^Add (.+)$", r"Tambah \1"),
    (r"^Install (.+)$", r"Pasang \1"),
    (r"^Uninstall (.+)$", r"Copot \1"),
    (r"^Update (.+)$", r"Perbarui \1"),
    (r"^Reload (.+)$", r"Muat Ulang \1"),
    (r"^Restart (.+)$", r"Mulai Ulang \1"),
    (r"^Format (.+)$", r"Format \1"),
    (r"^Rename (.+)$", r"Ganti Nama \1"),
    (r"^Search (.+)$", r"Cari \1"),
    (r"^Save (.+)$", r"Simpan \1"),
    (r"^Switch to (.+)$", r"Beralih ke \1"),
    (r"^Run (.+)$", r"Jalankan \1"),
    (r"^Debug (.+)$", r"Debug \1"),
    (r"^Filter by (.+)$", r"Saring berdasarkan \1"),
    (r"^Sort by (.+)$", r"Urutkan berdasarkan \1")
]

# 4. Substitusi Kata & Istilah Teknis
WORD_REPLACEMENTS = [
    ("command palette", "palet perintah"),
    ("keyboard shortcuts", "pintasan papan ketik"),
    ("keybindings", "pintasan tombol"),
    ("status bar", "bilah status"),
    ("activity bar", "bilah aktivitas"),
    ("title bar", "bilah judul"),
    ("menu bar", "bilah menu"),
    ("side bar", "bilah sisi"),
    ("sidebar", "bilah sisi"),
    ("source control", "kontrol versi"),
    ("call stack", "tumpukan panggilan"),
    ("debug console", "konsol debug"),
    ("quick open", "buka cepat"),
    ("quick pick", "pilihan cepat"),
    ("zen mode", "mode zen"),
    ("full screen", "layar penuh"),
    ("breadcrumbs", "breadcrumbs"),
    ("minimap", "minimap"),
    ("code action", "tindakan kode"),
    ("quick fix", "perbaikan cepat"),
    ("rename symbol", "ganti nama simbol"),
    ("find all references", "cari semua referensi"),
    ("peek definition", "intip definisi"),
    ("format document", "format dokumen"),
    ("organize imports", "rapikan impor"),
    ("merge conflict", "konflik penggabungan"),
    ("stage changes", "tandai perubahan (stage)"),
    ("unstage changes", "batalkan tanda perubahan"),
    ("discard changes", "buang perubahan"),
    ("commit message", "pesan commit"),
    ("pull request", "pull request"),
    ("remote repository", "repositori jarak jauh"),
    ("local repository", "repositori lokal"),
    ("untracked changes", "perubahan tidak terlacak"),
    ("staged changes", "perubahan bertanda (staged)"),
    ("getting started", "memulai"),
    ("welcome page", "halaman selamat datang"),
    ("release notes", "catatan rilis"),
    ("documentation", "dokumentasi"),
    ("extensions view", "tampilan ekstensi"),
    ("check for updates", "periksa pembaruan"),
    ("word wrap", "pembungkusan kata"),
    ("line numbers", "nomor baris"),
    ("new terminal", "terminal baru"),
    ("split terminal", "bagi terminal"),
    ("clear terminal", "bersihkan terminal"),
    ("problems view", "tampilan masalah"),
    ("search in files", "cari dalam berkas"),
    ("replace in files", "ganti dalam berkas"),
    ("match case", "cocokkan huruf besar/kecil"),
    ("whole word", "kata utuh"),
    ("regular expression", "ekspresi reguler"),
    ("new file", "berkas baru"),
    ("new folder", "folder baru"),
    ("open folder", "buka folder"),
    ("open file", "buka berkas"),
    ("open workspace", "buka ruang kerja"),
    ("save as", "simpan sebagai"),
    ("save all", "simpan semua"),
    ("close editor", "tutup editor"),
    ("close window", "tutup jendela"),
    ("close folder", "tutup folder"),
    ("close workspace", "tutup ruang kerja"),
    ("workspace", "ruang kerja"),
    ("editor", "editor"),
    ("window", "jendela"),
    ("files", "berkas"),
    ("file", "berkas"),
    ("folders", "folder"),
    ("folder", "folder"),
    ("directory", "direktori"),
    ("directories", "direktori"),
    ("line", "baris"),
    ("column", "kolom"),
    ("selection", "pilihan"),
    ("commands", "perintah"),
    ("command", "perintah"),
    ("settings", "pengaturan"),
    ("preferences", "preferensi"),
    ("extension", "ekstensi"),
    ("extensions", "ekstensi"),
    ("snippet", "cuplikan kode"),
    ("snippets", "cuplikan kode"),
    ("output", "keluaran (output)"),
    ("problems", "masalah"),
    ("variables", "variabel"),
    ("breakpoints", "titik henti (breakpoints)"),
    ("breakpoint", "titik henti (breakpoint)"),
    ("indentation", "indentasi"),
    ("encoding", "pengodean (encoding)"),
    ("definition", "definisi"),
    ("implementation", "implementasi"),
    ("references", "referensi"),
    ("hover", "layang (hover)"),
    ("suggestions", "saran"),
    ("completions", "pelengkapan"),
    ("matches", "kecocokan"),
    ("match", "kecocokan"),
    ("read-only", "hanya-baca"),
    ("active", "aktif"),
    ("inactive", "tidak aktif"),
    ("enabled", "diaktifkan"),
    ("disabled", "dinonaktifkan"),
    ("default", "bawaan"),
    ("installed", "terpasang"),
    ("recommended", "disarankan"),
    ("automatic", "otomatis"),
    ("automatically", "secara otomatis")
]

# Istilah terkontaminasi/rusak dari pack lama yang HARUS dibersihkan
CONTAMINATED_PATTERNS = [
    (r"\bworkspace from berkas\b", "ruang kerja dari berkas"),
    (r"\bruang kerja from berkas\b", "ruang kerja dari berkas"),
    (r"\bfrom berkas\b", "dari berkas"),
    (r"\bwor&&kspace from berkas\b", "ruang &&kerja dari berkas"),
    (r"\ba&&dd folder to workspace\b", "t&&ambahkan folder ke ruang kerja"),
    (r"\badd folder to workspace\b", "tambahkan folder ke ruang kerja"),
    (r"\bsimpan as\b", "simpan sebagai"),
    (r"\bsimpan all\b", "simpan semua"),
    (r"\b&&open\b", "&&buka"),
    (r"\b&&save\b", "&&simpan"),
    (r"\bcu&&t\b", "po&&tong"),
    (r"\bclose editor\b", "tutup editor"),
    (r"\bclose window\b", "tutup jendela"),
    (r"\bnew file\b", "berkas baru"),
    (r"\bnew window\b", "jendela baru")
]

def clean_contaminated(text: str) -> str:
    if not isinstance(text, str):
        return text
    res = text
    for pat, rep in CONTAMINATED_PATTERNS:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)
    return res

def protect_tokens(text: str):
    tokens = []
    def repl(m):
        tokens.append(m.group(0))
        return f"__TOK_{len(tokens)-1}__"

    text = re.sub(r"\{[0-9]+\}", repl, text)
    text = re.sub(r"\%[0-9]*\$?[a-zA-Z]", repl, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)
    text = re.sub(r"`[^`]+`", repl, text)
    return text, tokens

def restore_tokens(text: str, tokens):
    for idx, tok in enumerate(tokens):
        text = text.replace(f"__TOK_{idx}__", tok)
    return text

def translate_string(src: str) -> str:
    if not src or not src.strip():
        return src

    if re.match(r"^[\s\{\}0-9\(\)\:\,\.\-\_\"\'\%\$\/\\]+$", src):
        return src

    has_double_amp = "&&" in src
    has_single_amp = src.startswith("&") and not has_double_amp

    # Bersihkan mnemonik untuk pencocokan kamus
    clean_src = src.replace("&&", "").lstrip("&").strip()

    # 1. Cek kamus mnemonik khusus
    if clean_src in MNEMONIC_MAP and (has_double_amp or has_single_amp):
        return MNEMONIC_MAP[clean_src]

    # 2. Cek Exact Phrase
    if clean_src in EXACT_PHRASES:
        id_val = EXACT_PHRASES[clean_src]
        if has_double_amp:
            return "&&" + id_val
        elif has_single_amp:
            return "&" + id_val
        return id_val

    # 3. Cek frase asli langsung
    if src in EXACT_PHRASES:
        return EXACT_PHRASES[src]

    # Lindungi token dinamis
    protected_text, tokens = protect_tokens(clean_src)

    # 4. Pola Kalimat
    matched_pattern = False
    for pat, rep in PATTERNS:
        if re.search(pat, protected_text, re.IGNORECASE):
            protected_text = re.sub(pat, rep, protected_text, flags=re.IGNORECASE)
            matched_pattern = True
            break

    # 5. Substitusi Istilah Teknis
    if matched_pattern:
        for en_word, id_word in WORD_REPLACEMENTS:
            pattern = r"\b" + re.escape(en_word) + r"\b"
            protected_text = re.sub(pattern, id_word, protected_text, flags=re.IGNORECASE)

    result = restore_tokens(protected_text, tokens)
    result = clean_contaminated(result)

    if has_double_amp and not ("&&" in result):
        result = "&&" + result

    return result

def main():
    print("=== Membangun Terjemahan VS Code & Antigravity (Pembersihan Total) ===")
    
    meta_path = "/Applications/Visual Studio Code.app/Contents/Resources/app/out/nls.metadata.json"
    if not os.path.exists(meta_path):
        print(f"❌ Error: {meta_path} tidak ditemukan!")
        sys.exit(1)

    print("1. Membaca metadata resmi VS Code (nls.metadata.json)...")
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    local_main_path = "translations/main.i18n.json"
    existing_contents = {}
    if os.path.exists(local_main_path):
        with open(local_main_path, "r", encoding="utf-8") as f:
            local_json = json.load(f)
            existing_contents = local_json.get("contents", {})

    print(f"2. Memproses {len(meta['keys'])} modul inti VS Code...")
    new_contents = {}
    total_strings = 0
    preserved_count = 0
    translated_count = 0
    cleaned_count = 0

    for mod_name, keys in meta["keys"].items():
        msgs = meta["messages"].get(mod_name, [])
        mod_dict = {}
        existing_mod = existing_contents.get(mod_name, {})

        for k, en_msg in zip(keys, msgs):
            k_str = k["key"] if isinstance(k, dict) else k
            total_strings += 1

            # Cek apakah modul ini adalah bagian menu penting atau sessions
            is_critical_menu = any(x in mod_name.lower() for x in ["workspaceactions", "editoractions", "windowactions", "fileactions", "sessions", "agenthost"])

            # Cek apakah ada terjemahan lama
            if k_str in existing_mod and not is_critical_menu:
                old_val = existing_mod[k_str]
                # Periksa apakah terkontaminasi bahasa Inggris
                cleaned_val = clean_contaminated(old_val)
                if cleaned_val != old_val:
                    cleaned_count += 1
                    mod_dict[k_str] = cleaned_val
                    continue

                if old_val != en_msg:
                    mod_dict[k_str] = old_val
                    preserved_count += 1
                    continue

            # Menerjemahkan dengan engine yang sudah di-upgrade
            translated_val = translate_string(en_msg)
            mod_dict[k_str] = translated_val
            translated_count += 1

        new_contents[mod_name] = mod_dict

    final_main = {
        "": [
            "--------------------------------------------------------------------------------------------",
            "Copyright (c) Microsoft Corporation. All rights reserved.",
            "Licensed under the MIT License. See License.txt in the project root for license information.",
            "--------------------------------------------------------------------------------------------",
            "Do not edit this file. It is machine generated."
        ],
        "version": "1.0.0",
        "contents": new_contents
    }

    print(f"3. Menyimpan terjemahan inti ke {local_main_path}...")
    with open(local_main_path, "w", encoding="utf-8") as f:
        json.dump(final_main, f, indent=2, ensure_ascii=False)

    print(f"   • Total Modul Terjemahan : {len(new_contents):,}")
    print(f"   • Total String           : {total_strings:,}")
    print(f"   • Teks Lama Dipertahankan: {preserved_count:,}")
    print(f"   • Teks Diterjemahkan Baru: {translated_count:,}")
    print(f"   • Teks Rusak Dibersihkan : {cleaned_count:,}")

    # 4. Memproses ekstensi bawaan (Built-in Extensions)
    print("\n4. Memproses ekstensi bawaan VS Code...")
    ext_dir = "/Applications/Visual Studio Code.app/Contents/Resources/app/extensions"
    registered_translations = [
        {
            "id": "vscode",
            "path": "./translations/main.i18n.json"
        }
    ]

    os.makedirs("translations/extensions", exist_ok=True)
    ext_count = 0
    ext_string_count = 0

    for ext_name in sorted(os.listdir(ext_dir)):
        ext_path = os.path.join(ext_dir, ext_name)
        if not os.path.isdir(ext_path):
            continue

        nls_file = os.path.join(ext_path, "package.nls.json")
        if not os.path.exists(nls_file):
            continue

        try:
            with open(nls_file, "r", encoding="utf-8") as f:
                nls_data = json.load(f)
        except Exception:
            continue

        ext_id = f"vscode.{ext_name}"
        dest_filename = f"{ext_id}.i18n.json"
        dest_path = os.path.join("translations/extensions", dest_filename)

        ext_contents = {}
        for k, v in nls_data.items():
            ext_string_count += 1
            if isinstance(v, dict):
                msg_val = v.get("message", "")
                ext_contents[k] = translate_string(msg_val) if msg_val else v
            elif isinstance(v, str):
                ext_contents[k] = translate_string(v)
            else:
                ext_contents[k] = v

        final_ext = {
            "": [
                "--------------------------------------------------------------------------------------------",
                "Copyright (c) Microsoft Corporation. All rights reserved.",
                "Licensed under the MIT License.",
                "--------------------------------------------------------------------------------------------"
            ],
            "version": "1.0.0",
            "contents": ext_contents
        }

        with open(dest_path, "w", encoding="utf-8") as f:
            json.dump(final_ext, f, indent=2, ensure_ascii=False)

        registered_translations.append({
            "id": ext_id,
            "path": f"./translations/extensions/{dest_filename}"
        })
        ext_count += 1

    print(f"   • Berhasil memproses {ext_count} ekstensi bawaan ({ext_string_count:,} string)!")

    # 5. Memperbarui package.json
    print("\n5. Memperbarui manifes package.json...")
    pkg = {
        "name": "vscode-language-pack-id",
        "displayName": "Indonesian Language Pack for Visual Studio Code",
        "description": "Paket Bahasa Indonesia resmi dan modern untuk Visual Studio Code",
        "version": "1.144.1",
        "publisher": "mrmarc",
        "license": "MIT",
        "homepage": "https://github.com/Mrmarc-bit/vscode-language-pack-id#readme",
        "repository": {
            "type": "git",
            "url": "https://github.com/Mrmarc-bit/vscode-language-pack-id.git"
        },
        "bugs": {
            "url": "https://github.com/Mrmarc-bit/vscode-language-pack-id/issues"
        },
        "engines": {
            "vscode": "^1.80.0"
        },
        "icon": "icon.png",
        "categories": [
            "Language Packs"
        ],
        "keywords": [
            "indonesian",
            "bahasa indonesia",
            "indonesia",
            "language pack",
            "terjemahan",
            "nusantara"
        ],
        "contributes": {
            "localizations": [
                {
                    "languageId": "id",
                    "languageName": "Indonesian",
                    "localizedLanguageName": "Bahasa Indonesia",
                    "translations": registered_translations
                }
            ]
        },
        "scripts": {
            "validate": "python3 scripts/validate.py",
            "link-local": "python3 scripts/install_local.py",
            "build-vsix": "python3 scripts/build_vsix.py",
            "sync": "python3 scripts/sync_upstream.py"
        }
    }

    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)

    print(f"   • package.json diperbarui dengan {len(registered_translations)} modul terdaftar.")
    print("\n🎉 GENERASI ULANG TERJEMAHAN SELESAI DENGAN SEMPURNA!")

if __name__ == "__main__":
    main()
