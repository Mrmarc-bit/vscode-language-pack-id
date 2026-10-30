#!/usr/bin/env python3
"""
Memasang ekstensi ini ke instalasi VS Code / Antigravity lokal untuk pengujian langsung (local preview).
Membuat tautan simbolik (symlink) atau menyalin ke direktori ekstensi editor.
"""

import os
import sys
import json
import shutil

def main():
    home_dir = os.path.expanduser("~")
    current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    # Baca publisher, nama, dan versi dari package.json
    pkg_path = os.path.join(current_dir, "package.json")
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)
    
    publisher = pkg.get("publisher", "MarufMuchlisin")
    name = pkg.get("name", "indonesian-language-pack")
    version = pkg.get("version", "1.144.0")
    target_folder_name = f"{publisher}.{name}-{version}"

    print("=== Pemasangan Indonesian Language Pack ke Editor Lokal ===")
    print(f"Direktori Sumber : {current_dir}")
    print(f"ID Folder        : {target_folder_name}")

    # Daftar target direktori ekstensi yang mungkin digunakan VS Code atau Antigravity
    target_ext_dirs = [
        os.path.join(home_dir, ".vscode", "extensions"),
        os.path.join(home_dir, ".antigravity", "extensions"),
        os.path.join(home_dir, ".gemini", "antigravity", "extensions"),
        os.path.join(home_dir, "Library", "Application Support", "Code", "extensions"),
        os.path.join(home_dir, "Library", "Application Support", "Antigravity", "extensions")
    ]

    installed_paths = []

    for ext_dir in target_ext_dirs:
        try:
            os.makedirs(ext_dir, exist_ok=True)
            target_path = os.path.join(ext_dir, target_folder_name)

            if os.path.islink(target_path) or os.path.exists(target_path):
                if os.path.islink(target_path) or os.path.isfile(target_path):
                    os.unlink(target_path)
                else:
                    shutil.rmtree(target_path)

            try:
                os.symlink(current_dir, target_path, target_is_directory=True)
                installed_paths.append(target_path)
            except Exception:
                shutil.copytree(current_dir, target_path, ignore=shutil.ignore_patterns('.git', 'node_modules', '*.vsix'))
                installed_paths.append(target_path)
        except Exception:
            pass

    if installed_paths:
        print("\n🎉 Berhasil memasang ekstensi ke direktori berikut:")
        for p in installed_paths:
            print(f"   • {p}")

        print("\n-------------------------------------------------------------")
        print("LANGKAH MENGAKTIFKAN BAHASA INDONESIA:")
        print("1. TUTUP SEPENUHNYA aplikasi VS Code / Antigravity (Cmd + Q).")
        print("2. Buka kembali VS Code / Antigravity.")
        print("3. Tekan pintasan Cmd + Shift + P.")
        print("4. Ketik: 'Configure Display Language' lalu tekan Enter.")
        print("5. Pilih 'Bahasa Indonesia' (Indonesian).")
        print("6. Klik 'Restart'.")
        print("-------------------------------------------------------------")
    else:
        print("❌ Gagal memasang otomatis. Silakan gunakan metode VSIX!")

if __name__ == "__main__":
    main()
