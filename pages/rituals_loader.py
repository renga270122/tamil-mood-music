import json
from datetime import date

RITUALS_FILE = "my_rituals.json"

# 📥 Load rituals safely
def load_rituals():
    rituals = []
    try:
        with open(RITUALS_FILE, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    if "name" not in entry:
                        entry["name"] = "Unnamed"
                    if "date" not in entry:
                        entry["date"] = "Unknown"
                    rituals.append(entry)
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return rituals

# 💾 Save rituals back to file
def save_rituals(rituals):
    with open(RITUALS_FILE, "w") as f:
        for r in rituals:
            f.write(json.dumps(r) + "\n")

# 📊 Ritual stats
def get_ritual_stats(rituals):
    today = date.today().isoformat()
    total = len(rituals)
    daily = sum(1 for r in rituals if r.get("date") == today)
    return total, daily
