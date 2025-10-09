import random
from datetime import datetime

TRIVIA_LIST = [
    "🧘‍♂️ The word 'yoga' comes from the Sanskrit root 'yuj', meaning 'to unite'.",
    "🎶 Chanting 'Om' is believed to vibrate at the frequency of the universe: 432 Hz.",
    "🌿 Tulsi (holy basil) is considered a sacred plant in India and used in spiritual rituals.",
    "🪔 The Gayatri Mantra is one of the oldest known mantras, found in the Rig Veda.",
    "🕉️ The symbol 'Om' represents the union of mind, body, and spirit.",
    "🔥 Lighting a lamp during rituals symbolizes the removal of darkness and ignorance.",
    "🌕 Full moons are traditionally seen as powerful times for manifestation and healing.",
    "📿 A japa mala typically has 108 beads — a sacred number in many spiritual traditions.",
    "🧠 Studies show that listening to calming chants can reduce cortisol and improve focus.",
    "💖 Gratitude journaling for just 5 minutes a day can boost emotional resilience."
]

def get_daily_trivia():
    seed = int(datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    return random.choice(TRIVIA_LIST)

def get_random_trivia():
    return random.choice(TRIVIA_LIST)
