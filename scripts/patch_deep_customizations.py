#!/usr/bin/env python3
"""
Patch mendalam untuk menerjemahkan seluruh antarmuka:
1. Menu Obrolan (Chat Popup Actions: Move Chat, Tool Sets, Chat Settings, Voice Transcripts, Debug Logs, dll)
2. Halaman Jelajahi Kustomisasi (Browse Customizations, Editor's Picks, Plan build & ship, Connect your work)
3. Halaman Kanvas (Canvases, session alerts, placeholders)
4. Halaman Server MCP (Start/Stop, User/Workspace/Built-In groups, deskripsi)
5. Halaman Plugin (Deskripsi, User/Workspace groups, Jelajahi)
"""

import os
import sys
import json

DEEP_PATCHES = {
    # 1. Chat Popup Menu Actions
    "vs/workbench/contrib/chat/browser/actions/chatActions": {
        "openChatFeatureSettings": "Pengaturan Obrolan",
        "openChatFeatureSettings.short": "Pengaturan Obrolan",
        "chat.toggleDefaultVisibility.label": "Tampilkan Tampilan secara Bawaan",
        "chat.showModelPicker": "Pilih Model Bahasa",
        "chat.manageCustomizations": "Kelola Kustomisasi",
        "chat.newChat": "Obrolan Baru",
        "chat.clearHistory": "Bersihkan Riwayat Obrolan"
    },
    "vs/workbench/contrib/chat/browser/actions/chatMoveActions": {
        "chat.openInEditor.label": "Pindahkan Obrolan ke Area Editor",
        "chat.openInNewWindow.label": "Pindahkan Obrolan ke Jendela Baru"
    },
    "vs/workbench/contrib/chat/browser/actions/chatNewActions": {
        "chat.undoEdit.label": "Urungkan Edit Terakhir",
        "chat.redoEdit.label": "Ulangi Edit Terakhir"
    },
    "vs/workbench/contrib/chat/browser/tools/toolSetsContribution": {
        "chat.configureToolSets.short": "Kumpulan Alat (Tool Sets)",
        "chat.configureToolSets": "Konfigurasikan Kumpulan Alat...",
        "chat.configureToolSets.add": "Buat berkas kumpulan alat baru..."
    },
    "vs/workbench/contrib/chat/browser/chatSlashCommands": {
        "debug": "Tampilkan Tampilan Debug Obrolan"
    },
    "vs/workbench/contrib/agentsVoice/browser/transcriptsView/voiceTranscripts.contribution": {
        "agentsVoice.showTranscripts": "Tampilkan Transkrip Suara",
        "agentsVoice.showTranscripts.menu": "Tampilkan Transkrip Suara",
        "voiceTranscriptsContainer": "Transkrip Suara",
        "voiceTranscriptsView": "Transkrip Suara"
    },
    "vs/workbench/contrib/chat/browser/actions/chatOpenAgentDebugPanelAction": {
        "chat.openAgentDebugPanel.label": "Buka Log Debug Agen",
        "chat.openAgentDebugPanelForSession.label": "Tampilkan Log Debug Agen"
    },

    # 2. Browse Customizations
    "vs/workbench/contrib/chat/browser/aiCustomization/aiCustomizationDiscoveryPage": {
        "customizationDiscovery.title": "Jelajahi kustomisasi",
        "customizationDiscovery.description": "Sesuaikan agen Anda dengan alat, tim, dan alur kerja Anda. [[Pelajari lebih lanjut]]",
        "customizationDiscovery.allSources": "Semua Sumber",
        "customizationDiscovery.accessibleAllSources": "Sumber: Semua Sumber",
        "customizationDiscovery.addCustomization": "Tambah Kustomisasi",
        "customizationDiscovery.addCustomizationLabel": "Tambah Kustomisasi",
        "customizationDiscovery.addMcp": "Tambah Server MCP",
        "customizationDiscovery.addPlugin": "Tambah Plugin",
        "customizationDiscovery.accessibleBrowse": "Mode Jelajah.",
        "customizationDiscovery.available": "Tersedia",
        "customizationDiscovery.editorsPicks": "Pilihan Editor",
        "customizationDiscovery.installedBadge": "Terpasang",
        "customizationDiscovery.installingBadge": "Memasang...",
        "customizationDiscovery.popularTitle": "Populer",
        "customizationDiscovery.recentTitle": "Terkini",
        "customizationDiscovery.recommendedTitle": "Disarankan",
        "customizationDiscovery.searchLabel": "Cari kustomisasi",
        "customizationDiscovery.searchPlaceholder": "Cari server MCP, plugin, keahlian, dan lainnya...",
        "customizationDiscovery.sourcesTitle": "Sumber",
        "customizationDiscovery.userSectionTitle": "Pengguna",
        "customizationDiscovery.workspaceSectionTitle": "Ruang Kerja"
    },
    "vs/workbench/contrib/chat/browser/aiCustomization/customizationMarketplaceWorkbenchService": {
        "customizationMarketplace.editorsPicks": "Pilihan Editor",
        "customizationMarketplace.planBuildAndShip": "Rencanakan, bangun, dan rilis",
        "customizationMarketplace.connectYourWork": "Hubungkan pekerjaan Anda"
    },

    # 3. Kanvas (Canvases)
    "vs/workbench/contrib/chat/browser/aiCustomization/copilotCustomizationsWidget": {
        "copilotCanvases.title": "Kanvas",
        "copilotCanvases.description": "Kanvas adalah permukaan visual interaktif yang dibagikan antara Anda dan agen.",
        "copilotCanvases.learnMore": "Pelajari lebih lanjut tentang kanvas",
        "copilotCanvases.search": "Ketik untuk mencari...",
        "copilotCanvases.noCompatibleChat": "Kanvas hanya tersedia di dalam sesi",
        "copilotCanvases.noCompatibleChatDescription": "Pilih sesi Copilot yang aktif lalu buka kembali menu Kustomisasi ini",
        "copilotCanvases.empty": "Tidak Ada Kanvas yang Tersedia",
        "copilotCanvases.emptyDescription": "Tidak ada obrolan Copilot saat ini yang menyediakan Kanvas apa pun.",
        "copilotCanvases.userGroup": "Pengguna",
        "copilotCanvases.workspaceGroup": "Ruang Kerja",
        "copilotCanvases.pluginGroup": "Plugin",
        "copilotCanvases.otherGroup": "Lainnya",
        "copilotCanvases.enabledStatus": "Diaktifkan",
        "copilotCanvases.disabledStatus": "Dinonaktifkan",
        "copilotCanvases.startingStatus": "Memulai"
    },

    # 4. Server MCP
    "vs/workbench/contrib/chat/browser/aiCustomization/mcpListWidget": {
        "mcpServers": "Server MCP",
        "mcpServersTitle": "Server MCP",
        "mcpServersDescription": "Standar terbuka yang memungkinkan AI menggunakan alat dan layanan eksternal. Server MCP menyediakan alat untuk operasi berkas, basis data, API, dan lainnya.",
        "learnMoreMcp": "Pelajari lebih lanjut tentang server MCP",
        "browseMcps": "Jelajahi",
        "browse": "Jelajahi",
        "addServer": "Tambah Server",
        "userMcpServersGroup": "Pengguna",
        "workspaceMcpServersGroup": "Ruang Kerja",
        "builtinMcpServersGroup": "Bawaan",
        "pluginMcpServersGroup": "Plugin",
        "extensionMcpServersGroup": "Ekstensi",
        "activeSessionMcpServerStart": "Mulai Server",
        "activeSessionMcpServerStop": "Hentikan Server",
        "startServer": "Mulai",
        "stopServer": "Hentikan",
        "user": "Pengguna",
        "workspace": "Ruang Kerja",
        "available": "Tersedia",
        "installed": "Terpasang",
        "installing": "Memasang...",
        "searchPlaceholder": "Ketik untuk mencari...",
        "mcpMigrationAvailable": "Migrasi tersedia"
    },

    # 5. Plugin
    "vs/workbench/contrib/chat/browser/aiCustomization/pluginListWidget": {
        "plugins": "Plugin",
        "pluginsTitle": "Plugin",
        "pluginsDescription": "Perluas agen AI Anda dengan plugin yang menambahkan perintah, keahlian, agen, kait, dan server MCP dari paket yang dapat digunakan kembali.",
        "learnMorePlugins": "Pelajari lebih lanjut tentang plugin agen",
        "browse": "Jelajahi",
        "userPluginsGroup": "Pengguna",
        "workspacePluginsGroup": "Ruang Kerja",
        "remotePluginsSection": "Sesi Jarak Jauh",
        "remotePluginSource": "Jarak Jauh",
        "remotePluginMetadata": "Host agen jarak jauh",
        "recommendedBadge": "Disarankan",
        "local": "Lokal",
        "localBadge": "Lokal",
        "searchPluginsPlaceholder": "Ketik untuk mencari...",
        "searchMarketplacePlaceholder": "Cari marketplace plugin..."
    },

    # 6. Sidebar Customizations / Sessions
    "vs/workbench/contrib/chat/browser/aiCustomization/aiCustomizationManagementEditor": {
        "browse": "Jelajahi",
        "migrationBrowse": "Jelajahi",
        "plugins": "Plugin",
        "canvases": "Kanvas",
        "mcp": "Server MCP",
        "mcpServers": "Server MCP",
        "skills": "Keahlian (Skills)",
        "instructions": "Instruksi",
        "agents": "Agen",
        "hooks": "Kait (Hooks)",
        "tools": "Alat",
        "migrations": "Migrasi",
        "models": "Model",
        "overview": "Ringkasan",
        "user": "Pengguna",
        "workspace": "Ruang Kerja",
        "userSaveTarget": "Pengguna",
        "workspaceSaveTarget": "Ruang Kerja"
    },

    # 7. Sesi & Bilah Navigasi
    "vs/sessions/contrib/sessions/browser/views/sessionsList": {
        "sessionsList": "Sesi",
        "chatsSection": "Obrolan",
        "automations": "Otomasi",
        "customizations": "Kustomisasi",
        "newSession": "Sesi Baru",
        "recent": "Terkini",
        "pinned": "Disematkan",
        "older": "Lebih Lama"
    }
}

def main():
    print("=== Menerapkan Patch Terjemahan Mendalam Antigravity & Copilot ===")
    main_i18n_path = "translations/main.i18n.json"

    with open(main_i18n_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    contents = data.get("contents", {})
    total_patched = 0

    for mod, patch_dict in DEEP_PATCHES.items():
        if mod not in contents:
            contents[mod] = {}
        contents[mod].update(patch_dict)
        total_patched += len(patch_dict)
        print(f"✅ Diperbarui modul: {mod} ({len(patch_dict)} kunci)")

    with open(main_i18n_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Berhasil menambal {total_patched} kunci terjemahan ke translations/main.i18n.json!")

if __name__ == "__main__":
    main()

