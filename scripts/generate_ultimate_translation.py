#!/usr/bin/env python3
"""
Generator Lengkap & Menyeluruh Indonesian Language Pack untuk Visual Studio Code Modern & Antigravity IDE.
Menerjemahkan seluruh menu bar, popup aksi, kustomisasi agen, kanvas, sesi, server MCP,
pengaturan, dialog, dan seluruh 92 ekstensi bawaan ke Bahasa Indonesia baku & alami.
"""

import os
import sys
import json
import re

# 1. MNEMONIK MENU BAR RESMI (&&)
MNEMONIC_MAP = {
    # Top Level Menu Bar
    "File": "&&Berkas",
    "Edit": "&&Ubah",
    "Selection": "&&Pilihan",
    "View": "&&Tampilan",
    "Go": "&&Buka",
    "Run": "&&Jalankan",
    "Terminal": "&&Terminal",
    "Window": "&&Jendela",
    "Help": "&&Bantuan",
    "Preferences": "&&Preferensi",

    # File Menu Items with Mnemonics
    "New Text File": "&&Berkas Teks Baru",
    "New File...": "&&Berkas Baru...",
    "New File": "&&Berkas Baru",
    "New Window": "Jendela &&Baru",
    "New Window with Profile": "Jendela Baru dengan &&Profil",
    "Open...": "&&Buka...",
    "Open File...": "&&Buka Berkas...",
    "Open Folder...": "Buka &&Folder...",
    "Open Workspace from File...": "Buka Ruang &&Kerja dari Berkas...",
    "Open Recent": "Buka &&Terkini",
    "Open Recent...": "Buka &&Terkini...",
    "Add Folder to Workspace...": "&&Tambah Folder ke Ruang Kerja...",
    "Save Workspace As...": "Simpan Ruang Kerja Seb&&agai...",
    "Duplicate Workspace": "&&Duplikasikan Ruang Kerja",
    "Save": "&&Simpan",
    "Save As...": "Simpan Seb&&agai...",
    "Save All": "Simpan Sem&&ua",
    "Share": "&&Bagikan",
    "Auto Save": "Simpan &&Otomatis",
    "Revert File": "Kem&&balikan Berkas",
    "Close Editor": "&&Tutup Editor",
    "Close Folder": "Tutup &&Folder",
    "Close Workspace": "Tutup Ruang &&Kerja",
    "Close Window": "Tutup Jen&&dela",
    "Exit": "&&Keluar",
    "Quit": "&&Keluar",

    # Edit Menu Items with Mnemonics
    "Undo": "&&Urungkan",
    "Redo": "&&Ulangi",
    "Cut": "&&Potong",
    "Copy": "&&Salin",
    "Paste": "&&Tempel",
    "Find": "&&Cari",
    "Replace": "&&Ganti",
    "Find in Files": "Cari dalam &&Berkas",
    "Replace in Files": "Ganti dalam Ber&&kas",
    "Toggle Line Comment": "Alihkan Komentar &&Baris",
    "Toggle Block Comment": "Alihkan Komentar Blo&&k",
    "Emmet: Expand Abbreviation": "&&Emmet: Bentangkan Singkatan",

    # Selection Menu Items
    "Select All": "Pilih Sem&&ua",
    "Expand Selection": "&&Bentangkan Pilihan",
    "Shrink Selection": "&&Ciutkan Pilihan",
    "Copy Line Up": "Salin Baris ke &&Atas",
    "Copy Line Down": "Salin Baris ke &Bawah",
    "Move Line Up": "Pindahkan Baris ke A&&tas",
    "Move Line Down": "Pindahkan Baris ke Ba&&wah",
    "Duplicate Selection": "Duplikasi Pili&&han",
    "Add Cursor Above": "Tambah Kursor di At&&as",
    "Add Cursor Below": "Tambah Kursor di Bawa&&h",
    "Add Cursors to Line Ends": "Tambah Kursor ke Ujung Bar&&is",
    "Add Next Occurrence": "Tambah Kemunculan Beriku&&tnya",
    "Add Previous Occurrence": "Tambah Kemunculan Sebelu&&mnya",
    "Select All Occurrences": "Pilih Semua Kemun&&culan",
    "Switch to Column Selection Mode": "Beralih ke Mode Pilihan &&Kolom",

    # View Menu Items
    "Command Palette...": "&&Palet Perintah...",
    "Open View...": "Buka &&Tampilan...",
    "Appearance": "&&Tampilan Antarmuka",
    "Primary Side Bar": "Bilah Sisi &&Utama",
    "Secondary Side Bar": "Bilah Sisi &&Sekunder",
    "Status Bar": "Bilah &&Status",
    "Activity Bar": "Bilah &&Aktivitas",
    "Panel": "&&Panel",
    "Editor Layout": "Tata Letak &&Editor",
    "Explorer": "&&Penjelajah",
    "Search": "&&Pencarian",
    "Source Control": "Kontrol &&Sumber",
    "Run and Debug": "Jalankan dan &&Debug",
    "Extensions": "&&Ekstensi",
    "Output": "&&Keluaran",
    "Problems": "&&Masalah",
    "Debug Console": "Konsol Debu&&g",
    "Full Screen": "Layar &&Penuh",
    "Zen Mode": "Mode &&Zen",
    "Centered Editor Layout": "Tata Letak Editor Ter&&pusat",
    "Centered Layout": "Tata Letak Ter&&pusat",
    "Word Wrap": "Bungkus &&Kata",
    "Single": "&&Tunggal",
    "Two Columns": "&&Dua Kolom",
    "Top": "&&Atas",
    "Bottom": "&&Bawah",
    "Grid (2x2)": "&&Kisi (2x2)",
    "Zoom In": "Per&&besar",
    "Zoom Out": "Per&&kecil",

    # Go Menu Items
    "Back": "&&Kembali",
    "Forward": "&&Maju",
    "Last Edit Location": "Lokasi Edit Ter&&akhir",
    "Next Edit Location": "Lokasi Edit Beriku&&tnya",
    "Switch Editor...": "Ganti &&Editor...",
    "Switch Group...": "Ganti &&Grup...",
    "Go to File...": "Buka Ber&&kas...",
    "Go to Symbol in Workspace...": "Buka Simbol di Ruang &&Kerja...",
    "Go to Symbol in Editor...": "Buka Simbol di &&Editor...",
    "Go to Line/Column...": "Buka Baris/&&Kolom...",
    "Go to Bracket": "Buka &&Kurung Pasangan",
    "Next Problem": "Masalah Beriku&&tnya",
    "Previous Problem": "Masalah Sebelu&&mnya",
    "Next Change": "Perubahan Beriku&&tnya",
    "Previous Change": "Perubahan Sebelu&&mnya",

    # Run Menu Items
    "Start Debugging": "Mulai &&Debugging",
    "Run Without Debugging": "Jalankan Tanpa Debuggin&&g",
    "Stop Debugging": "&&Hentikan Debugging",
    "Restart Debugging": "Mulai &Ulang Debugging",
    "Open Configurations": "Buka &&Konfigurasi",
    "Add Configuration...": "Tambah Konfigur&&asi...",
    "Step Over": "Lompati (Step &&Over)",
    "Step Into": "Masuk ke Dalam (Step &&Into)",
    "Step Out": "Keluar (Step Ou&&t)",
    "Continue": "&&Lanjutkan",
    "Toggle Breakpoint": "Alihkan Titik &&Henti",
    "New Breakpoint": "Titik Henti &&Baru",
    "Enable All Breakpoints": "Aktifkan Semua Titik Hen&&ti",
    "Disable All Breakpoints": "Nonaktifkan Semua Titik He&&nti",
    "Remove All Breakpoints": "Hapus Semua Titik Hent&&i",
    "Install Additional Debuggers...": "Pasang &&Debugger Tambahan...",
    "Data Breakpoint...": "Titik Henti &&Data...",
    "Function Breakpoint...": "Titik Henti &&Fungsi...",
    "Conditional Breakpoint...": "Titik Henti &&Kondisional...",
    "Triggered Breakpoint...": "Titik Henti Ter&&picu...",
    "Edit Breakpoint": "&&Ubah Titik Henti",
    "Logpoint...": "Titik Log (&&Logpoint)...",
    "Debug Anyway": "&&Debug Saja",

    # Terminal Menu Items
    "New Terminal": "Terminal &&Baru",
    "Split Terminal": "&&Bagi Terminal",
    "Run Task...": "Jalankan &&Tugas...",
    "Run Build Task...": "Jalankan Tugas &&Build...",
    "Run Active File": "Jalankan Berkas &&Aktif",
    "Run Selected Text": "Jalankan Teks Ter&&pilih",
    "Show Running Tasks...": "Tampilkan Tugas yang Ber&&jalan...",
    "Restart Running Task...": "Mulai Ulang Tugas yang Berja&&lan...",
    "Terminate Task...": "Hentikan Tu&&gas...",
    "Terminate Task": "&&Hentikan Tugas",
    "Terminate": "&&Hentikan",
    "Configure Tasks...": "Konfigurasikan Tu&&gas...",
    "Configure Default Build Task...": "Konfigurasikan Tugas Build Bawaa&&n...",

    # Window Menu Items
    "Minimize": "&&Minimalkan",
    "Zoom": "&&Perbesar",
    "Move Window to Left Side of Screen": "Pindahkan Jendela ke Sisi Kiri Lay&&ar",
    "Move Window to Right Side of Screen": "Pindahkan Jendela ke Sisi Kanan La&&yar",
    "Replace Window": "&&Ganti Jendela",
    "Bring All to Front": "Bawa Semua ke &&Depan",
    "Switch Window...": "Beralih &&Jendela...",

    # Help Menu Items
    "Welcome": "Selamat &&Datang",
    "Show All Commands": "Tampilkan Semua &&Perintah",
    "Documentation": "&&Dokumentasi",
    "Release Notes": "Catatan &&Rilis",
    "Keyboard Shortcuts Reference": "Referensi Pintasan Papan Tom&&bol",
    "Video Tutorials": "Tutorial &&Video",
    "Tips and Tricks": "&&Tips dan Trik",
    "Report Issue": "Laporkan &&Masalah",
    "Report Issue & Continue": "Laporkan Masalah &&& Lanjutkan",
    "Troubleshoot Issue": "&&Investigasi Masalah",
    "View License": "Lihat &&Lisensi",
    "Privacy Statement": "Pernyataan &&Privasi",
    "Toggle Developer Tools": "Alihkan Alat &&Pengembang",
    "Open Process Explorer": "Buka Penjelajah &&Proses",
    "Check for Updates...": "Periksa Pembarua&&n...",
    "About": "&&Tentang",
    "Join Us on YouTube": "&&Gabung Bersama Kami di YouTube",

    # Dialog & System Actions
    "OK": "&&OK",
    "Cancel": "&&Batal",
    "Save Anyway": "&&Simpan Saja",
    "Do not Save": "&&Jangan Simpan",
    "Don't Save": "&&Jangan Simpan",
    "Delete": "&&Hapus",
    "Remove": "&&Hapus",
    "Allow": "&&Izinkan",
    "Deny": "&&Tolak",
    "Retry": "&&Coba Lagi",
    "Try Again": "&&Coba Lagi",
    "Ignore": "&&Abaikan",
    "Learn More": "&&Pelajari Lebih Lanjut",
    "More Information": "Informasi Lebih &&Lanjut",
    "Sign In": "&&Masuk",
    "Sign Out": "&&Keluar",
    "Log In": "&&Masuk",
    "Connect": "&&Hubungkan",
    "Reopen": "&&Buka Kembali",
    "Keep Waiting": "&&Tetap Tunggu",
    "Sticky Scroll": "Gulir &&Lengket",
    "Focus Editor Sticky Scroll": "Fokuskan Gulir Lengket &&Editor",
    "Breadcrumbs": "&&Breadcrumb",
    "Next Session": "Sesi Beriku&&tnya",
    "Previous Session": "Sesi Sebelu&&mnya",
    "Next Group": "Grup Beriku&&tnya",
    "Previous Group": "Grup Sebelu&&mnya",
    "Next Used Editor": "Editor Digunakan Beriku&&tnya",
    "Previous Used Editor": "Editor Digunakan Sebelu&&mnya",
    "Add": "&&Tambah",
    "Rotate": "&&Putar",
    "Trust": "&&Percayai",
    "Restore": "&&Pulihkan",
    "Accept Merge": "&&Terima Penggabungan",
    "Fold Section": "&&Lipat Bagian",
    "Snippets": "&&Snippet",
    "Exit Anyways": "&&Tetap Keluar",
    "Themes": "&&Tema",
    "Insiders": "&&Insiders",
    "Profiles": "&&Profil",
    "Turn off": "&&Matikan",
    "No, I don't trust the authors": "&&Tidak, saya tidak mempercayai penulisnya",
    "Yes, I trust the authors": "&&Ya, saya mempercayai penulisnya",
    "Move to Recycle Bin": "Pindahkan ke Tempat &Sampah",
    "Move to Trash": "Pindahkan ke Tempat &Sampah",
    "Move": "&&Pindahkan",
    "Copy Editor Group into New Window": "&&Salin Grup Editor ke Jendela Baru",
    "Copy Editor into New Window": "&&Salin Editor ke Jendela Baru",
    "Move Editor Group into New Window": "&&Pindahkan Grup Editor ke Jendela Baru",
    "Move Editor into New Window": "&&Pindahkan Editor ke Jendela Baru",
    "New Empty Editor Window": "Jendela Editor Kosong &&Baru",
    "Restore Editors into Main Window": "&&Pulihkan Editor ke Jendela Utama",
    "Chat": "&&Obrolan",
    "DisassemblyView": "Tampilan &&Disasembli",
    "ToggleSource": "&&Alihkan Sumber",
    "Toggle Overtype/Insert Mode": "&&Alihkan Mode Overtype/Sisip"
}

