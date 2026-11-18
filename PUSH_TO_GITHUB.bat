@echo off
setlocal enabledelayedexpansion
title KNS Enterprise - 1-Click GitHub Website Publisher
color 0b

echo =======================================================================
echo          KNS ENTERPRISE - OFFICIAL WEBSITE GITHUB PUBLISHER
echo =======================================================================
echo.

:: Navigate to this repository directory dynamically
cd /d "%~dp0"
echo [1/4] Repository Location: %CD%

:: Check if git is available
where git >nul 2>&1
if %ERRORLEVEL% neq 0 (
    color 0c
    echo [ERROR] Git is not installed or not in PATH!
    echo Please install Git or contact N.I.N.O.
    pause
    exit /b 1
)

echo.
echo [2/4] Staging website files for GitHub Pages...
git add index.html .gitignore PUSH_TO_GITHUB.bat assets/ *.pdf *.png *.js *.html 2>nul

:: Check git status
git status --short

echo.
echo [3/4] Committing updates...
:: Check if there are staged changes
git diff --cached --quiet
if %ERRORLEVEL% neq 0 (
    set "COMMIT_MSG=Update KNS Enterprise Official Portal [%DATE% %TIME%]"
    git commit -m "!COMMIT_MSG!"
    echo [OK] Changes committed successfully.
) else (
    echo [INFO] No new local changes to commit. Proceeding to sync with GitHub...
)

echo.
echo [4/4] Pushing to GitHub (origin main)...
git push origin main

if %ERRORLEVEL% equ 0 (
    color 0a
    echo.
    echo =======================================================================
    echo  [SUCCESS] WEBSITE SUCCESSFULLY PUBLISHED TO GITHUB PAGES!
    echo =======================================================================
    echo.
    echo  Live Website URL:
    echo  https://knsenterprise2-hue.github.io/knsenterprise/
    echo.
    echo  Repository URL:
    echo  https://github.com/knsenterprise2-hue/knsenterprise
    echo =======================================================================
) else (
    color 0c
    echo.
    echo =======================================================================
    echo  [FAILED] Git push encountered an error!
    echo  Please check internet connection or GitHub credentials.
    echo =======================================================================
)

echo.
echo Press any key to close this window...
pause >nul
