# feedback.py

import streamlit as st
import json
from collections import Counter
import matplotlib.pyplot as plt

def render_feedback_section():
    st.markdown("## 💬 Share Your Experience with Soulvest")

    # 💬 Feedback Form
    with st.form("soulvest_feedback"):
        name = st.text_input("Your Name (optional)")
        email = st.text_input("Your Email (optional)")
        mood = st.selectbox("How did Soulvest make you feel?", ["😊 Peaceful", "🎶 Uplifted", "😢 Emotional", "🌟 Inspired", "🧘 Other"])
        rating = st.slider("Rate your experience", 1, 5, 4)
        feedback = st.text_area("Your thoughts, suggestions, or appreciation")

        submitted = st.form_submit_button("📨 Submit Feedback")
        if submitted:
            entry = {
                "name": name,
                "email": email,
                "mood": mood,
                "rating": rating,
                "feedback": feedback
            }
            with open("soulvest_feedback.json", "a") as f:
                f.write(json.dumps(entry) + "\n")
            st.success("🙏 Thank you for sharing your heart with Soulvest.")

    # 📝 Recent Feedback
    st.markdown("### 📝 Recent Feedback")
    try:
        with open("soulvest_feedback.json", "r") as f:
            entries = f.readlines()[-5:]
            for entry in entries:
                data = json.loads(entry)
                st.markdown(f"**{data.get('name', 'Anonymous')}** rated it **{data['rating']}/5** — {data['mood']}")
                st.write(data["feedback"])
    except FileNotFoundError:
        st.info("No feedback received yet.")

    # 🌈 Emoji Reactions Summary
    try:
        with open("soulvest_feedback.json", "r") as f:
            moods = [json.loads(line)["mood"] for line in f.readlines()]
            mood_counts = Counter(moods)
            st.markdown("### 🌈 Mood Reactions")
            for mood, count in mood_counts.items():
                st.write(f"{mood}: {count}")
    except:
        pass

    # 📊 Rating Chart
    try:
        with open("soulvest_feedback.json", "r") as f:
            ratings = [json.loads(line)["rating"] for line in f.readlines()]
            fig, ax = plt.subplots()
            ax.hist(ratings, bins=range(1, 7), edgecolor='black', color='#2E86C1')
            ax.set_title("Soulvest Experience Ratings")
            ax.set_xlabel("Rating")
            ax.set_ylabel("Count")
            st.pyplot(fig)
    except:
        st.warning(f"Could not render chart: {e}")
