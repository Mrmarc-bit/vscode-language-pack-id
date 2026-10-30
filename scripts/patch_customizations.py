#!/usr/bin/env python3
"""
Patch khusus untuk halaman Agent Customizations, Migrations, dan AI Tools Antigravity.
Menerjemahkan seluruh antarmuka 'Keep your customizations working', kartu migrasi,
peringatan prompt-to-skill, server MCP, partisipan obrolan, dan sidebar kustomisasi.
"""

import os
import sys
import json

MIGRATION_DASHBOARD_PATCH = {
    "agentMigrationRecoveries": "Pemulihan Migrasi Agen",
    "agentMigrationRecoveriesDescription": "Pulihkan sumber kustomisasi asli dari sebelum migrasi agen. Berkas tujuan yang dibuat atau diubah oleh agen tidak akan dihapus.",
    "backToMigrations": "Kembali ke migrasi",
    "changeMigrationDestinations": "Ubah tujuan untuk {0}",
    "chatParticipantMigrationManualReviewGuidance": "Tanyakan kepada penerbit ekstensi apakah menyediakan plugin agen, server MCP, atau alat ekstensi. Gunakan agen kustom ketika integrasi memerlukan peran spesialis berkelanjutan.",
    "chatParticipantMigrationManualReviewReason": "Partisipan obrolan sudah usang dan tidak didukung oleh runtime Copilot.",
    "deleteAgentMigrationRecovery": "Hapus Cadangan",
    "deleteAgentMigrationRecoveryAriaLabel": "Hapus cadangan untuk {0}",
    "extensionToolSetMigrationManualReviewGuidance": "Minta penerbit ekstensi untuk mengganti kumpulan alat ini dengan alat yang didukung, agen kustom, atau plugin agen.",
    "highRiskMigrationDescription": "Risiko tinggi",
    "ignoreMigrationCategory": "Abaikan {0}",
    "ignoreMigrationGroup": "Abaikan",
    "learnAboutMigrations": "Pelajari Tentang Migrasi",
    "learnHowToReplaceChatParticipants": "Pelajari cara mengganti partisipan obrolan",
    "learnHowToReplaceToolSets": "Pelajari cara mengganti kumpulan alat",
    "manualReviewItemHover": "{0}\n\n{1}",
    "migrate": "Migrasikan...",
    "migrateWithAgent": "Migrasikan dengan Agen",
    "migrateWithAgentAriaLabel": "Mulai migrasi terpandu untuk semua berkas kustomisasi yang memerlukan migrasi",
    "migrateWithAgentDescription": "Buka obrolan baru dengan agen untuk meninjau dan memigrasikan kustomisasi Anda. Ini menggunakan kredit Copilot.",
    "migrationAccessibleActionWithLabel": "{0}: {1}",
    "migrationAccessibleGuidanceLink": "{0}: {1}",
    "migrationActionSelectedCount": "Migrasikan {0}...",
    "migrationActionWithScope": "{0} ({1})",
    "migrationDestinationPath": "Tujuan: {0}",
    "migrationExtensionsScope": "Ekstensi",
    "migrationGroupAriaLabel": "{0}, {1} migrasi",
    "migrationGroupWithScope": "{0} ({1})",
    "migrationGuidanceSourceWithValue": "Sumber: {0}",
    "migrationItemActions": "Tindakan lainnya untuk {0}",
    "migrationItemAriaLabel": "{0}, {1}, sumber {2}",
    "migrationItemWithChangesAriaLabel": "{0}, {1}, sumber {2}. Perubahan migrasi: {3}",
    "migrationItemWithStatusAriaLabel": "{0}, perlu peninjauan manual, {1}, {2}, sumber {3}",
    "migrationLearnMore": "Pelajari Lebih Lanjut",
    "migrationLearnMoreAriaLabel": "Pelajari cara memigrasikan {0}",
    "migrationManualReviewGroup": "Perlu peninjauan manual",
    "migrationManualReviewGroupDescription": "Kustomisasi ini tidak dapat dimigrasikan secara otomatis. Pilih Tinjau untuk melihat hal yang perlu diubah.",
    "migrationsCompletedDescription": "Kustomisasi Anda siap digunakan.",
    "migrationsDescription": "Runtime agen baru Copilot menggunakan format dan lokasi berbeda untuk beberapa kustomisasi. Tinjau dan migrasikan item yang terpengaruh di bawah ini.",
    "migrationsGuidanceDescription": "Kustomisasi ini tidak dapat dimigrasikan secara otomatis. Gunakan Pelajari Lebih Lanjut untuk panduan memperbaruinya.",
    "migrationsTitle": "Migrasi",
    "migrationsWelcomeTitle": "Pastikan kustomisasi Anda tetap berfungsi",
    "migrationTreeAriaLabel": "Migrasi kustomisasi",
    "migrationUserScope": "Pengguna",
    "migrationWorkspaceScope": "Ruang Kerja",
    "moreActions": "Tindakan Lainnya",
    "noActiveMigrations": "Tidak ada migrasi aktif. Pulihkan migrasi yang diabaikan untuk meninjaunya.",
    "noMigrations": "Tidak ada migrasi yang diperlukan.",
    "openGuidanceSourceFile": "Buka {0}",
    "promptMigrationWarningSummary": "Perubahan konversi prompt ke keahlian (skill)",
    "replaceChatParticipant": "Ganti Partisipan Obrolan",
    "replaceToolSet": "Ganti Kumpulan Alat",
    "restoreAgentMigrationSources": "Pulihkan Sumber",
    "restoreAgentMigrationSourcesAriaLabel": "Pulihkan sumber asli untuk {0}",
    "retry": "Coba Lagi",
    "retryMigrationCategory": "Coba lagi memuat {0}",
    "retryMigrations": "Coba lagi memuat migrasi",
    "reviewMigrationItem": "Tinjau",
    "reviewMigrationItemAriaLabel": "Tinjau {0}",
    "selectMigrationItem": "Pilih {0} untuk migrasi",
    "showIgnoredMigrations": "Tampilkan Migrasi yang Diabaikan",
    "showIgnoredMigrationsAriaLabel": "Tampilkan dan pulihkan migrasi yang diabaikan",
    "toolSetMigrationManualReviewGuidance": "Pindahkan pemilihan alat, bukan berkasnya. Konfigurasikan alat yang didukung langsung di agen kustom atau tab Alat, atau gunakan plugin agen untuk alur kerja bersama.",
    "toolSetMigrationManualReviewReason": "Kumpulan alat (tool sets) sudah usang dan tidak didukung oleh runtime Copilot.",
    "viewContributingExtensionAriaLabel": "Lihat ekstensi yang menyumbang {0}"
}

