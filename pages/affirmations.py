import streamlit as st
import json
from datetime import datetime
import uuid

def render_affirmation_section(default=None):
    st.title("🌅 Affirmation Explorer")

    # Time selector options
    time_options = ["Morning", "Night", "Anytime"]

    # Initialize session state on first load
    if "selected_time_of_day" not in st.session_state:
        st.session_state.selected_time_of_day = default if default in time_options else "Morning"

    # Radio selector with persistent state
    time_of_day = st.radio(
        "Choose your affirmation time",
        time_options,
        index=time_options.index(st.session_state.selected_time_of_day),
        key="affirmation_time_selector_main"
    )

    # Update session state with current selection
    st.session_state.selected_time_of_day = time_of_day

    # Affirmation content
    affirmations = {
        "Morning": {
            "lines": ["I am grateful for this new day.", "I welcome peace and clarity."],
            "youtube": "https://www.youtube.com/watch?v=t_8BAU2k_6E&t=2s"
        },
        "Night": {
            "lines": ["I release the day with grace.", "I am calm and centered."],
            "youtube": "https://www.youtube.com/watch?v=oVEEM-MyBdI&t=4s"
        },
        "Anytime": {
            "lines": ["I am enough, just as I am.", "I choose peace in this moment."],
            "youtube": "https://www.youtube.com/watch?v=efZFARmGyMs"
        }
    }

    # Display selected affirmations
    st.markdown(f"### ✨ {time_of_day} Affirmations")
    for line in affirmations[time_of_day]["lines"]:
        st.write(f"• {line}")
    st.markdown(f"[🎧 Listen on YouTube]({affirmations[time_of_day]['youtube']})")

    # Save to My Rituals with unique button key
    save_button_key = f"save_affirmation_button_{time_of_day}_{uuid.uuid4()}"
    if st.button(f"💖 Save {time_of_day} Affirmations to My Rituals", key=save_button_key):
        tags = {
            "Morning": ["Grateful", "Peaceful"],
            "Night": ["Reflective", "Peaceful"],
            "Anytime": ["Empowering", "Peaceful"]
        }[time_of_day]

        entry = {
            "category": "Affirmation",
            "name": f"{time_of_day} Affirmations",
            "text": "\n".join(affirmations[time_of_day]["lines"]),
            "youtube": affirmations[time_of_day]["youtube"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "tags": tags
        }

        with open("my_rituals.json", "a") as f:
            f.write(json.dumps(entry) + "\n")

        st.success(f"{time_of_day} affirmations saved to your rituals.")
