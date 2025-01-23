@echo off
REM -------------------------------------------------
REM Name: run-hoopla.bat
REM Description: Activates a Python venv, prompts
REM              for dt-custom-data and Audiobook URL,
REM              then runs hoopla-key.py with
REM              those arguments.
REM -------------------------------------------------

REM 1) Change directory to the folder where this batch file is located
cd /d "%~dp0"

REM 2) Activate the Python virtual environment
call .\Scripts\activate.bat

REM 3) Prompt for dt-custom-data
echo.
set /p "DT_CUSTOM_DATA=Please enter your dt-custom-data: "

REM 4) Prompt for Audiobook URL
echo.
echo Example: https://www.hoopladigital.com/audiobook/the-double-helix-trudi-strain-trueit/13520844
set /p "AUDIOBOOK_URL=Please enter the URL to the Audiobook: "

REM 5) Run the Python script
python hoopla-key.py "%AUDIOBOOK_URL%" "%DT_CUSTOM_DATA%"

REM 6) Pause (optional)
pause
exit /b
