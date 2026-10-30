#!/usr/bin/env python3
"""
Script sinkronisasi dengan upstream (microsoft/vscode-loc).
Mendeteksi kunci dan string baru di VS Code modern yang belum diterjemahkan ke Bahasa Indonesia,
menghitung persentase progres, dan mengekspor daftar teks yang belum diterjemahkan.
"""

import os
import json
import urllib.request
import sys

UPSTREAM_URL = "https://raw.githubusercontent.com/microsoft/vscode-loc/main/i18n/vscode-language-pack-es/translations/main.i18n.json"

def main():
    print("=== Pengecekan Kunci Terbaru VS Code Upstream ===")
    local_main_path = "translations/main.i18n.json"
    
    if not os.path.exists(local_main_path):
        print(f"❌ Error: {local_main_path} tidak ditemukan!")
        sys.exit(1)

    print("1. Membaca terjemahan lokal Bahasa Indonesia...")
    with open(local_main_path, "r", encoding="utf-8") as f:
        local_data = json.load(f)
    local_contents = local_data.get("contents", {})

    print("2. Mengunduh data referensi terbaru dari upstream (microsoft/vscode-loc)...")
    try:
        req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            upstream_data = json.loads(resp.read().decode("utf-8"))
        upstream_contents = upstream_data.get("contents", {})
    except Exception as e:
        print(f"❌ Gagal mengunduh referensi upstream: {e}")
        sys.exit(1)

    print("3. Menganalisis perbedaan kunci string...")
    total_upstream_strings = 0
    total_local_strings = 0
    missing_strings_count = 0
    missing_data = {}

    for mod_name, mod_strings in upstream_contents.items():
        if not isinstance(mod_strings, dict):
            continue
        
        local_mod = local_contents.get(mod_name, {})
        for str_key, upstream_val in mod_strings.items():
            total_upstream_strings += 1
            if str_key in local_mod:
                total_local_strings += 1
            else:
                missing_strings_count += 1
                if mod_name not in missing_data:
                    missing_data[mod_name] = {}
                # Simpan teks referensi (atau key jika itu teksnya)
                missing_data[mod_name][str_key] = upstream_val

    pct = (total_local_strings / total_upstream_strings * 100) if total_upstream_strings > 0 else 0

    print("\n📊 HASIL ANALISIS TERJEMAHAN VS CODE:")
    print("--------------------------------------------------")
    print(f"Total string di VS Code versi terbaru : {total_upstream_strings:,}")
    print(f"Total string sudah diterjemahkan (ID) : {total_local_strings:,}")
    print(f"Total string belum diterjemahkan      : {missing_strings_count:,}")
    print(f"Tingkat kelengkapan terjemahan        : {pct:.2f}%")
    print("--------------------------------------------------")

    # Simpan missing translations jika ada
    output_missing_path = "translations/missing_translations.json"
    with open(output_missing_path, "w", encoding="utf-8") as f:
        json.dump(missing_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Daftar string yang belum diterjemahkan disimpan di: {output_missing_path}")
    print("   Gunakan file ini sebagai masukan untuk script penerjemahan otomatis AI!")

if __name__ == "__main__":
    main()
