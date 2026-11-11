"""
zTranzlator - Vanilla Master Dictionary Builder (Phase 1)
Project Zomboid Build 42 の公式英語(EN)と日本語(JP)を突合し、
高精度なマスター対訳辞書 (vanilla_dict.json) を自動生成するスクリプト。
"""

import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

if sys.platform == "win32":
    try:
        import winreg
    except ImportError:
        winreg = None
else:
    winreg = None


def is_valid_pz_dir(path) -> bool:
    """有効なProject Zomboid本体ディレクトリかどうかを判定"""
    if not path:
        return False
    p = Path(path)
    if not p.is_dir():
        return False
    # 実行ファイルまたは media/lua が存在するか
    has_exe = (p / "ProjectZomboid64.exe").is_file() or (p / "projectzomboid.exe").is_file() or (p / "ProjectZomboid32.exe").is_file()
    has_media = (p / "media" / "lua").is_dir()
    return has_exe or has_media


def is_valid_workshop_dir(path) -> bool:
    """有効なSteam Workshop (108600) ディレクトリかどうかを判定"""
    if not path:
        return False
    p = Path(path)
    return p.is_dir()


def get_all_steam_libraries() -> list:
    """
    Windowsレジストリ、Steam本体設定、libraryfolders.vdf、全ドライブ探索から
    PC上に存在するすべてのSteamライブラリフォルダを収集して返す
    """
    libraries = []
    seen = set()

    def add_lib(p: Path):
        try:
            if p and p.is_dir():
                resolved = p.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    libraries.append(resolved)
        except Exception:
            pass

    # 1. Windows レジストリから PZ のインストール先を取得
    if winreg:
        reg_keys = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
            (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
        ]
        for root_key, sub_key in reg_keys:
            try:
                with winreg.OpenKey(root_key, sub_key) as k:
                    val, _ = winreg.QueryValueEx(k, "InstallLocation")
                    if val:
                        pz_path = Path(val)
                        if pz_path.is_dir():
                            lib_root = pz_path.parent.parent.parent
                            add_lib(lib_root)
            except Exception:
                pass

    # 2. Windows レジストリから Steam 本体のインストールパスを取得
    steam_roots = []
    if winreg:
        steam_reg_keys = [
            (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam", "SteamPath"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam", "InstallPath"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath"),
        ]
        for root_key, sub_key, val_name in steam_reg_keys:
            try:
                with winreg.OpenKey(root_key, sub_key) as k:
                    val, _ = winreg.QueryValueEx(k, val_name)
                    if val and Path(val).is_dir():
                        steam_roots.append(Path(val))
            except Exception:
                pass

    for s_root in steam_roots:
        add_lib(s_root)
        # libraryfolders.vdf をパースして全外部Steamライブラリを取得
        vdf_path = s_root / "steamapps" / "libraryfolders.vdf"
        if vdf_path.is_file():
            try:
                content = vdf_path.read_text(encoding="utf-8", errors="ignore")
                for match in re.findall(r'"path"\s+"([^"]+)"', content):
                    clean_path = match.replace(r"\\", "\\")
                    add_lib(Path(clean_path))
            except Exception:
                pass

    # 3. 利用可能なすべてのドライブレターを探索
    drive_letters = []
    if sys.platform == "win32":
        import string
        for letter in string.ascii_uppercase:
            drive = Path(f"{letter}:\\")
            if drive.exists():
                drive_letters.append(drive)
    else:
        drive_letters = [Path("/")]

    for drive in drive_letters:
        candidates = [
            drive / "SteamLibrary",
            drive / "Steam",
            drive / "Program Files (x86)" / "Steam",
            drive / "Program Files" / "Steam",
            drive / "Games" / "SteamLibrary",
            drive / "Games" / "Steam",
        ]
        for c in candidates:
            add_lib(c)

    return libraries


def find_pz_directory(custom_path=None) -> Path:
    """Project Zomboidのインストール先を特定する (手動パス最優先 ➡ レジストリ ➡ 全Steamライブラリ ➡ 全ドライブ走査)"""
    # 1. ユーザー手動指定パス
    if custom_path:
        p = Path(custom_path)
        if is_valid_pz_dir(p):
            return p

    # 2. Windows レジストリから直接取得
    if winreg:
        reg_keys = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
            (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 108600"),
        ]
        for root_key, sub_key in reg_keys:
            try:
                with winreg.OpenKey(root_key, sub_key) as k:
                    val, _ = winreg.QueryValueEx(k, "InstallLocation")
                    if val and is_valid_pz_dir(val):
                        return Path(val)
            except Exception:
                pass

    # 3. 検出された全Steamライブラリから探す
    libraries = get_all_steam_libraries()
    for lib in libraries:
        candidate = lib / "steamapps" / "common" / "ProjectZomboid"
        if is_valid_pz_dir(candidate):
            return candidate

    # 4. 全ドライブの直下やGamesフォルダから探す (GOG版・スタンドアロン等)
    if sys.platform == "win32":
        import string
        for letter in string.ascii_uppercase:
            drive = Path(f"{letter}:\\")
            if not drive.exists():
                continue
            extras = [
                drive / "Games" / "Project Zomboid",
                drive / "Games" / "ProjectZomboid",
                drive / "GOG Games" / "Project Zomboid",
                drive / "ProjectZomboid",
            ]
            for ext in extras:
                if is_valid_pz_dir(ext):
                    return ext

    return None


def find_workshop_directory(pz_dir=None, custom_path=None) -> Path:
    """Steam Workshop (108600) ディレクトリを特定する"""
    # 1. ユーザー手動指定パス
    if custom_path:
        p = Path(custom_path)
        if is_valid_workshop_dir(p):
            return p

    # 2. PZ本体ディレクトリの親から推測
    if pz_dir:
        try:
            ws = pz_dir.parent.parent / "workshop" / "content" / "108600"
            if ws.is_dir():
                return ws
        except Exception:
            pass

    # 3. 全Steamライブラリから探す
    libraries = get_all_steam_libraries()
    for lib in libraries:
        ws = lib / "steamapps" / "workshop" / "content" / "108600"
        if ws.is_dir():
            return ws

    # 4. デフォルトフォールバック
    default_c = Path(r"C:\Program Files (x86)\Steam\steamapps\workshop\content\108600")
    if default_c.is_dir():
        return default_c

    return None


DEFAULT_PZ_PATHS = [
    Path(r"C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid"),
    Path(r"C:\Program Files\Steam\steamapps\common\ProjectZomboid"),
    Path(r"D:\SteamLibrary\steamapps\common\ProjectZomboid"),
    Path(r"E:\SteamLibrary\steamapps\common\ProjectZomboid"),
]


def clean_text(text: str) -> str:
    """前後の空白や特殊エスケープを正規化"""
    if not isinstance(text, str):
        return ""
    return text.strip()


def build_master_dictionary(pz_dir: Path, output_dir: Path, target_lang: str = "JP") -> Path:
    translate_dir = pz_dir / "media" / "lua" / "shared" / "Translate"
    en_dir = translate_dir / "EN"
    target_dir = translate_dir / target_lang

    if not en_dir.is_dir() or not target_dir.is_dir():
        print(f"[Error] Translateフォルダが見つかりません: {target_dir}")
        return None

    print(f"[1/4] PZ本体ディレクトリを確認: {pz_dir}")
    print(f"      ENフォルダ: {en_dir}")
    print(f"      {target_lang}フォルダ: {target_dir}")

    en_files = sorted(list(en_dir.glob("*.json")))
    print(f"[2/4] スキャン対象のJSONファイル数: {len(en_files)} 件")

    exact_dict = {}
    detailed_dict = defaultdict(lambda: {"translations": set(), "categories": set(), "keys": []})
    
    total_pairs = 0
    file_stats = {}

    for en_file in en_files:
        target_file = target_dir / en_file.name
        if not target_file.is_file():
            continue

        category = en_file.stem
        try:
            with open(en_file, "r", encoding="utf-8") as f:
                en_data = json.load(f)
            with open(target_file, "r", encoding="utf-8") as f:
                target_data = json.load(f)
        except Exception as e:
            print(f"  [Skip] パース失敗: {en_file.name} ({e})")
            continue

        matched_count = 0
        for key, en_val in en_data.items():
            if key not in target_data:
                continue

            target_val = target_data[key]
            en_str = clean_text(en_val)
            trans_str = clean_text(target_val)

            if not en_str or not trans_str:
                continue

            # 英語原文と訳文を記録
            detailed_dict[en_str]["translations"].add(trans_str)
            detailed_dict[en_str]["categories"].add(category)
            detailed_dict[en_str]["keys"].append(key)

            # exact_dict に登録（未登録なら採用）
            if en_str not in exact_dict:
                exact_dict[en_str] = trans_str

            matched_count += 1
            total_pairs += 1

        file_stats[category] = matched_count

    print(f"[3/4] 突合完了! 総キーペア数: {total_pairs} 件")
    print(f"      ユニーク英語フレーズ数: {len(detailed_dict)} 語")

    # 同音異義語（複数の訳が存在する単語）の集計
    homonyms = {}
    for en_str, data in detailed_dict.items():
        if len(data["translations"]) > 1:
            homonyms[en_str] = {
                "translations": list(data["translations"]),
                "categories": list(data["categories"]),
            }

    print(f"      同音異義語（文脈で訳が分かれる単語）: {len(homonyms)} 語")

    # JSON出力用に整形
    output_dir.mkdir(parents=True, exist_ok=True)

    # vanilla_dict_{target_lang}.json (高速引き用シンプル辞書)
    simple_dict_path = output_dir / f"vanilla_dict_{target_lang}.json"
    with open(simple_dict_path, "w", encoding="utf-8") as f:
        json.dump(exact_dict, f, ensure_ascii=False, indent=2)
    
    if target_lang == "JP":
        # 互換用 vanilla_dict.json
        with open(output_dir / "vanilla_dict.json", "w", encoding="utf-8") as f:
            json.dump(exact_dict, f, ensure_ascii=False, indent=2)

    print(f"[4/4] 保存完了:")
    print(f"      -> {simple_dict_path} ({simple_dict_path.stat().st_size // 1024} KB)")

    # 2. vanilla_dict_meta.json (文脈・カテゴリ情報付き詳細辞書)
    detailed_serializable = {}
    for en_str, data in detailed_dict.items():
        detailed_serializable[en_str] = {
            "default": exact_dict[en_str],
            "translations": list(data["translations"]),
            "categories": list(data["categories"]),
            "sample_keys": data["keys"][:3]
        }

    meta_dict_path = output_dir / "vanilla_dict_meta.json"
    with open(meta_dict_path, "w", encoding="utf-8") as f:
        json.dump({
            "version": "B42",
            "unique_terms": len(detailed_dict),
            "homonyms_count": len(homonyms),
            "terms": detailed_serializable,
            "homonyms": homonyms,
        }, f, ensure_ascii=False, indent=2)
    print(f"      -> {meta_dict_path} ({meta_dict_path.stat().st_size // 1024} KB)")

    # プレビュー表示
    print("\n--- 辞書サンプル (一部抜粋) ---")
    samples = [
        "Axe", "Can Opener", "M16 Magazine", "OPTIONS", "QUIT", 
        "First person", "Third person", "Aim", "Walk To"
    ]
    for s in samples:
        if s in exact_dict:
            print(f"  [〇] '{s}' ➡ '{exact_dict[s]}'")
        else:
            print(f"  [✕] '{s}' ➡ (バニラ辞書に未登録 / MOD独自用語)")

    return simple_dict_path


if __name__ == "__main__":
    target_pz = find_pz_directory()
    if len(sys.argv) > 1:
        target_pz = Path(sys.argv[1])

    if not target_pz or not target_pz.is_dir():
        print("[Error] Project Zomboidのインストールディレクトリが見つかりませんでした。")
        print("Usage: python dict_builder.py \"C:\\Path\\To\\ProjectZomboid\"")
        sys.exit(1)

    out_path = Path(__file__).parent
    build_master_dictionary(target_pz, out_path)
