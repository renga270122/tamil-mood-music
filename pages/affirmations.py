import streamlit as st
import json
from datetime import datetime
import uuid

RITUALS_FILE = "my_rituals.json"

# 💾 Save ritual entry
def save_affirmation_to_rituals(name, lines, youtube, tags):
    entry = {
        "id": str(uuid.uuid4()),
        "category": "Affirmation",
        "name": name,
        "text": "\n".join(lines),
        "youtube": youtube,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tags": tags
    }
    with open(RITUALS_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    st.success(f"✅ Saved '{name}' to your rituals!")

# 🌅 Affirmation Explorer
def render_affirmation_section(default=None):
    st.title("🌅 Affirmation Explorer")

    time_options = ["Morning", "Night", "Anytime"]
    if "selected_time_of_day" not in st.session_state:
        st.session_state.selected_time_of_day = default if default in time_options else "Morning"

    key_suffix = default if default else "Any"
    time_of_day = st.radio(
        "Choose your affirmation time",
        time_options,
        index=time_options.index(st.session_state.selected_time_of_day),
        key=f"affirmation_time_selector_{key_suffix}"  # ✅ unique per context
    )

    st.session_state.selected_time_of_day = time_of_day

    affirmations = {
        "Morning": {
            "lines": ["I am grateful for this new day.", "I welcome peace and clarity."],
            "youtube": "https://www.youtube.com/watch?v=t_8BAU2k_6E&t=2s",
            "tags": ["Grateful", "Peaceful"]
        },
        "Night": {
            "lines": ["I release the day with grace.", "I am calm and centered."],
            "youtube": "https://www.youtube.com/watch?v=oVEEM-MyBdI&t=4s",
            "tags": ["Reflective", "Peaceful"]
        },
        "Anytime": {
            "lines": ["I am enough, just as I am.", "I choose peace in this moment."],
            "youtube": "https://www.youtube.com/watch?v=efZFARmGyMs",
            "tags": ["Empowering", "Peaceful"]
        }
    }

    selected = affirmations[time_of_day]
    st.markdown(f"### ✨ {time_of_day} Affirmations")
    for line in selected["lines"]:
        st.write(f"• {line}")
    st.markdown(f"[🎧 Listen on YouTube]({selected['youtube']})")

    # ✅ Stable unique key using time_of_day only
    if st.button(f"💖 Save {time_of_day} Affirmations to My Rituals", key=f"save_{time_of_day}_affirmations"):
        save_affirmation_to_rituals(
            name=f"{time_of_day} Affirmations",
            lines=selected["lines"],
            youtube=selected["youtube"],
            tags=selected["tags"]
        )
