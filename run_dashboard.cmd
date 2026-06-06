@echo off
cd /d "%~dp0"

where node >nul 2>nul
if %errorlevel%==0 (
  node serve_dashboard.js
  exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
  python -m http.server 8000
  exit /b %errorlevel%
)

where py >nul 2>nul
if %errorlevel%==0 (
  py -m http.server 8000
  exit /b %errorlevel%
)

echo Could not find Node.js or Python on PATH.
echo Install Node.js or Python, then run this file again.
exit /b 1
