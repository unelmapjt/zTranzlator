@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
title zTranzlator Launcher

echo ============================================================
echo   zTranzlator - Project Zomboid Build 42 Translation Suite
echo ============================================================
echo.

:: 1. すでにスタンドアロン版 [EXE] が存在するか確認
if exist "%~dp0zTranzlator.exe" goto :RUN_EXE1
if exist "%~dp0zTranzlator\zTranzlator.exe" goto :RUN_EXE2
if exist "%LOCALAPPDATA%\zTranzlator\zTranzlator\zTranzlator.exe" goto :RUN_EXE3
if exist "%LOCALAPPDATA%\zTranzlator\zTranzlator.exe" goto :RUN_EXE4
goto :DETECT_PYTHON

:RUN_EXE1
echo [zTranzlator] スタンドアロン版 [zTranzlator.exe] を起動します...
start "" "%~dp0zTranzlator.exe"
exit /b 0

:RUN_EXE2
echo [zTranzlator] スタンドアロン版 [zTranzlator\zTranzlator.exe] を起動します...
start "" "%~dp0zTranzlator\zTranzlator.exe"
exit /b 0

:RUN_EXE3
echo [zTranzlator] スタンドアロン版 [AppData] を起動します...
start "" "%LOCALAPPDATA%\zTranzlator\zTranzlator\zTranzlator.exe"
exit /b 0

:RUN_EXE4
echo [zTranzlator] スタンドアロン版 [AppData] を起動します...
start "" "%LOCALAPPDATA%\zTranzlator\zTranzlator.exe"
exit /b 0

:: 2. Python 環境の検出
:DETECT_PYTHON
set "PYTHON_CMD="
python -c "import sys" >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_CMD=python"
    goto :CHECK_PYTHON
)

py -c "import sys" >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_CMD=py"
    goto :CHECK_PYTHON
)

goto :NO_ENVIRONMENT

:CHECK_PYTHON
echo [zTranzlator] Python 環境を検出しました: %PYTHON_CMD%
%PYTHON_CMD% -c "import customtkinter, PIL, requests, psutil, darkdetect" >nul 2>nul
if %ERRORLEVEL% EQU 0 goto :LAUNCH_APP

echo [zTranzlator] 初回セットアップ: 必要なライブラリを自動インストールしています...
%PYTHON_CMD% -m pip install --quiet customtkinter pillow requests psutil darkdetect
if %ERRORLEVEL% NEQ 0 goto :PIP_FAIL
goto :LAUNCH_APP

:PIP_FAIL
echo.
echo [警告] 必要なライブラリのインストールに失敗しました。
goto :NO_ENVIRONMENT

:LAUNCH_APP
echo [zTranzlator] アプリケーションを起動中...
start "" %PYTHON_CMD% app_gui.py
exit /b 0

:NO_ENVIRONMENT
echo.
echo ============================================================
echo   【実行環境の案内】
echo ============================================================
echo Python または スタンドアロン版 [zTranzlator.exe] が見つかりませんでした。
echo.
echo 以下のいずれかの方法でご利用いただけます：
echo.
echo   【方法1】スタンドアロン版 [ZIP] をダウンロード（おすすめ・Python不要）
echo     ZIP を解凍して、中のファイルをこのフォルダに配置してください。
echo.
echo   【方法2】Python 3.10 以上をインストール
echo     https://www.python.org/downloads/
echo.
echo 公式配布ページ [GitHub Releases]:
echo   https://github.com/unelmapjt/zTranzlator/releases/latest
echo ============================================================
echo.
set /p OPEN_PAGE="ブラウザでダウンロードページを開きますか？ [Y/N]: "
if /i "%OPEN_PAGE%"=="Y" (
    start https://github.com/unelmapjt/zTranzlator/releases/latest
)
pause
