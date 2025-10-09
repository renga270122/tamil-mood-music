import random
from datetime import datetime

# 🌿 Motivational quote bank
QUOTE_CATEGORIES = {
    "peace": [
        "Peace comes from within. Do not seek it without. — Buddha",
        "The quieter you become, the more you can hear. — Ram Dass",
        "Stillness is where creativity and solutions to problems are found. — Eckhart Tolle",
        "Within you, there is a stillness and a sanctuary to which you can retreat at any time. — Hermann Hesse"
    ],
    "growth": [
        "Hardships often prepare ordinary people for an extraordinary destiny. — C.S. Lewis",
        "The oak fought the wind and was broken, the willow bent when it must and survived. — Robert Jordan",
        "Although the world is full of suffering, it is also full of the overcoming of it. — Helen Keller",
        "We must embrace pain and burn it as fuel for our journey. — Kenji Miyazawa"
    ],
    "positivity": [
        "The universe always works for your highest good, even when you can’t see the path ahead.",
        "Every breath you take is a sacred reminder of life’s infinite blessings.",
        "Your soul already knows the way—trust its whispers even when the path seems unclear.",
        "Light lives within you. No matter how dark the world feels, your soul carries the spark of divine love."
    ]
}

# 🔮 Get a random quote from all categories
def get_random_quote():
    all_quotes = sum(QUOTE_CATEGORIES.values(), [])
    return random.choice(all_quotes)

# 🧘‍♂️ Get a quote from a specific category
def get_quote_by_category(category):
    quotes = QUOTE_CATEGORIES.get(category.lower())
    if quotes:
        return random.choice(quotes)
    else:
        return get_random_quote()

# 📅 Optional: Daily quote seed (same quote for the day)
def get_daily_quote():
    seed = int(datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    return get_random_quote()
