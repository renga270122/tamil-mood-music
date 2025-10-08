import streamlit as st

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

    time_of_day = st.radio("Choose your affirmation time", ["Morning", "Evening"])
    if time_of_day:
        st.markdown(f"### {time_of_day} Affirmations")
        for line in affirmations[time_of_day]["lines"]:
            st.write(f"🪷 {line}")
        st.markdown(f"[🎧 Play Guided {time_of_day} Affirmations on YouTube]({affirmations[time_of_day]['youtube']})")
