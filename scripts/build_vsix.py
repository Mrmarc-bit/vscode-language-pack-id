#!/usr/bin/env python3
"""
Membangun berkas paket .vsix secara mandiri dengan spesifikasi resmi Microsoft Visual Studio Marketplace (OPC / Open Packaging Conventions).
Kompatibel 100% dengan standar parser Azure DevOps / Visual Studio Marketplace.
"""

import os
import sys
import json
import zipfile

def build_vsix():
    current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    pkg_path = os.path.join(current_dir, "package.json")
    
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)

    publisher = pkg.get("publisher", "MarufMuchlisin")
    name = pkg.get("name", "vscode-language-pack-id")
    version = pkg.get("version", "1.144.2")
    display_name = pkg.get("displayName", "Indonesian Language Pack for Visual Studio Code")
    description = pkg.get("description", "Paket Bahasa Indonesia resmi dan modern untuk Visual Studio Code")
    engine = pkg.get("engines", {}).get("vscode", "^1.80.0")
    homepage = pkg.get("homepage", "https://github.com/Mrmarc-bit/vscode-language-pack-id#readme")
    repo_url = pkg.get("repository", {}).get("url", "https://github.com/Mrmarc-bit/vscode-language-pack-id")
    bugs_url = pkg.get("bugs", {}).get("url", "https://github.com/Mrmarc-bit/vscode-language-pack-id/issues")

    vsix_filename = f"{name}-{version}.vsix"
    vsix_filepath = os.path.join(current_dir, vsix_filename)

    print(f"=== Membangun Paket VSIX Standar Resmi Marketplace: {vsix_filename} ===")

    # 1. Buat [Content_Types].xml resmi OPC
    content_types_xml = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension=".vsixmanifest" ContentType="text/xml"/>
  <Default Extension=".json" ContentType="application/json"/>
  <Default Extension=".png" ContentType="image/png"/>
  <Default Extension=".md" ContentType="text/markdown"/>
  <Default Extension=".txt" ContentType="text/plain"/>
</Types>"""

    # 2. Buat extension.vsixmanifest resmi Microsoft VS Code Marketplace
    vsixmanifest_xml = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="{name}" Version="{version}" Publisher="{publisher}"/>
    <DisplayName>{display_name}</DisplayName>
    <Description xml:space="preserve">{description}</Description>
    <Tags>language-pack, i18n, indonesian, bahasa indonesia, terjemahan</Tags>
    <Categories>Language Packs</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{engine}" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value="" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value="" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="ui,workspace" />
      <Property Id="Microsoft.VisualStudio.Code.LocalizedLanguages" Value="id" />
      <Property Id="Microsoft.VisualStudio.Services.Links.Source" Value="{repo_url}" />
      <Property Id="Microsoft.VisualStudio.Services.Links.Getstarted" Value="{repo_url}" />
      <Property Id="Microsoft.VisualStudio.Services.Links.GitHub" Value="{repo_url}" />
      <Property Id="Microsoft.VisualStudio.Services.Links.Support" Value="{bugs_url}" />
      <Property Id="Microsoft.VisualStudio.Services.Links.Learn" Value="{homepage}" />
      <Property Id="Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown" Value="true" />
      <Property Id="Microsoft.VisualStudio.Services.Content.Pricing" Value="Free"/>
    </Properties>
    <License>extension/LICENSE</License>
    <Icon>extension/icon.png</Icon>
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

    # 3. Kumpulkan seluruh berkas
    files_to_pack = []
    
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
        for ef in sorted(os.listdir(ext_dir)):
            if ef.endswith(".json"):
                src = os.path.join(ext_dir, ef)
                files_to_pack.append((src, f"extension/translations/extensions/{ef}"))

    # 4. Tulis ke berkas arsip ZIP (VSIX)
    if os.path.exists(vsix_filepath):
        os.remove(vsix_filepath)

    with zipfile.ZipFile(vsix_filepath, "w", compression=zipfile.ZIP_DEFLATED) as z:
        # Tambahkan manifest dan content types di root arsip
        z.writestr("[Content_Types].xml", content_types_xml.strip())
        z.writestr("extension.vsixmanifest", vsixmanifest_xml.strip())

        # Tambahkan seluruh file isi ekstensi
        for src, arcname in files_to_pack:
            z.write(src, arcname)

    size_mb = os.path.getsize(vsix_filepath) / (1024 * 1024)
    print(f"✅ Paket VSIX Standar Marketplace berhasil dibuat: {vsix_filepath} ({size_mb:.2f} MB)")
    print(f"   Total berkas terkemas: {len(files_to_pack) + 2} berkas")
    print(f"   Publisher ID: {publisher}")
    print(f"   Versi: {version}")

if __name__ == "__main__":
    build_vsix()
