import streamlit as st
import json
from datetime import date
import uuid

RITUALS_FILE = "my_rituals.json"

# 💾 Save ritual
def save_ritual(name, category, text, youtube=None, tags=None):
    entry = {
        "id": str(uuid.uuid4()),
        "name": name,
        "category": category,
        "text": text,
        "date": date.today().isoformat(),
        "youtube": youtube,
        "tags": tags or []
    }
    with open(RITUALS_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    st.success(f"✅ Saved '{name}' to your rituals!")

# 🌿 Healing Practice Dashboard
def render_healing_practices():
    st.title("🌿 Healing Practices")

    practice = st.radio(
        "Choose your healing path:",
        ["Ho'oponopono Chants", "Guided Meditations", "OM Chanting", "Kriya Yoga"],
        key="healing_selector"
    )

    # 🌺 Ho'oponopono
    if practice == "Ho'oponopono Chants":
        st.header("🌺 Ho'oponopono Healing")
        st.write("Repeat the 4 sacred phrases with intention:")
        st.markdown("**I'm sorry. Please forgive me. Thank you. I love you.**")
        st.video("https://www.youtube.com/watch?v=rrXmjeUdzeM")
        if st.button("💾 Save this practice"):
            save_ritual(
                name="Ho'oponopono Healing",
                category="Chant",
                text="I'm sorry. Please forgive me. Thank you. I love you.",
                youtube="https://www.youtube.com/watch?v=rrXmjeUdzeM",
                tags=["Forgiveness", "Healing", "Hawaiian"]
            )

    # 🧘 Guided Meditations
    elif practice == "Guided Meditations":
        st.header("🧘 Guided Meditations")
        st.write("Explore emotional wellness through guided journeys.")
        st.video("https://www.youtube.com/watch?v=rrXmjeUdzeM")
        if st.button("💾 Save this practice"):
            save_ritual(
                name="Emotional Wellness Meditation",
                category="Meditation",
                text="Guided meditation for emotional healing and mindfulness.",
                youtube="https://www.youtube.com/watch?v=rrXmjeUdzeM",
                tags=["Mindfulness", "Emotional Wellness"]
            )

    # 🔊 OM Chanting
    elif practice == "OM Chanting":
        st.header("🔊 OM Chanting")
        st.write("Chant *A-U-M* slowly and feel the vibration through your body.")
        st.video("https://www.youtube.com/watch?v=rrXmjeUdzeM")
        if st.button("💾 Save this practice"):
            save_ritual(
                name="OM Chanting",
                category="Chant",
                text="Chanting A-U-M for inner peace and vibrational healing.",
                youtube="https://www.youtube.com/watch?v=rrXmjeUdzeM",
                tags=["OM", "Vibration", "Peace"]
            )

    # 🔥 Kriya Yoga
    elif practice == "Kriya Yoga":
        st.header("🔥 Kriya Yoga Practices")
        st.write("Explore Shat Kriyas (cleansing) and Kundalini Kriyas (energy activation).")
        st.video("https://www.youtube.com/watch?v=rrXmjeUdzeM")
        if st.button("💾 Save this practice"):
            save_ritual(
                name="Kriya Yoga",
                category="Kriya",
                text="Kriya Yoga for breath control, energy activation, and inner clarity.",
                youtube="https://www.youtube.com/watch?v=rrXmjeUdzeM",
                tags=["Kriya", "Breathwork", "Energy"]
            )