# 2. FRASA UI & PERINTAH PERSIS (EXACT MATCHES)
EXACT_PHRASES = {
    # Top & Core Menus
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
    "New Text File": "Berkas Teks Baru",
    "New File": "Berkas Baru",
    "New File...": "Berkas Baru...",
    "New Window": "Jendela Baru",
    "New Window with Profile": "Jendela Baru dengan Profil",
    "New Window with Profile...": "Jendela Baru dengan Profil...",
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
    "Open Recent...": "Buka Terkini...",
    "More...": "Lainnya...",
    "Reopen Closed Editor": "Buka Kembali Editor yang Ditutup",
    "Reopen Editor With...": "Buka Kembali Editor Dengan...",
    "Reopen Editor with Text Editor": "Buka Kembali Editor dengan Editor Teks",
    "Clear Recently Opened": "Bersihkan Daftar Terkini",
    "Clear Recently Opened...": "Bersihkan Daftar Terkini...",
    "Clear Recent": "Bersihkan Terkini",
    "Clear Recent...": "Bersihkan Terkini...",
    "Add Folder to Workspace...": "Tambahkan Folder ke Ruang Kerja...",
    "Save Workspace As...": "Simpan Ruang Kerja Sebagai...",
    "Duplicate Workspace": "Duplikasikan Ruang Kerja",
    "Duplicate Workspace in New Window": "Duplikasikan Ruang Kerja di Jendela Baru",
    "Duplicate As Workspace in New Window": "Duplikasikan sebagai Ruang Kerja di Jendela Baru",
    "Save": "Simpan",
    "Save As...": "Simpan Sebagai...",
    "Save As": "Simpan Sebagai",
    "Save All": "Simpan Semua",
    "Save All in Group": "Simpan Semua dalam Grup",
    "Save All Files": "Simpan Semua Berkas",
    "Auto Save": "Simpan Otomatis",
    "Preferences": "Preferensi",
    "Settings": "Pengaturan",
    "Revert File": "Kembalikan Berkas",
    "Close Editor": "Tutup Editor",
    "Close All Editors": "Tutup Semua Editor",
    "Close All Editor Groups": "Tutup Semua Grup Editor",
    "Close Others": "Tutup Lainnya",
    "Close Saved": "Tutup yang Tersimpan",
    "Close Other Editors": "Tutup Editor Lainnya",
    "Close Editors to the Right": "Tutup Editor ke Kanan",
    "Close Editors to the Left": "Tutup Editor ke Kiri",
    "Close Editors to the Left in Group": "Tutup Editor di Sebelah Kiri dalam Grup",
    "Close Editors in Other Groups": "Tutup Editor di Grup Lain",
    "Close Editor in All Groups": "Tutup Editor di Semua Grup",
    "Close Folder": "Tutup Folder",
    "Close Workspace": "Tutup Ruang Kerja",
    "Close Window": "Tutup Jendela",
    "Exit": "Keluar",
    "Quit": "Keluar",
    "Share": "Bagikan",
    "Share...": "Bagikan...",

    # Editor Actions
    "Clear Editor History": "Bersihkan Riwayat Editor",
    "Clear Editor History without Confirmation": "Bersihkan Riwayat Editor tanpa Konfirmasi",
    "Copy Editor Group into New Window": "Salin Grup Editor ke Jendela Baru",
    "Copy Editor into New Window": "Salin Editor ke Jendela Baru",
    "Move Editor Group into New Window": "Pindahkan Grup Editor ke Jendela Baru",
    "Move Editor into New Window": "Pindahkan Editor ke Jendela Baru",
    "New Empty Editor Window": "Jendela Editor Kosong Baru",
    "New Editor Group Above": "Grup Editor Baru di Atas",
    "New Editor Group Below": "Grup Editor Baru di Bawah",
    "New Editor Group to the Left": "Grup Editor Baru di Kiri",
    "New Editor Group to the Right": "Grup Editor Baru di Kanan",
    "Open Next Editor in Group": "Buka Editor Berikutnya dalam Grup",
    "Open Next Editor": "Buka Editor Berikutnya",
    "Open Next Recently Used Editor": "Buka Editor Baru Digunakan Berikutnya",
    "Open Next Recently Used Editor In Group": "Buka Editor Baru Digunakan Berikutnya dalam Grup",
    "Open Previous Editor": "Buka Editor Sebelumnya",
    "Open Previous Editor in Group": "Buka Editor Sebelumnya dalam Grup",
    "Open Previous Recently Used Editor": "Buka Editor Baru Digunakan Sebelumnya",
    "Open Previous Recently Used Editor In Group": "Buka Editor Baru Digunakan Sebelumnya dalam Grup",
    "Quick Open Least Recently Used Editor": "Buka Cepat Editor yang Paling Jarang Digunakan",
    "Quick Open Least Recently Used Editor in Group": "Buka Cepat Editor yang Paling Jarang Digunakan dalam Grup",
    "Quick Open Previous Recently Used Editor": "Buka Cepat Editor Sebelumnya yang Baru Digunakan",
    "Quick Open Previous Recently Used Editor in Group": "Buka Cepat Editor Sebelumnya yang Baru Digunakan dalam Grup",
    "Restore Editors into Main Window": "Pulihkan Editor ke Jendela Utama",
    "Revert and Close Editor": "Kembalikan dan Tutup Editor",
    "Reverting Editors...": "Mengembalikan Editor...",
    "Show All Editors By Appearance": "Tampilkan Semua Editor Berdasarkan Tampilan",
    "Show All Editors By Most Recently Used": "Tampilkan Semua Editor Berdasarkan yang Baru Digunakan",
    "Show Editors in Active Group By Most Recently Used": "Tampilkan Editor di Grup Aktif Berdasarkan yang Baru Digunakan",
    "Split Editor": "Bagi Editor",
    "Split Editor Down": "Bagi Editor ke Bawah",
    "Split Editor Left": "Bagi Editor ke Kiri",
    "Split Editor Right": "Bagi Editor ke Kanan",
    "Split Editor Up": "Bagi Editor ke Atas",
    "Split Editor Orthogonal": "Bagi Editor Tegak Lurus",
    "Toggle Editor Type": "Alihkan Tipe Editor",
    "Toggle Editor Group Sizes": "Alihkan Ukuran Grup Editor",
    "Toggle Maximize Editor Group": "Alihkan Maksimalkan Grup Editor",
    "Unmaximize Group": "Batalkan Maksimalkan Grup",
    "Unpin Editor": "Lepas Sematan Editor",
    "Duplicate Editor Group Down": "Duplikasikan Grup Editor ke Bawah",
    "Duplicate Editor Group Left": "Duplikasikan Grup Editor ke Kiri",
    "Duplicate Editor Group Right": "Duplikasikan Grup Editor ke Kanan",
    "Duplicate Editor Group Up": "Duplikasikan Grup Editor ke Atas",
    "Single Column Editor Layout": "Tata Letak Editor Satu Kolom",
    "Three Columns Editor Layout": "Tata Letak Editor Tiga Kolom",
    "Three Rows Editor Layout": "Tata Letak Editor Tiga Baris",
    "Grid Editor Layout (2x2)": "Tata Letak Editor Kisi (2x2)",
    "Two Columns Editor Layout": "Tata Letak Editor Dua Kolom",
    "Two Columns Bottom Editor Layout": "Tata Letak Editor Dua Kolom di Bawah",
    "Two Rows Editor Layout": "Tata Letak Editor Dua Baris",
    "Two Rows Right Editor Layout": "Tata Letak Editor Dua Baris di Kanan",
    "Reset Editor Group Sizes": "Atur Ulang Ukuran Grup Editor",

    # File Operations Dialogs
    "Do you want to clear the history of recently opened editors?": "Apakah Anda ingin membersihkan riwayat editor yang baru saja dibuka?",
    "Do you want to clear all recently opened files and workspaces?": "Apakah Anda ingin membersihkan semua berkas dan ruang kerja yang baru saja dibuka?",
    "This action is irreversible!": "Tindakan ini tidak dapat diurungkan!",
    "Buka di Samping": "Buka di Samping",
    "Open to the Side": "Buka di Samping",
    "open to the side": "buka di samping",
    "Folder Baru...": "Folder Baru...",
    "New Folder...": "Folder Baru...",
    "New folder...": "Folder Baru...",
    "New Folder": "Folder Baru",
    "Delete Permanently": "Hapus Secara Permanen",
    "Reload Window": "Muat Ulang Jendela",
    "Toggle Auto Save": "Alihkan Simpan Otomatis",
    "Alihkan Simpan Otomatis": "Alihkan Simpan Otomatis",

    # Antigravity & Copilot UI
    "Sessions": "Sesi",
    "New": "Baru",
    "Automations": "Otomatisasi",
    "Chats": "Obrolan",
    "Customizations": "Kustomisasi",
    "Overview": "Ringkasan",
    "Plugins": "Plugin",
    "Canvases": "Kanvas",
    "MCP Servers": "Server MCP",
    "Skills": "Keahlian",
    "Instructions": "Instruksi",
    "Agents": "Agen",
    "Hooks": "Kait",
    "Tools": "Alat",
    "Migrations": "Migrasi",
    "Review Migrations": "Tinjau Migrasi",
    "Migrate with Agent": "Migrasikan dengan Agen",
    "Keep your customizations working": "Pertahankan kustomisasi Anda tetap berfungsi",
    "Copilot's new agent runtime uses different formats and locations for some customizations. Review and migrate the affected items below.": "Runtime agen baru Copilot menggunakan format dan lokasi yang berbeda untuk sejumlah kustomisasi. Tinjau dan migrasikan item yang terdampak di bawah ini.",
    "Learn About Migrations": "Pelajari Tentang Migrasi",
    "Learn more about migrations": "Pelajari lebih lanjut tentang migrasi",
    "Prompt-to-skill conversion changes": "Perubahan konversi Prompt ke Keahlian",
    "Unsupported prompt-only headers are removed. Converted skills set disable-model-invocation: true, so the agent will not load them automatically; invoke them manually with /name.": "Header khusus prompt yang tidak didukung telah dihapus. Keahlian yang dikonversi disetel ke disable-model-invocation: true, sehingga agen tidak memuatnya secara otomatis; panggil secara manual dengan /name.",
    "Convert Prompt to Skills (User)": "Konversi Prompt ke Keahlian (Pengguna)",
    "MCP Servers (User)": "Server MCP (Pengguna)",
    "User Data (User)": "Data Pengguna (Pengguna)",
    "Chat Participants (Ekstensi)": "Peserta Obrolan (Ekstensi)",
    "Needs manual review": "Perlu peninjauan manual",
    "Review": "Tinjau",
    "Ignore": "Abaikan",
    "Migrate...": "Migrasikan...",
    "Migrate": "Migrasikan",
    "VS Code will ask you to trust this server again after migration.": "VS Code akan meminta Anda mempercayai server ini lagi setelah migrasi.",
    "Undo Last Edit": "Urungkan Pengeditan Terakhir",
    "Redo Last Edit": "Ulangi Pengeditan Terakhir",
    "Move Chat into Editor Area": "Pindahkan Obrolan ke Area Editor",
    "Move Chat into New Window": "Pindahkan Obrolan ke Jendela Baru",
    "Tool Sets": "Kumpulan Alat",
    "Chat Settings": "Pengaturan Obrolan",
    "Show Chat Debug View": "Tampilkan Tampilan Debug Obrolan",
    "Show Voice Transcripts": "Tampilkan Transkrip Suara",
    "Show Agent Debug Logs": "Tampilkan Log Debug Agen",
    "Show View by Default": "Tampilkan Tampilan secara Bawaan",
    "Browse customizations": "Jelajahi kustomisasi",
    "Browse": "Jelajahi",
    "Tailor your agent to your tools, your team, and your workflow.": "Sesuaikan agen Anda dengan alat, tim, dan alur kerja Anda.",
    "Search MCP servers, plugins, skills and more...": "Cari server MCP, plugin, keahlian, dan lainnya...",
    "All Sources": "Semua Sumber",
    "Editor's picks": "Pilihan Editor",
    "Plan, build, and ship": "Rencanakan, bangun, dan rilis",
    "Connect your work": "Hubungkan pekerjaan Anda",
    "Install": "Pasang",
    "Uninstall": "Copot",
    "Installed": "Terpasang",
    "Canvases are interactive visual surfaces shared by you and the agent.": "Kanvas adalah antarmuka visual interaktif yang dibagikan antara Anda dan agen.",
    "Canvases are interactive visual surfaces shared by you and the agent. Learn more about canvases": "Kanvas adalah antarmuka visual interaktif yang dibagikan antara Anda dan agen. Pelajari lebih lanjut tentang kanvas",
    "Canvases are only available inside a session": "Kanvas hanya tersedia di dalam sesi",
    "Select an active Copilot session and then open this Customizations menu again": "Pilih sesi Copilot yang aktif lalu buka kembali menu Kustomisasi ini",
    "An open standard that lets AI use external tools and services. MCP servers provide tools for file operations, databases, APIs, and more.": "Standar terbuka yang memungkinkan AI menggunakan alat dan layanan eksternal. Server MCP menyediakan alat untuk operasi berkas, basis data, API, dan lainnya.",
    "Learn more about MCP servers": "Pelajari lebih lanjut tentang server MCP",
    "Extend your AI agent with plugins that add commands, skills, agents, hooks, and MCP servers from reusable packages.": "Perluas kemampuan agen AI Anda dengan plugin yang menambahkan perintah, keahlian, agen, kait, dan server MCP dari paket yang dapat digunakan kembali.",
    "Learn more about agent plugins": "Pelajari lebih lanjut tentang plugin agen",
    "Type to search...": "Ketik untuk mencari...",
    "Start": "Mulai",
    "Stop": "Hentikan",
    "Migration available": "Migrasi tersedia",
    "User": "Pengguna",
    "Workspace": "Ruang Kerja",
    "Plugin": "Plugin",
    "Extension": "Ekstensi",
    "Built-In": "Bawaan",
    "Built-in": "Bawaan",
    "Local": "Lokal",
    "Remote": "Jarak Jauh",
    "Sign In": "Masuk",
    "Sign Out": "Keluar",
    "Log In": "Masuk",
    "Log Out": "Keluar",
    "Skip": "Lewati",
    "Unknown": "Tidak Diketahui",
    "Pin": "Sematkan",
    "Unpin": "Lepas Sematan",
    "Download": "Unduh",
    "Upload": "Unggah",
    "Learn more": "Pelajari lebih lanjut",
    "Learn More": "Pelajari Lebih Lanjut",
    "Unavailable": "Tidak Tersedia",
    "Available": "Tersedia",
    "Do not ask me again": "Jangan tanya saya lagi",
    "Don't ask again": "Jangan tanya lagi",
    "Always allow": "Selalu izinkan",
    "Always deny": "Selalu tolak",
    "Never allow": "Jangan pernah izinkan",
    "Remember my choice": "Ingat pilihan saya",

    # Common UI Controls & Status
    "OK": "OK",
    "Cancel": "Batal",
    "Apply": "Terapkan",
    "Yes": "Ya",
    "No": "Tidak",
    "Always": "Selalu",
    "Never": "Jangan Pernah",
    "Ask": "Tanya",
    "Retry": "Coba Lagi",
    "Delete": "Hapus",
    "Remove": "Hapus",
    "Clear": "Bersihkan",
    "Reset": "Atur Ulang",
    "Configure": "Konfigurasikan",
    "Manage": "Kelola",
    "Refresh": "Segarkan",
    "Reload": "Muat Ulang",
    "Restart": "Mulai Ulang",
    "Show": "Tampilkan",
    "Hide": "Sembunyikan",
    "Copy": "Salin",
    "Paste": "Tempel",
    "Cut": "Potong",
    "Select": "Pilih",
    "Select All": "Pilih Semua",
    "Search": "Cari",
    "Filter": "Saring",
    "Sort": "Urutkan",
    "Next": "Berikutnya",
    "Previous": "Sebelumnya",
    "Back": "Kembali",
    "Forward": "Maju",
    "Done": "Selesai",
    "Close": "Tutup",
    "Save": "Simpan",
    "Save All": "Simpan Semua",
    "Don't Save": "Jangan Simpan",
    "Dismiss": "Tutup",
    "Import": "Impor",
    "Export": "Ekspor",
    "Browse...": "Jelajahi...",
    "Preview": "Pratinjau",
    "Loading...": "Memuat...",
    "Error": "Kesalahan",
    "Warning": "Peringatan",
    "Info": "Informasi",
    "Success": "Berhasil",
    "Failed": "Gagal",
    "Status": "Status",
    "Details": "Detail",
    "More Actions...": "Tindakan Lainnya...",
    "Collapse All": "Ciutkan Semua",
    "Expand All": "Bentangkan Semua",
    "Default": "Bawaan",
    "None": "Tidak Ada",
    "Disabled": "Dinonaktifkan",
    "Enabled": "Diaktifkan",
    "Running": "Berjalan",
    "Name": "Nama",
    "Description": "Deskripsi",
    "Rename...": "Ganti Nama...",
    "Rename": "Ganti Nama",
    "Approvals": "Persetujuan",
    "Browser": "Peramban",
    "Off": "Mati",
    "On": "Nyala",
    "Outline": "Garis Besar",
    "Timeline": "Linimasa",
    "Breadcrumbs": "Breadcrumb",
    "Minimap": "Peta Mini",
    "Word Wrap": "Bungkus Kata",
    "Line Numbers": "Nomor Baris",
    "Format Document": "Format Dokumen",
    "Refactor...": "Refaktor...",
    "Change All Occurrences": "Ubah Semua Kemunculan",
    "Source Action...": "Tindakan Sumber...",
    "Organize Imports": "Rapikan Impor",
    "Go to Definition": "Buka Definisi",
    "Peek Definition": "Intip Definisi",
    "Find All References": "Cari Semua Referensi",
    "Go to Implementation": "Buka Implementasi",
    "Go to Type Definition": "Buka Definisi Tipe",
    "Keyboard Shortcuts": "Pintasan Papan Tombol",
    "User Snippets": "Snippet Pengguna",
    "Color Theme": "Tema Warna",
    "File Icon Theme": "Tema Ikon Berkas",
    "Product Icon Theme": "Tema Ikon Produk",
    "Check for Updates...": "Periksa Pembaruan...",
    "About": "Tentang",
    "Release Notes": "Catatan Rilis",
    "Documentation": "Dokumentasi",
    "Report Issue": "Laporkan Masalah",
    "Toggle Developer Tools": "Alihkan Alat Pengembang",
    "Open Process Explorer": "Buka Penjelajah Proses",
    "Show All Commands": "Tampilkan Semua Perintah"
}