MANAGEMENT_EDITOR_PATCH = {
    "agents": "Agen",
    "agentsDesc": "Tentukan agen kustom dengan persona khusus, akses alat, dan instruksi untuk tugas-tugas tertentu.",
    "backToCustomizationDiscovery": "Kembali ke Jelajah",
    "backToCustomizationDiscoveryTooltip": "Kembali ke Jelajah",
    "backToCustomizationMigrations": "Kembali ke migrasi",
    "backToOverview": "Kembali ke ringkasan",
    "browse": "Jelajahi",
    "canvases": "Kanvas",
    "canvasesDesc": "Kelola ekstensi kanvas untuk antarmuka visual generatif.",
    "confirmDelete": "Hapus '{0}'?",
    "confirmDeleteDetail": "Tindakan ini tidak dapat diurungkan.",
    "customizationMigrationShortcut": "Migrasi",
    "customizationMigrationShortcutLabel": "Migrasi",
    "delete": "Hapus",
    "deleteBackup": "Hapus Cadangan",
    "deleteCustomization": "Hapus",
    "edit": "Ubah",
    "hooks": "Kait (Hooks)",
    "hooksDesc": "Konfigurasikan kait siklus hidup untuk agen dan otomatisasi alur kerja.",
    "instructions": "Instruksi",
    "instructionsDesc": "Panduan kontekstual dan aturan instruksi yang selalu disertakan ke model.",
    "mcp": "Server MCP",
    "mcpDesc": "Hubungkan server Model Context Protocol eksternal untuk memperluas kapabilitas agen.",
    "mcpServers": "Server MCP",
    "migrate": "Migrasikan...",
    "migrateWithAgent": "Migrasikan dengan Agen",
    "migrationBrowse": "Jelajahi",
    "migrationCardTitleChatParticipants": "Partisipan Obrolan",
    "migrationCardTitleMcpServers": "Server MCP",
    "migrationCardTitlePromptToSkill": "Konversi Prompt ke Keahlian (Skills)",
    "migrationCardTitleToolSets": "Kumpulan Alat (Tool Sets)",
    "migrationCardTitleUserData": "Data Pengguna",
    "migrationDestinationPath": "Tujuan: {0}",
    "migrationExtensionScope": "Ekstensi",
    "migrationExtensionsScope": "Ekstensi",
    "migrationGuidanceItems": "{0} kustomisasi",
    "migrationGuidanceOneItem": "1 kustomisasi",
    "migrationInProgressAction": "Memigrasikan...",
    "migrationLearnMore": "Pelajari Lebih Lanjut",
    "migrationNeedsManualReviewReason": "Server ini tidak dapat dimigrasikan secara otomatis. Perbarui secara manual dalam berkas konfigurasinya.",
    "migrationUserScope": "Pengguna",
    "migrationWorkspaceScope": "Ruang Kerja",
    "migrations": "Migrasi",
    "models": "Model",
    "modelsDesc": "Konfigurasikan dan kelola model bahasa yang tersedia untuk digunakan.",
    "overview": "Ringkasan",
    "overviewButtonLabel": "Ringkasan",
    "plugins": "Plugin",
    "pluginsDesc": "Pasang dan kelola plugin agen yang menambahkan alat, keahlian, dan integrasi tambahan.",
    "promptMigrationWarningDetails": "Header khusus prompt yang tidak didukung akan dihapus. Keahlian yang dikonversi menyetel disable-model-invocation: true, sehingga agen tidak akan memuatnya secara otomatis; panggil secara manual dengan /nama.",
    "promptMigrationWarningSummary": "Perubahan konversi prompt ke keahlian (skill)",
    "prompts": "Prompt",
    "promptsDesc": "Templat prompt yang dapat digunakan kembali dan dipanggil sebagai perintah garis miring (/slash).",
    "restoreSources": "Pulihkan Sumber",
    "saved": "Tersimpan",
    "skills": "Keahlian (Skills)",
    "skillsDesc": "Buat berkas keahlian yang dapat digunakan kembali untuk menyediakan pengetahuan dan alur kerja spesifik.",
    "tools": "Alat",
    "toolsDesc": "Aktifkan atau nonaktifkan kelompok alat model bahasa yang tersedia untuk obrolan.",
    "userSaveTarget": "Pengguna",
    "workspaceSaveTarget": "Ruang Kerja"
}

