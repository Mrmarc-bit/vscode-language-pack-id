#!/usr/bin/env python3
"""
Membangun berkas paket .vsix secara mandiri menggunakan modul zipfile Python standar.
Menghasilkan berkas .vsix siap pasang tanpa memerlukan dependensi npm/vsce.
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET

def build_vsix():
    current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    pkg_path = os.path.join(current_dir, "package.json")
    
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)

    publisher = pkg.get("publisher", "mrmarc")
    name = pkg.get("name", "vscode-language-pack-id")
    version = pkg.get("version", "1.144.0")
    display_name = pkg.get("displayName", "Indonesian Language Pack for Visual Studio Code")
    description = pkg.get("description", "Paket Bahasa Indonesia untuk Visual Studio Code")

    vsix_filename = f"{name}-{version}.vsix"
    vsix_filepath = os.path.join(current_dir, vsix_filename)

    print(f"=== Membangun Paket VSIX: {vsix_filename} ===")

    # 1. Buat [Content_Types].xml
    content_types_xml = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openformats.org/package/2006/content-types">
  <Default Extension="vsixmanifest" ContentType="text/xml"/>
  <Default Extension="json" ContentType="application/json"/>
  <Default Extension="png" ContentType="image/png"/>
  <Default Extension="md" ContentType="text/markdown"/>
  <Default Extension="txt" ContentType="text/plain"/>
</Types>"""

    # 2. Buat extension.vsixmanifest
    vsixmanifest_xml = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Id="{name}" Version="{version}" Language="en-US" Publisher="{publisher}"/>
    <DisplayName>{display_name}</DisplayName>
    <Description xml:space="preserve">{description}</Description>
    <Tags>language-pack, i18n, indonesian, bahasa indonesia</Tags>
    <Categories>Language Packs</Categories>
    <Icon>extension/icon.png</Icon>
    <License>extension/LICENSE</License>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="extension/icon.png" Addressable="true"/>
  </Assets>
</PackageManifest>"""

    # 3. Kumpulkan semua berkas yang akan dimasukkan ke dalam arsip
    files_to_pack = []
    
    # Berkas di root extension/
    root_files = ["package.json", "README.md", "LICENSE", "icon.png", "GLOSSARY.md"]
    for rf in root_files:
        src = os.path.join(current_dir, rf)
        if os.path.exists(src):
            files_to_pack.append((src, f"extension/{rf}"))

    # translations/main.i18n.json
    main_i18n = os.path.join(current_dir, "translations", "main.i18n.json")
    if os.path.exists(main_i18n):
        files_to_pack.append((main_i18n, "extension/translations/main.i18n.json"))

    # translations/extensions/*.i18n.json
    ext_dir = os.path.join(current_dir, "translations", "extensions")
    if os.path.exists(ext_dir):
        for fn in sorted(os.listdir(ext_dir)):
            if fn.endswith(".i18n.json"):
                src = os.path.join(ext_dir, fn)
                files_to_pack.append((src, f"extension/translations/extensions/{fn}"))

    # Buat berkas ZIP / VSIX
    if os.path.exists(vsix_filepath):
        os.remove(vsix_filepath)

    with zipfile.ZipFile(vsix_filepath, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml.strip())
        zf.writestr("extension.vsixmanifest", vsixmanifest_xml.strip())
        
        for src, arcname in files_to_pack:
            zf.write(src, arcname)

    size_mb = os.path.getsize(vsix_filepath) / (1024 * 1024)
    print(f"✅ Paket VSIX berhasil dibuat: {vsix_filepath} ({size_mb:.2f} MB)")
    print(f"   Total berkas dikemas: {len(files_to_pack) + 2} berkas")
    print("\nCara memasang ke VS Code / Antigravity:")
    print("1. Buka menu Extensions (Cmd + Shift + X).")
    print("2. Klik ikon '...' (Views and More Actions) di pojok kanan atas panel Extensions.")
    print("3. Pilih 'Install from VSIX...' (Pasang dari VSIX...).")
    print(f"4. Pilih berkas: {vsix_filepath}")
    print("5. Restart editor saat muncul notifikasi konfirmasi.")

if __name__ == "__main__":
    build_vsix()