# 3. POLA GRAMATIKAL LENGKAP & TEMA
PATTERNS = [
    # Tema Warna & UI Tampilan
    (r"^The background color of (the |an |a )?(.*)", r"Warna latar belakang dari \2"),
    (r"^The foreground color of (the |an |a )?(.*)", r"Warna latar depan dari \2"),
    (r"^The border color of (the |an |a )?(.*)", r"Warna batas dari \2"),
    (r"^Background color of (the |an |a )?(.*)", r"Warna latar belakang dari \2"),
    (r"^Foreground color of (the |an |a )?(.*)", r"Warna latar depan dari \2"),
    (r"^Border color of (the |an |a )?(.*)", r"Warna batas dari \2"),
    (r"^Color of (the |an |a )?(.*)", r"Warna dari \2"),
    (r"^Color for (the |an |a )?(.*)", r"Warna untuk \2"),
    (r"^Icon for (the |an |a )?(.*)", r"Ikon untuk \2"),
    (r"^View icon of (the |an |a )?(.*)", r"Ikon tampilan dari \2"),
    (r"^True when (the |an |a )?(.*)", r"Bernilai True saat \2"),
    (r"^False when (the |an |a )?(.*)", r"Bernilai False saat \2"),
    (r"^This will delete (.*)", r"Tindakan ini akan menghapus \1"),
    (r"^This will remove (.*)", r"Tindakan ini akan menghapus \1"),
    (r"^This will sign out (.*)", r"Tindakan ini akan mengeluarkan \1"),
    (r"^Unable to write to (.*)", r"Tidak dapat menulis ke \1"),
    (r"^Unable to open (.*)", r"Tidak dapat membuka \1"),
    (r"^Unable to delete (.*)", r"Tidak dapat menghapus \1"),
    (r"^Unable to read (.*)", r"Tidak dapat membaca \1"),
    (r"^You can restore (.*)", r"Anda dapat memulihkan \1"),
    (r"^Plays a sound when (.*)", r"Memutar suara saat \1"),
    (r"^Plays a sound (.*)", r"Memutar suara \1"),
    (r"^Provide information about (.*)", r"Memberikan informasi tentang \1"),
    (r"^Select a location to (.*)", r"Pilih lokasi untuk \1"),
    (r"^Select a location (.*)", r"Pilih lokasi \1"),

    # Settings Descriptions
    (r"^Controls whether suggestions should be accepted on commit characters\..*", "Mengontrol apakah saran harus diterima pada karakter commit. Misalnya, pada JavaScript, titik koma (`;`) dapat berupa karakter commit yang menerima saran dan mengetik karakter tersebut."),
    (r"^Controls whether suggestions should be accepted on `Enter`.*", "Mengontrol apakah saran harus diterima dengan tombol `Enter`, selain tombol `Tab`. Membantu menghindari kerancuan antara memasukkan baris baru atau menerima saran."),
    (r"^Controls whether to allow using variable fonts in the editor\..*", "Mengontrol apakah mengizinkan penggunaan font variabel di editor."),
    (r"^Controls whether to allow using variable line heights in the editor\..*", "Mengontrol apakah mengizinkan tinggi baris variabel di editor."),
    (r"^Controls whether (.*)", r"Mengontrol apakah \1"),
    (r"^Controls if (.*)", r"Mengontrol jika \1"),
    (r"^Controls how (.*)", r"Mengontrol bagaimana \1"),
    (r"^Controls the (.*)", r"Mengontrol \1"),
    (r"^Controls (.*)", r"Mengontrol \1"),
    (r"^When enabled, (.*)", r"Saat diaktifkan, \1"),
    (r"^When disabled, (.*)", r"Saat dinonaktifkan, \1"),
    (r"^When (.*)", r"Saat \1"),
    (r"^Whether to (.*)", r"Apakah akan \1"),
    (r"^Whether (.*)", r"Apakah \1"),
    (r"^Determines whether (.*)", r"Menentukan apakah \1"),
    (r"^Determines if (.*)", r"Menentukan jika \1"),
    (r"^Determines (.*)", r"Menentukan \1"),
    (r"^Configure (.*)", r"Konfigurasikan \1"),
    (r"^Configures (.*)", r"Mengonfigurasi \1"),
    (r"^Specifies the (.*)", r"Menentukan \1"),
    (r"^Specifies (.*)", r"Menentukan \1"),
    (r"^The number of (.*)", r"Jumlah \1"),
    (r"^A list of (.*)", r"Daftar \1"),
    (r"^List of (.*)", r"Daftar \1"),
    (r"^An array of (.*)", r"Larik \1"),
    (r"^Timeout in milliseconds.*", "Batas waktu dalam milidetik."),
    (r"^Enable/disable (.*)", r"Aktifkan/nonaktifkan \1"),
    (r"^Enables (.*)", r"Mengaktifkan \1"),
    (r"^Disables (.*)", r"Menonaktifkan \1"),
    (r"^Enable (.*)", r"Aktifkan \1"),
    (r"^Disable (.*)", r"Nonaktifkan \1"),
    
    # Dialogs & Prompts
    (r"^Do you want to (.*)\?", r"Apakah Anda ingin \1?"),
    (r"^Are you sure you want to (.*)\?", r"Apakah Anda yakin ingin \1?"),
    (r"^Failed to (.*)", r"Gagal \1"),
    (r"^Unable to (.*)", r"Tidak dapat \1"),
    (r"^Could not (.*)", r"Tidak dapat \1"),
    (r"^Cannot (.*)", r"Tidak dapat \1"),
    (r"^No (.*) found", r"Tidak ada \1 yang ditemukan"),
    (r"^Successfully (.*)", r"Berhasil \1"),
    (r"^An error occurred while (.*)", r"Terjadi kesalahan saat \1"),
    (r"^Click to (.*)", r"Klik untuk \1"),
    (r"^Press (.*) to (.*)", r"Tekan \1 untuk \2"),
    (r"^Type (.*) to (.*)", r"Ketik \1 untuk \2"),

    # Action / Command Patterns
    (r"^Open ([A-Za-z0-9_\-\s]+) in New Window$", r"Buka \1 di Jendela Baru"),
    (r"^Open in ([A-Za-z0-9_\-\s]+)$", r"Buka di \1"),
    (r"^Move ([A-Za-z0-9_\-\s]+) into ([A-Za-z0-9_\-\s]+)$", r"Pindahkan \1 ke \2"),
    (r"^Move ([A-Za-z0-9_\-\s]+) to ([A-Za-z0-9_\-\s]+)$", r"Pindahkan \1 ke \2"),
    (r"^Copy ([A-Za-z0-9_\-\s]+) into ([A-Za-z0-9_\-\s]+)$", r"Salin \1 ke \2"),
    (r"^Copy ([A-Za-z0-9_\-\s]+) to ([A-Za-z0-9_\-\s]+)$", r"Salin \1 ke \2"),
    (r"^Show ([A-Za-z0-9_\-\s]+) by default$", r"Tampilkan \1 secara bawaan"),
    (r"^Show ([A-Za-z0-9_\-\s]+)$", r"Tampilkan \1"),
    (r"^Hide ([A-Za-z0-9_\-\s]+)$", r"Sembunyikan \1"),
    (r"^Toggle ([A-Za-z0-9_\-\s]+)$", r"Alihkan \1"),
    (r"^Select ([A-Za-z0-9_\-\s]+)$", r"Pilih \1"),
    (r"^Clear ([A-Za-z0-9_\-\s]+)$", r"Bersihkan \1"),
    (r"^Reset ([A-Za-z0-9_\-\s]+)$", r"Atur Ulang \1"),
    (r"^Delete ([A-Za-z0-9_\-\s]+)$", r"Hapus \1"),
    (r"^Remove ([A-Za-z0-9_\-\s]+)$", r"Hapus \1"),
    (r"^Add ([A-Za-z0-9_\-\s]+)$", r"Tambah \1"),
    (r"^Create ([A-Za-z0-9_\-\s]+)$", r"Buat \1"),
    (r"^Close ([A-Za-z0-9_\-\s]+)$", r"Tutup \1"),
    (r"^Save ([A-Za-z0-9_\-\s]+)$", r"Simpan \1"),
]

