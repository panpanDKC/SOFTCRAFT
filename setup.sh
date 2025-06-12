python3 -m venv venv || { echo "venv creation failed"; return 1; }
source venv/bin/activate || { echo "activate failed"; return 1; }
pip install --upgrade pip || echo "pip upgrade failed"
pip install -r requirements.txt || echo "requirements install failed"