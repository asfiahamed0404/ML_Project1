#!/usr/bin/env bash
# ============================================================
#  ML Project — macOS / Linux setup helper
#  Run:  bash setup.sh
# ============================================================
set -e

echo
echo "=== [1/3] Creating virtualenv ./venv ... ==="
python3 -m venv venv

echo
echo "=== [2/3] Activating venv ... ==="
# shellcheck disable=SC1091
source venv/bin/activate

echo
echo "=== [3/3] Installing requirements + editable package ... ==="
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

echo
echo "=== Done! You can now run: ==="
echo "    python app.py"
echo "=== Or train the model:    http://127.0.0.1:5000/train ==="
echo