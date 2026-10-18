@echo off
chcp 65001 >nul
cd /d "%~dp0"
title zTranzlator Launcher

echo ============================================================
echo   zTranzlator - Project Zomboid (Build 42) Translation Suite
echo ============================================================
echo.

:: 1. すでにスタンドアロン版 (EXE) が存在するか確認 (0秒即起動)
if exist "%~dp0zTranzlator.exe" (
    echo [zTranzlator] スタンドアロン版 (zTranzlator.exe) を起動します...
    start "" "%~dp0zTranzlator.exe"
    exit /b 0
)
if exist "%~dp0zTranzlator\zTranzlator.exe" (
    echo [zTranzlator] スタンドアロン版 (zTranzlator\zTranzlator.exe) を起動します...
    start "" "%~dp0zTranzlator\zTranzlator.exe"
    exit /b 0
)
if exist "%LOCALAPPDATA%\zTranzlator\zTranzlator\zTranzlator.exe" (
    echo [zTranzlator] スタンドアロン版 (AppData) を起動します...
    start "" "%LOCALAPPDATA%\zTranzlator\zTranzlator\zTranzlator.exe"
    exit /b 0
)
if exist "%LOCALAPPDATA%\zTranzlator\zTranzlator.exe" (
    echo [zTranzlator] スタンドアロン版 (AppData) を起動します...
    start "" "%LOCALAPPDATA%\zTranzlator\zTranzlator.exe"
    exit /b 0
)

:: 2. Python 環境の検出 (Windows Store のダミースタブを安全に回避)
set "PYTHON_CMD="
python -c "import sys" >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_CMD=python"
) else (
    py -c "import sys" >nul 2>nul
    if %ERRORLEVEL% EQU 0 set "PYTHON_CMD=py"
)

:: Python が正常に動作する場合: 必要なライブラリを確認して起動
if defined PYTHON_CMD (
    echo [zTranzlator] Python 環境を検出しました (%PYTHON_CMD%)
    %PYTHON_CMD% -c "import customtkinter, PIL, requests, psutil" >nul 2>nul
    if %ERRORLEVEL% NEQ 0 (
        echo [zTranzlator] 初回セットアップ: 必要なライブラリを自動インストールしています...
        %PYTHON_CMD% -m pip install --quiet customtkinter pillow requests psutil darkdetect
    )
    echo [zTranzlator] アプリケーションを起動中...
    %PYTHON_CMD% app_gui.py
    if %ERRORLEVEL% EQU 0 exit /b 0
    echo.
    echo [警告] Python スクリプトの実行に失敗しました。
    echo スタンドアロン版（EXE）の自動セットアップへ切り替えます...
    echo.
)

:: 3. Python が未導入の環境 (クリーンなWindows PC向け):
:: GitHub Releases からスタンドアロン版（EXE）を全自動ダウンロード・セットアップ
echo ============================================================
echo   Python 未導入環境を検出しました。
echo   スタンドアロン実行環境 (EXE版) を全自動セットアップします。
echo   ※ 初回のみダウンロードが行われます（Pythonのインストール不要）
echo ============================================================
echo.
echo GitHub Releases より最新パッケージを取得中... しばらくお待ちください。

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$ProgressPreference = 'SilentlyContinue';" ^
    "$targetDir = '%~dp0';" ^
    "$testFile = Join-Path $targetDir '.perm_test';" ^
    "$canWrite = $false;" ^
    "try { [System.IO.File]::WriteAllText($testFile, 'test'); Remove-Item $testFile -Force; $canWrite = $true; } catch { $canWrite = $false; };" ^
    "if (-not $canWrite) { $targetDir = Join-Path $env:LOCALAPPDATA 'zTranzlator'; if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force | Out-Null }; };" ^
    "$zipPath = Join-Path $targetDir 'zTranzlator_setup.zip';" ^
    "$url = 'https://github.com/unelmapjt/zTranzlator/releases/download/v1.0.0/zTranzlator_v1.0.0_win64.zip';" ^
    "try {" ^
    "    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;" ^
    "    Write-Host 'ダウンロード中...';" ^
    "    Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing;" ^
    "    Write-Host '展開中...';" ^
    "    Expand-Archive -Path $zipPath -DestinationPath $targetDir -Force;" ^
    "    if (Test-Path $zipPath) { Remove-Item $zipPath -Force; };" ^
    "    Write-Host 'セットアップ完了！起動中...';" ^
    "    $exe1 = Join-Path $targetDir 'zTranzlator.exe';" ^
    "    $exe2 = Join-Path $targetDir 'zTranzlator\zTranzlator.exe';" ^
    "    if (Test-Path $exe1) { Start-Process $exe1; exit 0; };" ^
    "    if (Test-Path $exe2) { Start-Process $exe2; exit 0; };" ^
    "    exit 0;" ^
    "} catch {" ^
    "    Write-Error $_.Exception.Message;" ^
    "    exit 1;" ^
    "}"

if %ERRORLEVEL% EQU 0 exit /b 0

echo.
echo ============================================================
echo [エラー] 自動セットアップに失敗しました。
echo インターネット接続を確認するか、以下のURLから
echo スタンドアロン版（ZIP）を直接ダウンロードしてご利用ください：
echo.
echo   https://github.com/unelmapjt/zTranzlator/releases/latest
echo ============================================================
echo.
set /p OPEN_BROWSER="ブラウザでダウンロードページを開きますか？ (Y/N): "
if /i "%OPEN_BROWSER%"=="Y" (
    start https://github.com/unelmapjt/zTranzlator/releases/latest
)
pause
