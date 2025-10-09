import streamlit as st
from app import PAGE_NAMES  # if PAGE_NAMES is defined in app.py and accessible

st.session_state.page = PAGE_NAMES["morning"]
st.rerun()

def render_sidebar():
    st.sidebar.title("🧘 Soulvest Navigation")

    nav_options = {
        "Home": "🏠 Home",
        "Morning Affirmation": "🌅 Morning Affirmation",
        "Night Affirmation": "🌃 Night Affirmation",
        "Healing Chants": "ॐ Healing Chants",
        "Personalized Rituals": "🌺 Personalized Rituals",
        "Playlist Explorer":" 🎵 Playlist Explorer",
        "My Rituals": "💖 My Rituals",
        "Healing Practices": "Healing Practices"
    }

    selected = st.sidebar.radio("Go to:", list(PAGE_NAMES.values()), key="sidebar_nav")
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()