# 4. KATA & ISTILAH TEKNIS (KBBI & STANDARD DEVKIT INDONESIA)
WORD_REPLACEMENTS = [
    (r"\binto\b", "ke"),
    (r"\bfrom\b", "dari"),
    (r"\bwith\b", "dengan"),
    (r"\bwithout\b", "tanpa"),
    (r"\bfor\b", "untuk"),
    (r"\band\b", "dan"),
    (r"\bor\b", "atau"),
    (r"\bby default\b", "secara bawaan"),
    (r"\bby\b", "oleh"),

    # Technical Nouns
    (r"\bfile\b", "berkas"),
    (r"\bfiles\b", "berkas"),
    (r"\bfolder\b", "folder"),
    (r"\bfolders\b", "folder"),
    (r"\bdirectory\b", "direktori"),
    (r"\bdirectories\b", "direktori"),
    (r"\bworkspace\b", "ruang kerja"),
    (r"\bworkspaces\b", "ruang kerja"),
    (r"\bwindow\b", "jendela"),
    (r"\bwindows\b", "jendela"),
    (r"\beditor\b", "editor"),
    (r"\beditors\b", "editor"),
    (r"\bgroup\b", "grup"),
    (r"\bgroups\b", "grup"),
    (r"\bsettings\b", "pengaturan"),
    (r"\bsetting\b", "pengaturan"),
    (r"\bpreferences\b", "preferensi"),
    (r"\bkeyboard shortcuts\b", "pintasan papan tombol"),
    (r"\bextensions\b", "ekstensi"),
    (r"\bextension\b", "ekstensi"),
    (r"\boutput\b", "keluaran"),
    (r"\bproblems\b", "masalah"),
    (r"\bterminal\b", "terminal"),
    (r"\bview\b", "tampilan"),
    (r"\bviews\b", "tampilan"),
    (r"\bhistory\b", "riwayat"),
    (r"\brecently opened\b", "baru saja dibuka"),
    (r"\brecent\b", "terkini"),
    (r"\bactive\b", "aktif"),
    (r"\bcurrent\b", "saat ini"),
    (r"\bdefault\b", "bawaan"),
    (r"\bcustomization\b", "kustomisasi"),
    (r"\bcustomizations\b", "kustomisasi"),
    (r"\bplugin\b", "plugin"),
    (r"\bplugins\b", "plugin"),
    (r"\bcanvas\b", "kanvas"),
    (r"\bcanvases\b", "kanvas"),
    (r"\bMCP server\b", "server MCP"),
    (r"\bMCP servers\b", "server MCP"),
    (r"\bskill\b", "keahlian"),
    (r"\bskills\b", "keahlian"),
    (r"\binstruction\b", "instruksi"),
    (r"\binstructions\b", "instruksi"),
    (r"\bagent\b", "agen"),
    (r"\bagents\b", "agen"),
    (r"\bhook\b", "kait"),
    (r"\bhooks\b", "kait"),
    (r"\btool\b", "alat"),
    (r"\btools\b", "alat"),
    (r"\btool sets\b", "kumpulan alat"),
    (r"\btool set\b", "kumpulan alat"),
    (r"\bmigration\b", "migrasi"),
    (r"\bmigrations\b", "migrasi"),
    (r"\bsession\b", "sesi"),
    (r"\bsessions\b", "sesi"),
    (r"\bparticipant\b", "peserta"),
    (r"\bparticipants\b", "peserta"),
    (r"\bdebug console\b", "konsol debug"),
    (r"\bbreadcrumbs\b", "breadcrumb"),
    (r"\bminimap\b", "peta mini"),
    (r"\bsticky scroll\b", "gulir lengket"),
    (r"\bprimary side bar\b", "bilah sisi utama"),
    (r"\bsecondary side bar\b", "bilah sisi sekunder"),
    (r"\bside bar\b", "bilah sisi"),
    (r"\bstatus bar\b", "bilah status"),
    (r"\bactivity bar\b", "bilah aktivitas"),
    (r"\btitle bar\b", "bilah judul"),
    (r"\bpanel\b", "panel"),
    (r"\bcommand palette\b", "palet perintah"),

    # Common Verbs
    (r"\bcreate\b", "buat"),
    (r"\bcreating\b", "membuat"),
    (r"\bcreated\b", "dibuat"),
    (r"\bdelete\b", "hapus"),
    (r"\bdeleting\b", "menghapus"),
    (r"\bdeleted\b", "dihapus"),
    (r"\bremove\b", "hapus"),
    (r"\bremoving\b", "menghapus"),
    (r"\bremoved\b", "dihapus"),
    (r"\bopen\b", "buka"),
    (r"\bopening\b", "membuka"),
    (r"\bopened\b", "dibuka"),
    (r"\bclose\b", "tutup"),
    (r"\bclosing\b", "menutup"),
    (r"\bclosed\b", "ditutup"),
    (r"\bsave\b", "simpan"),
    (r"\bsaving\b", "menyimpan"),
    (r"\bsaved\b", "tersimpan"),
    (r"\bshow\b", "tampilkan"),
    (r"\bshowing\b", "menampilkan"),
    (r"\bshown\b", "ditampilkan"),
    (r"\bhide\b", "sembunyikan"),
    (r"\bhiding\b", "menyembunyikan"),
    (r"\bhidden\b", "tersembunyi"),
    (r"\benable\b", "aktifkan"),
    (r"\benabling\b", "mengaktifkan"),
    (r"\benabled\b", "diaktifkan"),
    (r"\bdisable\b", "nonaktifkan"),
    (r"\bdisabling\b", "menonaktifkan"),
    (r"\bdisabled\b", "dinonaktifkan"),
    (r"\bselect\b", "pilih"),
    (r"\bselecting\b", "memilih"),
    (r"\bselected\b", "terpilih"),
    (r"\bsearch\b", "cari"),
    (r"\bsearching\b", "mencari"),
    (r"\bfind\b", "cari"),
    (r"\breplace\b", "ganti"),
    (r"\breplacing\b", "mengganti"),
    (r"\breplaced\b", "diganti"),
    (r"\binstall\b", "pasang"),
    (r"\binstalling\b", "memasang"),
    (r"\binstalled\b", "terpasang"),
    (r"\buninstall\b", "copot"),
    (r"\buninstalling\b", "mencopot"),
    (r"\buninstalled\b", "dicopot"),
    (r"\bupdate\b", "perbarui"),
    (r"\bupdating\b", "memperbarui"),
    (r"\bupdated\b", "diperbarui"),
    (r"\breload\b", "muat ulang"),
    (r"\breloading\b", "memuat ulang"),
    (r"\breloaded\b", "dimuat ulang"),
    (r"\brestart\b", "mulai ulang"),
    (r"\brestarting\b", "memulai ulang"),
    (r"\brestarted\b", "dimulai ulang"),
    (r"\brun\b", "jalankan"),
    (r"\brunning\b", "berjalan"),
    (r"\bstart\b", "mulai"),
    (r"\bstarting\b", "memulai"),
    (r"\bstarted\b", "dimulai"),
    (r"\bstop\b", "hentikan"),
    (r"\bstopping\b", "menghentikan"),
    (r"\bstopped\b", "dihentikan"),
    (r"\bcancel\b", "batalkan"),
    (r"\bcanceling\b", "membatalkan"),
    (r"\bcancelled\b", "dibatalkan"),
    (r"\bclear\b", "bersihkan"),
    (r"\bclearing\b", "membersihkan"),
    (r"\bcleared\b", "dibersihkan"),
    (r"\breset\b", "atur ulang"),
    (r"\bresetting\b", "mengatur ulang"),
    (r"\bconfigure\b", "konfigurasikan"),
    (r"\bconfiguring\b", "mengonfigurasi"),
    (r"\bconfigured\b", "dikonfigurasi"),
    (r"\bmanage\b", "kelola"),
    (r"\bmanaging\b", "mengelola"),
    (r"\bmanaged\b", "dikelola"),
    (r"\bapply\b", "terapkan"),
    (r"\bapplying\b", "menerapkan"),
    (r"\bapplied\b", "diterapkan"),
    (r"\brevert\b", "kembalikan"),
    (r"\breverting\b", "mengembalikan"),
    (r"\breverted\b", "dikembalikan"),
    (r"\bundo\b", "urungkan"),
    (r"\bredo\b", "ulangi"),
    (r"\bcopy\b", "salin"),
    (r"\bcopying\b", "menyalin"),
    (r"\bcopied\b", "disalin"),
    (r"\bpaste\b", "tempel"),
    (r"\bpasting\b", "menempelkan"),
    (r"\bpasted\b", "ditempelkan"),
    (r"\bcut\b", "potong"),
    (r"\bcutting\b", "memotong"),
    (r"\bformat\b", "format"),
    (r"\bformatting\b", "memformat"),
    (r"\bformatted\b", "diformat"),
    (r"\brefactor\b", "refaktor"),
    (r"\brefactoring\b", "merefaktor"),
    (r"\bexpand\b", "bentangkan"),
    (r"\bexpanding\b", "membentangkan"),
    (r"\bexpanded\b", "dibentangkan"),
    (r"\bcollapse\b", "ciutkan"),
    (r"\bcollapsing\b", "menciutkan"),
    (r"\bcollapsed\b", "diciutkan"),
    (r"\bdiscard\b", "buang"),
    (r"\bdiscarding\b", "membuang"),
    (r"\bdiscarded\b", "dibuang"),
    (r"\brename\b", "ganti nama"),
    (r"\brenaming\b", "mengganti nama"),
    (r"\brenamed\b", "diganti nama"),
    (r"\bduplicate\b", "duplikasikan"),
    (r"\bduplicating\b", "menduplikasikan"),
    (r"\bduplicated\b", "diduplikasikan")
]

