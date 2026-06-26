@echo off
REM ============================================================
REM  ML Project — Windows setup helper (cmd)
REM  Run this once after cloning the repo.
REM ============================================================

setlocal

echo.
echo === [1/4] Opening project in VS Code... ===
code . || echo (VS Code 'code' command not found - skipping)

echo.
echo === [2/4] Creating conda environment in .\venv (Python 3.8)...
conda create -p venv python==3.8 -y

echo.
echo === [3/4] Activating environment...
call conda activate venv\

echo.
echo === [4/4] Installing requirements + editable package...
pip install -r requirements.txt
pip install -e .

echo.
echo === Done! You can now run:  python app.py ===
echo === Or train the model:    http://127.0.0.1:5000/train ===
echo.

endlocal