import streamlit as st
import json
from collections import Counter
import matplotlib.pyplot as plt
import os
import uuid
from datetime import datetime, date

FEEDBACK_FILE = "soulvest_feedback.json"

# 🔧 Save feedback entry
def save_feedback(entry):
    with open(FEEDBACK_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

# 📥 Load all feedback entries
def load_feedback():
    try:
        with open(FEEDBACK_FILE, "r") as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []

# 📊 Count total and today's feedback
def get_feedback_stats(entries):
    today = date.today().isoformat()
    total = len(entries)
    daily = sum(1 for e in entries if e.get("timestamp", "").startswith(today))
    return total, daily

# 🧘 Main feedback section
def render_feedback_section():
    st.markdown("## 💬 Share Your Experience with Soulvest")

    # 💬 Feedback Form
    with st.form(key=f"soulvest_feedback_{uuid.uuid4()}"):  # ✅ dynamic key
        name = st.text_input("Your Name (optional)")
        email = st.text_input("Your Email (optional)")
        mood = st.selectbox("How did Soulvest make you feel?", ["😊 Peaceful", "🎶 Uplifted", "😢 Emotional", "🌟 Inspired", "🧘 Other"])
        rating = st.slider("Rate your experience", 1, 5, 4)
        feedback = st.text_area("Your thoughts, suggestions, or appreciation")

        submitted = st.form_submit_button("📨 Submit Feedback")
        if submitted and feedback.strip():
            entry = {
                "name": name,
                "email": email,
                "mood": mood,
                "rating": rating,
                "feedback": feedback.strip(),
                "timestamp": datetime.now().isoformat()
            }
            save_feedback(entry)
            st.success("🙏 Thank you for sharing your heart with Soulvest.")

    # 📥 Load entries and stats
    entries = load_feedback()
    total, daily = get_feedback_stats(entries)

    # 📊 Display stats
    st.markdown("---")
    st.markdown(f"📊 **Total Feedback Entries:** {total}")
    st.markdown(f"📅 **Today's Feedback Entries:** {daily}")

    # 📝 Recent Feedback
    st.markdown("### 📝 Recent Feedback")
    if entries:
        for entry in reversed(entries[-5:]):
            st.markdown(f"**{entry.get('name', 'Anonymous')}** rated it **{entry['rating']}/5** — {entry['mood']}")
            st.write(entry["feedback"])
            st.caption(f"🕒 {entry.get('timestamp', 'Unknown time')}")
    else:
        st.info("No feedback received yet.")

    # 🌈 Emoji Reactions Summary
    mood_counts = Counter(e["mood"] for e in entries)
    st.markdown("### 🌈 Mood Reactions")
    for mood, count in mood_counts.items():
        st.write(f"{mood}: {count}")

    # 📊 Rating Chart
    try:
        ratings = [e["rating"] for e in entries]
        fig, ax = plt.subplots()
        ax.hist(ratings, bins=range(1, 7), edgecolor='black', color='#2E86C1')
        ax.set_title("Soulvest Experience Ratings")
        ax.set_xlabel("Rating")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Could not render chart: {e}")