# 5. PEMBERSIHAN FRASA HYBRID RUSAK
CONTAMINATED_CLEANUPS = [
    (r"Buka Wor&&kspace from berkas\.\.\.", "Buka Ruang &&Kerja dari Berkas..."),
    (r"Buka Workspace from berkas\.\.\.", "Buka Ruang Kerja dari Berkas..."),
    (r"Buka Recent\.\.\.", "Buka Terkini..."),
    (r"Buka Recent", "Buka Terkini"),
    (r"Simpan As\.\.\.", "Simpan Sebagai..."),
    (r"Simpan All", "Simpan Semua"),
    (r"Tutup folder \[K F\]", "Tutup Folder"),
    (r"A&&dd Folder to Workspace\.\.\.", "&&Tambah Folder ke Ruang Kerja..."),
    (r"Move Chat into jendela baru", "Pindahkan Obrolan ke Jendela Baru"),
    (r"Move Chat into Editor Area", "Pindahkan Obrolan ke Area Editor"),
    (r"Tampilkan View by bawaan", "Tampilkan Tampilan secara Bawaan"),
    (r"Tampilkan Voice Transcripts", "Tampilkan Transkrip Suara"),
    (r"Tampilkan Agent Debug Logs", "Tampilkan Log Debug Agen"),
    (r"Pilih an aktif Copilot session and then open this Customizations menu again", "Pilih sesi Copilot yang aktif lalu buka kembali menu Kustomisasi ini"),
    (r"Cari MCP servers, plugins, skills and more\.\.\.", "Cari server MCP, plugin, keahlian, dan lainnya..."),
    (r"Salin into New jendela", "Salin ke Jendela Baru"),
    (r"Buka in New jendela", "Buka di Jendela Baru"),
    (r"into jendela baru", "ke Jendela Baru"),
    (r"in New jendela", "di Jendela Baru"),
    (r"into New jendela", "ke Jendela Baru"),
    (r"from berkas", "dari Berkas"),
    (r"into Area Editor", "ke Area Editor"),
    (r"Duplicate As Workspace in jendela baru", "Duplikasikan sebagai Ruang Kerja di Jendela Baru"),
    (r"Use your changes dan overwrite berkas contents", "Gunakan perubahan Anda dan timpa konten berkas"),
    (r"buang your changes dan kembalikan to berkas contents", "Buang perubahan Anda dan kembalikan ke konten berkas"),
    (r"Compare aktif berkas dengan tersimpan", "Bandingkan berkas aktif dengan yang tersimpan"),
    (r"Compare dengan tersimpan", "Bandingkan dengan yang tersimpan"),
    (r"Salin Path of aktif berkas", "Salin Jalur berkas aktif"),
    (r"Salin Relative Path of aktif berkas", "Salin Jalur Relatif berkas aktif"),
    (r"folder dengan Unsaved berkas", "Folder dengan Berkas Belum Disimpan"),
    (r"ruang kerja dengan Unsaved berkas", "Ruang Kerja dengan Berkas Belum Disimpan"),
    (r"Apakah Anda ingin buka the folder to review the unsaved berkas\?", "Apakah Anda ingin membuka folder untuk meninjau berkas yang belum disimpan?"),
    (r"Apakah Anda ingin buka the ruang kerja to review the unsaved berkas\?", "Apakah Anda ingin membuka ruang kerja untuk meninjau berkas yang belum disimpan?"),
    (r"Confirm Before tutup", "Konfirmasi Sebelum Menutup"),
    (r"Quick buka terkini\.\.\.", "Buka Terkini Cepat..."),
    (r"folder dibuka in aktif jendela", "Folder dibuka di jendela aktif"),
    (r"ruang kerja dibuka in aktif jendela", "Ruang kerja dibuka di jendela aktif"),
    (r"folder dibuka in a jendela", "Folder dibuka di sebuah jendela"),
    (r"ruang kerja dibuka in a jendela", "Ruang kerja dibuka di sebuah jendela"),
    (r"buka to the Side", "Buka di Samping"),
    (r"Tutup All", "Tutup Semua"),
    (r"Hapus Permanently", "Hapus Secara Permanen"),
    (r"permanently hapus", "menghapus permanen"),
    (r"muat ulang jendela", "Muat Ulang Jendela"),
    (r"Alihkan Auto simpan", "Alihkan Simpan Otomatis"),
    (r"Buat a new folder atau direktori", "Buat folder atau direktori baru"),
    (r"Your changes will be lost if you don't simpan them\.", "Perubahan Anda akan hilang jika tidak disimpan."),
    (r"A berkas atau folder name must be provided\.", "Nama berkas atau folder harus diisi."),
    (r"A berkas atau folder \*\*\{0\}\*\* already exists at this location\. Please choose a different name\.", "Berkas atau folder **{0}** sudah ada di lokasi ini. Silakan pilih nama lain."),
    (r"A berkas atau folder name cannot mulai dengan a slash\.", "Nama berkas atau folder tidak boleh diawali dengan garis miring."),
    (r"The name \*\*\{0\}\*\* is not valid as a berkas atau folder name\. Please choose a different name\.", "Nama **{0}** tidak valid sebagai nama berkas atau folder. Silakan pilih nama lain."),
    (r"pilih to buka \(hold Ctrl-key to force new jendela atau Alt-key untuk same jendela\)", "Pilih untuk membuka (tahan tombol Ctrl untuk membuka di jendela baru atau tombol Alt untuk jendela yang sama)"),
    (r"pilih to buka \(hold Cmd-key to force new jendela atau Option-key untuk same jendela\)", "Pilih untuk membuka (tahan tombol Cmd untuk membuka di jendela baru atau tombol Option untuk jendela yang sama)"),
    (r"Folder dengan Berkas Belum Disimpan cannot be dihapus until all unsaved berkas have been tersimpan atau dikembalikan\.", "Folder yang berisi berkas belum disimpan tidak dapat dihapus sampai semua berkas disimpan atau dikembalikan."),
    (r"Ruang Kerja dengan Berkas Belum Disimpan cannot be dihapus until all unsaved berkas have been tersimpan atau dikembalikan\.", "Ruang kerja yang berisi berkas belum disimpan tidak dapat dihapus sampai semua berkas disimpan atau dikembalikan.")
]

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

