import streamlit as st
import json
import os

def render_rituals():
    st.title("💖 Personalized Rituals")

    if not os.path.exists("my_rituals.json"):
        st.info("No rituals saved yet. Explore chants, affirmations, and playlists to begin your journey.")
        return

    with open("my_rituals.json", "r") as f:
        entries = f.readlines()

    seen = set()
    unique_entries = []
    for line in reversed(entries):  # Show latest first
        try:
            data = json.loads(line)
            key = (data["category"], data["name"])
            if key not in seen:
                seen.add(key)
                unique_entries.append(data)
        except json.JSONDecodeError:
            continue

    if not unique_entries:
        st.info("No unique rituals found.")
        return

    st.markdown("### 🧘 Your Recent Rituals")
    for data in unique_entries[:10]:  # Show last 10 unique
        st.markdown(f"**{data['name']}** ({data['category']})")
        st.code(data["text"])
        st.markdown(f"[🎧 Replay on YouTube]({data['youtube']})")
        st.markdown("---")
