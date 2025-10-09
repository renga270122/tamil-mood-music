import streamlit as st
from utils.welcome import show_welcome_message

from pages.app_hits import load_app_hits, get_hit_stats

hits = load_app_hits()
total_hits, daily_hits = get_hit_stats(hits)

st.markdown(f"📈 **Total App Visits:** {total_hits}")
st.markdown(f"📅 **Today's Visits:** {daily_hits}")


def render_home():
    # 🌟 Modular welcome message (e.g., time-based greeting, quote)
    show_welcome_message()

    # 🏠 Main title
    st.title("🏠 Welcome to Soulvest Music")

    # 🎶 Intro message
    st.markdown("""
    Soulvest Music is your sanctuary for healing, empowerment, and soulful rituals.  
    Explore affirmations, chants, playlists, and personalized rituals to uplift your spirit.
    """)

    # 🌈 Daily inspiration
    st.markdown("### 🌈 Daily Inspiration")
    st.info("“Let your inner music guide your outer journey.”")

    # 💖 Footer
    st.markdown("---")
    st.caption("Crafted with love and devotion 💖 by Soulvest.ai")
