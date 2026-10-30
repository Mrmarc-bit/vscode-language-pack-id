#!/usr/bin/env python3
"""
Script penerjemah otomatis dengan bantuan AI (Google Gemini / LLM).
Membaca 'translations/missing_translations.json', menerjemahkan modul per modul
dengan mematuhi 'GLOSSARY.md', lalu menggabungkan hasilnya ke 'translations/main.i18n.json'.

Penggunaan:
  export GEMINI_API_KEY="kunci-api-kamu"
  python3 scripts/translate_ai.py --limit-modules 5
"""

import os
import sys
import json
import argparse
import urllib.request

SYSTEM_PROMPT = """Kamu adalah penerjemah ahli antarmuka perangkat lunak untuk Visual Studio Code (Bahasa Inggris ke Bahasa Indonesia).
Tugasmu adalah menerjemahkan nilai teks antarmuka ke Bahasa Indonesia yang ramah bagi pemula, alami, dan baku sesuai standar industri teknologi di Indonesia.

ATURAN WAJIB:
1. JANGAN ubah key/kunci JSON sama sekali. Terjemahkan HANYA nilainya (values).
2. Parameter seperti {0}, {1}, %s, dll. HARUS tetap ada dengan urutan yang tepat.
3. Akses cepat (mnemonic) tombol dengan simbol '&' atau '&&' (seperti '&File' -> '&Berkas') harus dipertahankan.
4. Istilah teknis universal (Git Commit, Push, Pull, Branch, Debug, Terminal, Runtime, Framework, Regex, Breakpoint) tetap dipertahankan atau diberikan penjelas yang jelas.
5. Ikuti glosarium:
   - File -> Berkas
   - Folder / Directory -> Folder / Direktori
   - Save / Save As -> Simpan / Simpan Sebagai...
   - Settings / Preferences -> Pengaturan / Preferensi
   - Command Palette -> Palet Perintah
   - Explorer -> Penjelajah
   - Output -> Output / Keluaran
   - Problems -> Masalah
6. Kembalikan HANYA format JSON valid tanpa tanda markdown (```json ... ```).
"""

def call_gemini_api(api_key: str, prompt_text: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.2
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=60) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))
        candidate = res_data["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(candidate)

def main():
    parser = argparse.ArgumentParser(description="Penerjemah batch AI untuk VS Code Language Pack")
    parser.add_argument("--limit-modules", type=int, default=3, help="Jumlah modul yang akan diterjemahkan per eksekusi")
    parser.add_argument("--dry-run", action="store_true", help="Uji coba tanpa mengubah file main.i18n.json")
    args = parser.parse_args()

    missing_path = "translations/missing_translations.json"
    main_path = "translations/main.i18n.json"

    if not os.path.exists(missing_path):
        print("⚠️  Berkas missing_translations.json belum ada. Menjalankan sinkronisasi upstream terlebih dahulu...")
        os.system(f"{sys.executable} scripts/sync_upstream.py")

    with open(missing_path, "r", encoding="utf-8") as f:
        missing_data = json.load(f)

    with open(main_path, "r", encoding="utf-8") as f:
        main_data = json.load(f)

    if not missing_data:
        print("🎉 Luar biasa! Tidak ada string yang belum diterjemahkan.")
        return

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: Lingkungan variabel GEMINI_API_KEY belum disetel!")
        print("Contoh cara menyetelnya:")
        print("   export GEMINI_API_KEY='AIzaSy...'")
        print("   python3 scripts/translate_ai.py --limit-modules 5")
        sys.exit(1)

    modules_to_translate = list(missing_data.keys())[:args.limit_modules]
    print(f"Memproses {len(modules_to_translate)} modul teratas...")

    total_translated_keys = 0

    for idx, mod_name in enumerate(modules_to_translate):
        items = missing_data[mod_name]
        print(f"\n[{idx+1}/{len(modules_to_translate)}] Menerjemahkan modul: {mod_name} ({len(items)} string)...")

        prompt = f"Terjemahkan kamus string antarmuka VS Code berikut ke Bahasa Indonesia:\n{json.dumps(items, ensure_ascii=False, indent=2)}"
        
        try:
            translated_items = call_gemini_api(api_key, prompt)
            print(f"✅ Selesai ({len(translated_items)} string diterjemahkan).")
            
            if not args.dry_run:
                if "contents" not in main_data:
                    main_data["contents"] = {}
                if mod_name not in main_data["contents"]:
                    main_data["contents"][mod_name] = {}
                
                main_data["contents"][mod_name].update(translated_items)
                total_translated_keys += len(translated_items)
                
                # Hapus modul yang sudah diterjemahkan dari missing_data
                del missing_data[mod_name]
        except Exception as e:
            print(f"❌ Gagal menerjemahkan modul {mod_name}: {e}")

    if not args.dry_run and total_translated_keys > 0:
        print(f"\nMenyimpan perubahan ke {main_path}...")
        with open(main_path, "w", encoding="utf-8") as f:
            json.dump(main_data, f, ensure_ascii=False, indent=2)

        print(f"Memperbarui {missing_path}...")
        with open(missing_path, "w", encoding="utf-8") as f:
            json.dump(missing_data, f, ensure_ascii=False, indent=2)

        print(f"🎉 Sukses menambahkan {total_translated_keys} string terjemahan baru!")
        print("Jalankan 'python3 scripts/validate.py' untuk memeriksa integritas data.")

if __name__ == "__main__":
    main()

