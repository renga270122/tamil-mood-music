import streamlit as st
from datetime import datetime
import json, os, random, pytz
import pandas as pd
import matplotlib.pyplot as plt

# 🔧 Page imports
from pages.home import render_home
from pages.feedback import render_feedback_section
from pages.affirmations import render_affirmation_section
from pages.chants import render_chants
from pages.rituals import render_rituals
from pages.playlist import render_playlist_explorer
from pages.tamil_playlist import render_tamil_playlist
from pages.my_rituals import render_my_rituals
from pages.healing_practices import render_healing_practices

# 🔧 Data imports
from data.composers import composer_thumbnails, composer_bios, composer_playlists
from data.singers import singer_thumbnails, singer_bios, singer_playlists
from data.config import PAGE_NAMES
from pages.app_hits import log_app_hit
from pages.my_rituals_dashboard import render_ritual_dashboard


# Log the visit
if "hit_logged" not in st.session_state:
    log_app_hit()
    st.session_state.hit_logged = True


# 🔧 Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 🔧 Sidebar
st.sidebar.title("🧘 Soulvest Navigation")

nav_options = [
    "Home", "Morning Affirmation", "Night Affirmation", "Healing Chants",
    "Personalized Rituals", "Playlist Explorer",
    "My Rituals", "Feedback","Healing Practices"
]

selected = st.sidebar.radio("Go to:", nav_options, key="sidebar_nav")

if selected != st.session_state.page:
    st.session_state.page = selected
    st.rerun()

# 🔍 Debug
st.write("🔍 Current page:", st.session_state.page)

# 🔧 Routing
page = st.session_state.page

if page == "Home":
    render_home()
elif page == "Morning Affirmation":
    render_affirmation_section(default="Morning")
elif page == "Night Affirmation":
    render_affirmation_section(default="Night")
elif page == "Healing Chants":
    render_chants()
elif page == "Personalized Rituals":
    render_rituals()
elif st.session_state.page == "Playlist Explorer":
    render_playlist_explorer(composer_thumbnails, composer_bios, composer_playlists, singer_thumbnails, singer_bios, singer_playlists)
elif page == "My Rituals":
    render_ritual_dashboard()
elif st.session_state.page == "Healing Practices":
    render_healing_practices()    
elif page == "Feedback":
    render_feedback_section()
else:
    st.error(f"⚠️ Unknown page: {page}")
    render_home()

# 📍 Sidebar footer
st.sidebar.markdown(f"📍 You’re viewing: **{page}**")

# 🌟 Daily Affirmation
daily_affirmations = [
    "I am grounded, grateful, and growing.",
    "My energy is aligned with abundance.",
    "I radiate peace and attract positivity.",
    "I am worthy of love, joy, and success.",
    "I trust the rhythm of my soul."
]
st.sidebar.markdown("### 🌟 Daily Affirmation")
st.sidebar.write(random.choice(daily_affirmations))

# 📅 Current Date & Time
now = datetime.now().strftime("%A, %d %B %Y — %I:%M %p")
st.sidebar.markdown("### 📅 Today")
st.sidebar.write(now)

# 📈 App View Trends
log_file = "app_views_log.json"
today = datetime.now().strftime("%Y-%m-%d")

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        log_data = json.load(f)
else:
    log_data = {}

log_data[today] = log_data.get(today, 0) + 1

with open(log_file, "w") as f:
    json.dump(log_data, f)

df = pd.DataFrame(list(log_data.items()), columns=["Date", "Views"])
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

st.sidebar.markdown("### 📈 App View Trends")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Views"], marker="o", color="#2E86C1")
ax.set_title("Daily App Views")
ax.set_xlabel("Date")
ax.set_ylabel("Views")
ax.grid(True)
st.sidebar.pyplot(fig)

# 💡 Tip of the Day
tips = [
    "Try chanting with breath awareness for deeper calm.",
    "Use morning affirmations to set your intention.",
    "Save your favorite chants to revisit anytime.",
    "Explore Ashtakams for devotional depth.",
    "Reflect on your mood before choosing a ritual."
]
st.sidebar.markdown("### 💡 Tip of the Day")
st.sidebar.write(random.choice(tips))

# 🧘 Mood Selector
st.sidebar.markdown("### 🧘 How are you feeling today?")
mood = st.sidebar.radio("Select your mood", ["😊 Peaceful", "😌 Grateful", "😢 Reflective", "😠 Stressed", "🙏 Seeking"])

# 🕉️ Recent Saved Rituals
if os.path.exists("my_rituals.json"):
    with open("my_rituals.json", "r") as f:
        entries = f.readlines()

    seen = set()
    recent = []
    for line in reversed(entries):
        data = json.loads(line)
        key = (data["category"], data["name"])
        if key not in seen:
            seen.add(key)
            recent.append(data)

    st.sidebar.markdown("### 🕉️ Recent Rituals")
    for data in recent[:3]:
        st.sidebar.markdown(f"- {data['name']} ({data['category']})")
else:
    st.sidebar.info("No rituals saved yet.")

# 🌟 Soulvest Logo (optional)
st.image("soulvest_logo.png", width=250)


#st.video(singer_url)
st.title("🧘 Soulvest: Mantras and Ashtagams")
# 🔱 Invoke Gayatri Mantra selector
render_chants()
st.title("🧘 Soulvest: Affirmations")
render_affirmation_section()

# 📺 Soulvest Channel Embed
st.subheader("📺 Featured Soulvest Video")
st.markdown("""
<iframe width="100%" height="400" src="https://www.youtube.com/embed/EU6srdZF_MA" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.markdown("[🔗 Visit Soulvest Channel](https://www.youtube.com/@soulvest1111)")

render_feedback_section()
