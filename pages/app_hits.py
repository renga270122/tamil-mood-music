# utils/app_hits.py

import json
from datetime import datetime, date

HIT_LOG_FILE = "app_hits.jsonl"

# 🔧 Log each app visit
def log_app_hit():
    entry = {"timestamp": datetime.now().isoformat()}
    with open(HIT_LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

# 📥 Load all hits
def load_app_hits():
    try:
        with open(HIT_LOG_FILE, "r") as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []

# 📊 Count total and daily hits
def get_hit_stats(entries):
    today = date.today().isoformat()
    total = len(entries)
    daily = sum(1 for e in entries if e["timestamp"].startswith(today))
    return total, daily
