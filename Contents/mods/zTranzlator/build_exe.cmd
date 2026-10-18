@echo off
chcp 65001 >nul
cd /d "%~dp0"
title zTranzlator - EXE Build Tool
echo ============================================================
echo   zTranzlator Standalone EXE Builder
echo   Project Zomboid Build 42 Translation Tool
echo ============================================================
echo.
echo [1/3] ビルド用ライブラリを確認・インストール中...
python -m pip install --upgrade pip
python -m pip install pyinstaller pillow customtkinter darkdetect psutil requests
echo.
echo [2/3] zTranzlator.exe をビルド中 (Modern Single-folder Portable)...
python -m PyInstaller --noconfirm --onedir --windowed ^
    --name "zTranzlator" ^
    --add-data "vanilla_dict.json;." ^
    --add-data "vanilla_dict_KO.json;." ^
    --add-data "MANUAL.html;." ^
    --add-data "README.md;." ^
    --add-data "SPECIFICATION.md;." ^
    --add-data "preview.png;." ^
    --add-data "poster.png;." ^
    --collect-all customtkinter ^
    app_gui.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [Error] ビルドに失敗しました。
    pause
    exit /b %ERRORLEVEL%
)
echo.
echo [3/4] 配信用ドキュメントを同梱中...
copy /y "HOW_TO_USE.txt" "dist\zTranzlator\" >nul
copy /y "MANUAL.html" "dist\zTranzlator\" >nul
copy /y "README.md" "dist\zTranzlator\" >nul

echo [4/4] 配信用 ZIP アーカイブを作成中...
powershell -NoProfile -Command "Compress-Archive -Path 'dist\zTranzlator' -DestinationPath 'dist\zTranzlator_v1.0.0_win64.zip' -Force"

echo.
echo ============================================================
echo   ビルド ＆ ZIP パッケージ作成が完了しました！
echo   EXE: dist\zTranzlator\zTranzlator.exe
echo   ZIP: dist\zTranzlator_v1.0.0_win64.zip
echo ============================================================
pause