def clean_contaminated(text: str) -> str:
    for pat, rep in CONTAMINATED_CLEANUPS:
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)
    return text

def translate_string(src: str) -> str:
    if not src or not src.strip():
        return src

    if re.match(r"^[\s\{\}0-9\(\)\:\,\.\-\_\"\'\%\$\/\\]+$", src):
        return src

    has_double_amp = "&&" in src
    has_single_amp = src.startswith("&") and not has_double_amp

    clean_src = src.replace("&&", "").lstrip("&").strip()

    # 1. Cek Kamus Mnemonik Persis
    if clean_src in MNEMONIC_MAP and (has_double_amp or has_single_amp):
        return MNEMONIC_MAP[clean_src]

    # 2. Cek Kamus Frasa UI Persis
    if clean_src in EXACT_PHRASES:
        id_val = EXACT_PHRASES[clean_src]
        if has_double_amp:
            return "&&" + id_val
        elif has_single_amp:
            return "&" + id_val
        return id_val

    if src in EXACT_PHRASES:
        return EXACT_PHRASES[src]

    # Lindungi parameter dan token format
    protected_text, tokens = protect_tokens(clean_src)

    # 3. Pola Kalimat / Grammar Setting & Notifikasi
    matched_pattern = False
    for pat, rep in PATTERNS:
        if re.search(pat, protected_text, re.IGNORECASE):
            protected_text = re.sub(pat, rep, protected_text, flags=re.IGNORECASE)
            matched_pattern = True
            break

    # 4. Penggantian Kata Teknis & Frasa
    for en_pat, id_word in WORD_REPLACEMENTS:
        pattern = en_pat if en_pat.startswith(r"\b") else r"\b" + re.escape(en_pat) + r"\b"
        protected_text = re.sub(pattern, id_word, protected_text, flags=re.IGNORECASE)

    result = restore_tokens(protected_text, tokens)
    result = clean_contaminated(result)

    if has_double_amp and not ("&&" in result):
        result = "&&" + result

    return result

