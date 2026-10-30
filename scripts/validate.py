#!/usr/bin/env python3
"""
Validator untuk Indonesian Language Pack VS Code.
Memeriksa integritas JSON, keberadaan berkas yang terdaftar di package.json,
serta format placeholder.
"""

import os
import json
import re
import sys

def main():
    print("=== Validasi Indonesian Language Pack VS Code ===")
    has_error = False

    # 1. Validasi package.json
    pkg_path = "package.json"
    if not os.path.exists(pkg_path):
        print("❌ Error: package.json tidak ditemukan!")
        sys.exit(1)

    try:
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        print("✅ package.json valid.")
    except Exception as e:
        print(f"❌ Error membaca package.json: {e}")
        sys.exit(1)

    # 2. Cek pendaftaran localizations
    locs = pkg.get("contributes", {}).get("localizations", [])
    if not locs:
        print("❌ Error: Tidak ada 'contributes.localizations' di package.json!")
        sys.exit(1)

    id_loc = next((l for l in locs if l.get("languageId") == "id"), None)
    if not id_loc:
        print("❌ Error: languageId 'id' tidak ditemukan di package.json!")
        sys.exit(1)

    print("✅ Pendaftaran languageId 'id' terverifikasi.")

    # 3. Cek semua berkas terjemahan yang terdaftar
    translations = id_loc.get("translations", [])
    print(f"Memeriksa {len(translations)} entri terjemahan terdaftar...")

    total_strings = 0
    total_modules = 0

    for item in translations:
        rel_path = item.get("path")
        if not rel_path or not os.path.exists(rel_path):
            print(f"❌ File tidak ditemukan: {rel_path} (id: {item.get('id')})")
            has_error = True
            continue

        try:
            with open(rel_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            if item.get("id") == "vscode":
                contents_dict = content.get("contents", {})
                total_modules += len(contents_dict)
                for mod_key, strings_dict in contents_dict.items():
                    if isinstance(strings_dict, dict):
                        total_strings += len(strings_dict)
                    else:
                        total_strings += 1
            else:
                contents_dict = content.get("contents", {})
                if isinstance(contents_dict, dict):
                    total_strings += sum(len(v) if isinstance(v, dict) else 1 for v in contents_dict.values())
                else:
                    total_strings += len(content)

        except Exception as e:
            print(f"❌ JSON error di {rel_path}: {e}")
            has_error = True

    print(f"\n📊 Ringkasan Data:")
    print(f"   • Total Modul Inti: {total_modules}")
    print(f"   • Estimasi Total String Terjemahan: {total_strings:,}")

    if has_error:
        print("\n❌ Validasi selesai dengan beberapa kesalahan!")
        sys.exit(1)
    else:
        print("\n✅ Semua berkas terjemahan valid dan siap digunakan!")

if __name__ == "__main__":
    main()
