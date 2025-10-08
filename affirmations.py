import streamlit as st
import uuid
import json
import os
from datetime import datetime

def render_affirmation_section():
    st.markdown("## 🌅 Morning & 🌃 Evening Affirmations")

    affirmations = {
        "Morning": {
            "lines": [
                "I welcome this day with gratitude and joy.",
                "I am energized, focused, and ready to create.",
                "I radiate positivity and attract abundance."
            ],
            "youtube": "https://www.youtube.com/watch?v=t_8BAU2k_6E"
        },
        "Evening": {
            "lines": [
                "I release all worries and embrace peace.",
                "I am proud of what I accomplished today.",
                "I rest deeply and wake up refreshed."
            ],
            "youtube": "https://www.youtube.com/watch?v=oVEEM-MyBdI"
        }
    }

    # ✅ Unique key to avoid DuplicateWidgetID error
    unique_key = f"affirmation_time_selector_{uuid.uuid4()}"
    time_of_day = st.radio("Choose your affirmation time", ["Morning", "Evening"], key=unique_key)

    if time_of_day:
        st.markdown(f"### {time_of_day} Affirmations")
        for line in affirmations[time_of_day]["lines"]:
            st.write(f"🪷 {line}")
        st.markdown(f"[🎧 Play Guided {time_of_day} Affirmations on YouTube]({affirmations[time_of_day]['youtube']})")

        # 💖 Save to My Rituals
        if st.button(f"💖 Save {time_of_day} Affirmations to My Rituals"):
            entry = {
                "category": "Affirmation",
                "name": f"{time_of_day} Affirmations",
                "text": "\n".join(affirmations[time_of_day]["lines"]),
                "youtube": affirmations[time_of_day]["youtube"]
            }
            with open("my_rituals.json", "a") as f:
                f.write(json.dumps(entry) + "\n")
            st.success(f"{time_of_day} Affirmations added to your rituals.")

        # 🧘 Mood-aware journaling prompt
        st.markdown("### 📝 Reflect on your mood")
        mood = st.selectbox("How are you feeling right now?", ["😊 Peaceful", "😌 Grateful", "😢 Reflective", "😠 Stressed", "🙏 Seeking"], key=f"mood_{uuid.uuid4()}")
        journal = st.text_area("Write a few lines to release or affirm your current state:", key=f"journal_{uuid.uuid4()}")

        if journal:
            st.success("Your reflection has been recorded. Let your words guide your healing.")
