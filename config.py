import os

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get("PORT", 5000))
DEBUG = bool(os.environ.get("DEBUG", False))
NEXT_HOP_URL = os.environ.get('NEXT_HOP_URL', '')
MAX_DEPTH = int(os.environ.get('MAX_DEPTH', 1))
