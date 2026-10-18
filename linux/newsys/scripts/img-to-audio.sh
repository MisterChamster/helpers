#!/usr/bin/env bash

cd /home/root-user/gitclones/audio-img

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt >/dev/null 2>&1

python3 main.py

# read -p "Press Enter to continue..."
