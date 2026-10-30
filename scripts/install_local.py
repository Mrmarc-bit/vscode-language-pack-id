#!/usr/bin/env python3
"""
Memasang ekstensi ini ke instalasi VS Code lokal untuk pengujian langsung (local preview).
Membuat tautan simbolik (symlink) di ~/.vscode/extensions/
"""

import os
import sys
import shutil
import platform

def main():
    home_dir = os.path.expanduser("~")
    current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    # Lokasi direktori ekstensi VS Code
    vscode_ext_dir = os.path.join(home_dir, ".vscode", "extensions")
    target_folder_name = "nusantara-dev.vscode-language-pack-id-1.0.0"
    target_path = os.path.join(vscode_ext_dir, target_folder_name)

    print("=== Pemasangan Ekstensi ke VS Code Lokal ===")
    print(f"Direktori Proyek: {current_dir}")
    print(f"Target VS Code Extensions: {target_path}")

    if not os.path.exists(vscode_ext_dir):
        print(f"Direktori {vscode_ext_dir} belum ada. Membuat direktori...")
        os.makedirs(vscode_ext_dir, exist_ok=True)

    # Jika sudah ada symlink atau folder sebelumnya, hapus dulu
    if os.path.islink(target_path) or os.path.exists(target_path):
        print(f"Menghapus instalasi sebelumnya di {target_path}...")
        if os.path.islink(target_path) or os.path.isfile(target_path):
            os.unlink(target_path)
        else:
            shutil.rmtree(target_path)

    # Buat symlink
    try:
        os.symlink(current_dir, target_path, target_is_directory=True)
        print("\n🎉 Berhasil menautkan ekstensi secara lokal!")
        print("\nLangkah selanjutnya untuk mengaktifkan:")
        print("1. Buka (atau restart jika sedang terbuka) aplikasi VS Code Anda.")
        print("2. Tekan pintasan Cmd+Shift+P (di Mac) atau Ctrl+Shift+P (di Windows/Linux).")
        print("3. Ketik perintah: 'Configure Display Language'.")
        print("4. Pilih 'Bahasa Indonesia' (Indonesian).")
        print("5. Klik 'Restart' ketika diminta oleh VS Code.")
        print("6. Selamat! Seluruh antarmuka VS Code Anda sekarang berbahasa Indonesia.")
    except Exception as e:
        print(f"❌ Gagal membuat symlink: {e}")
        print("Mencoba menyalin folder secara manual sebagai alternatif...")
        try:
            shutil.copytree(current_dir, target_path, ignore=shutil.ignore_patterns('.git', 'node_modules'))
            print("✅ Berhasil menyalin folder ke direktori ekstensi!")
        except Exception as copy_err:
            print(f"❌ Gagal menyalin: {copy_err}")
            sys.exit(1)

if __name__ == "__main__":
    main()
