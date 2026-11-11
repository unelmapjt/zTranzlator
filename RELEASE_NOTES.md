# 🧟 zTranzlator v1.1.0 - Project Zomboid Build 42 Translation Suite

Skyrimの有名翻訳ツール「xTranslator」に着想を得た、**Project Zomboid Build 42 専用の完全非破壊・差分継承AI翻訳ツールスイート**です。  
MODファイルを直接書き換えることなく、安心・安全に母国語（日本語・韓国語・中国語・スペイン語など）の翻訳パッチMODを自動生成します。

---

### 🚀 クイックスタート（つかいかた）
1. 下部の **Assets** 一覧から **`zTranzlator_v1.1.0_win64.zip`** をダウンロードして展開します。
2. フォルダ内の **`zTranzlator.exe`** をダブルクリックするだけで即起動します（**Python不要・完全ポータブル**）。
3. 画面左側で翻訳したいMODを選び、**［一括AI翻訳を実行］** ➡ **［ローカルMOD適用］** をクリックするだけで日本語化パッチMODが完成します！

---

### ✨ 主な特徴 / Key Features
* 🛡️ **完全非破壊＆差分継承**: 元MODを一切傷つけず、MODアプデ時も過去の翻訳を100%自動引き継ぎ。
* 📖 **内蔵スマート辞書**: 公式対訳 35,000語 ＋ UI短縮ルール。GPUやAPIキー不要で即動作。
* 🤖 **多彩なAIエンジン**: Ollama（ローカルLLM）や Google Gemini（無料枠あり）に対応。
* 🌐 **多言語対応**: 日本語(JA)、韓国語(KO)、中国語(CN/CH)、スペイン語(ES)、フランス語(FR)、ドイツ語(DE)など主要11言語に対応。
* 📏 **UI文字幅警告アシスト**: ゲーム画面のボタンから文字がはみ出すのを防ぐリアルタイム文字幅推定。

---

## 🌟 v1.1.0 アップデート内容 / Changelog

### 🇯🇵 日本語
* **全ドライブ・別ディスク対応（PZ本体・Workshopの自動検出を大幅強化）**:
  * Windows レジストリ、Steam設定ファイル（`libraryfolders.vdf`）、PC上の全論理ドライブ（C〜Z）を自動走査。
  * ゲーム本体やSteamを別ドライブ（D/E/Fドライブや外付けSSD等）にインストールしている環境でも、Project Zomboid 本体および Workshop フォルダを確実に自動検出できるようになりました。
* **手動パス指定＆永続保存UIの追加**:
  * 画面上部のステータスに「● PZ: 未検出 (クリックして指定)」が表示され、クリックするだけでエクスプローラーからPZ本体フォルダを指定可能になりました。
  * 「⚙️ 翻訳設定」画面にも「📁 ゲーム・MODパス設定」カードを新設。いつでもPZ本体・Workshopフォルダの手動指定や自動再検出が行えます。
* **Workshop 配布用パッケージおよびドキュメントの同期**

### 🇺🇸 English
* **About zTranzlator**:
  * A non-destructive, incremental AI translation suite for Project Zomboid (Build 42), inspired by Skyrim's xTranslator.
  * Generates clean, standalone companion patch mods without modifying original game/mod files.
* **Multi-Drive & Secondary SSD Auto-Detection**:
  * Automatically scans Windows registry, Steam configuration (`libraryfolders.vdf`), and all available logical drives (C through Z).
  * Smoothly detects Project Zomboid install directory and Workshop folders even if located on secondary drives/SSDs or custom paths.
* **Manual Directory Configuration & Persistent Settings**:
  * Added clickable status button on the header to select the PZ install folder in 1 click.
  * Added "Directory Settings (PZ & Workshop)" section to Settings modal for manual configuration & re-detection.

---

### 📦 Assets（配布ファイル）
* **`zTranzlator_v1.1.0_win64.zip`** (Standalone Portable EXE - Python不要)
