@echo off
title Push KNS Enterprise Website to GitHub
color 0a
echo =======================================================================
echo           PUSHING KNS ENTERPRISE UPDATES TO GITHUB
echo =======================================================================
echo.
cd /d "E:\knsenterprise_repo"
echo Running git push origin main...
git push origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Website successfully updated on GitHub Pages!
    echo Visit: https://knsenterprise2-hue.github.io/knsenterprise/
) else (
    echo [NOTE] If prompted for GitHub login, please sign in.
)
echo.
pause
