#!/usr/bin/env bash
# Rebuild the site from pages.py, then serve it at http://localhost:8000
# Ctrl-C to stop. Re-run after any edit, or just run build.py and refresh.
set -e
cd "$(dirname "$0")"
python3 build.py
echo
echo "  → http://localhost:8000"
echo
python3 -m http.server 8000