TREEVIEW_VIEWS_PATCH = {
    "aiCustomizationTree": "Item Kustomisasi Obrolan",
    "builtinWithCount": "Bawaan ({0})",
    "customAgents": "Agen Kustom",
    "extensionsWithCount": "Ekstensi ({0})",
    "instructions": "Instruksi",
    "mcpServers": "Server MCP",
    "pluginsWithCount": "Plugin ({0})",
    "skills": "Keahlian (Skills)",
    "userWithCount": "Pengguna ({0})",
    "workspaceWithCount": "Ruang Kerja ({0})"
}

def main():
    print("=== Menerapkan Patch Kustomisasi & Migrasi Agen ===")
    main_i18n_path = "translations/main.i18n.json"

    with open(main_i18n_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    contents = data.get("contents", {})

    # 1. Patch customizationMigrationDashboard
    mod1 = "vs/workbench/contrib/chat/browser/aiCustomization/customizationMigrationDashboard"
    if mod1 not in contents:
        contents[mod1] = {}
    contents[mod1].update(MIGRATION_DASHBOARD_PATCH)
    print(f"✅ Diperbarui: {mod1} ({len(MIGRATION_DASHBOARD_PATCH)} kunci)")

    # 2. Patch aiCustomizationManagementEditor
    mod2 = "vs/workbench/contrib/chat/browser/aiCustomization/aiCustomizationManagementEditor"
    if mod2 not in contents:
        contents[mod2] = {}
    contents[mod2].update(MANAGEMENT_EDITOR_PATCH)
    print(f"✅ Diperbarui: {mod2} ({len(MANAGEMENT_EDITOR_PATCH)} kunci)")

    # 3. Patch aiCustomizationTreeViewViews
    mod3 = "vs/sessions/contrib/aiCustomizationTreeView/browser/aiCustomizationTreeViewViews"
    if mod3 not in contents:
        contents[mod3] = {}
    contents[mod3].update(TREEVIEW_VIEWS_PATCH)
    print(f"✅ Diperbarui: {mod3} ({len(TREEVIEW_VIEWS_PATCH)} kunci)")

    # Simpan main.i18n.json
    with open(main_i18n_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ Berhasil menyimpan translations/main.i18n.json")

if __name__ == "__main__":
    main()