def main():
    print("=== Membangun Terjemahan Lengkap VS Code & Antigravity IDE ===")
    
    meta_path = "/Applications/Visual Studio Code.app/Contents/Resources/app/out/nls.metadata.json"
    if not os.path.exists(meta_path):
        print(f"❌ Error: {meta_path} tidak ditemukan!")
        sys.exit(1)

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    local_main_path = "translations/main.i18n.json"

    print(f"1. Memproses {len(meta['keys'])} modul inti VS Code...")
    new_contents = {}
    total_strings = 0

    for mod_name, keys in meta["keys"].items():
        msgs = meta["messages"].get(mod_name, [])
        mod_dict = {}

        for k, en_msg in zip(keys, msgs):
            k_str = k["key"] if isinstance(k, dict) else k
            total_strings += 1
            mod_dict[k_str] = translate_string(en_msg)

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

    print(f"2. Menyimpan {total_strings:,} string inti ke {local_main_path}...")
    with open(local_main_path, "w", encoding="utf-8") as f:
        json.dump(final_main, f, indent=2, ensure_ascii=False)

    print(f"   • Total Modul: {len(new_contents):,}")
    print(f"   • Total String: {total_strings:,}")

    # 3. Memproses 92 Ekstensi Bawaan VS Code
    print("\n3. Memproses seluruh ekstensi bawaan VS Code...")
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

    print(f"   • Berhasil memproses {ext_count} ekstensi bawaan ({ext_string_count:,} string).")

    # 4. Memperbarui package.json
    print("\n4. Memperbarui package.json...")
    with open("package.json", "r", encoding="utf-8") as f:
        pkg = json.load(f)

    pkg["version"] = "1.144.2"
    pkg["contributes"]["localizations"] = [
        {
            "languageId": "id",
            "languageName": "Indonesian",
            "localizedLanguageName": "Bahasa Indonesia",
            "translations": registered_translations
        }
    ]

    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)

    print("✅ GENERASI TERJEMAHAN LENGKAP SELESAI DENGAN SUKSES!")

if __name__ == "__main__":
    main()
