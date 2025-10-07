import streamlit as st

# 🌟 Soulvest Logo
st.image("soulvest_logo.png", width=250)

# 🎶 Soulvest: Tamil Mood Music & Chakra Rituals
st.title("🎶 Soulvest: Tamil Mood Music & 🕉️ Chakra Rituals")

# ✅ Verified mood-based playlists by composer with millions of views
composer_playlists = {
    "Happy": {
        "A.R. Rahman": "https://www.youtube.com/playlist?list=PLxIPumcDtzc3YzI-N28cFfwa5JBdxqH6j",  # API Tamil Songs
        "Ilaiyaraaja": "https://www.youtube.com/watch?v=x6f8tyHxFZY",  # Ilaiyaraaja Happy Vibes
        "Yuvan Shankar Raja": "https://www.youtube.com/playlist?list=PLocuwgpJy9A0wUb5S9cTUh-C4yW9xrycP",  # Aldrin Xavier
        "Harris Jayaraj": "https://www.youtube.com/watch?v=Sj3JcTmKosU",  # Tamilian Vlogs Top 15 Hits
        "Vidyasagar": "https://music.youtube.com/playlist?list=PLEgLAfNh0RfSE2DeZIySPwFRYjHNGY4ZW",  # E Songs
        "M.S. Viswanathan": "https://www.youtube.com/playlist?list=PLI9J3C8amofHxZnOAYkHC9dg40upmeyFv"  # Pyramid Glitz Music
    },
    "Sad": {
        "A.R. Rahman": "https://www.youtube.com/playlist?list=PLxIPumcDtzc3YzI-N28cFfwa5JBdxqH6j",
        "Ilaiyaraaja": "https://www.youtube.com/watch?v=x6f8tyHxFZY",
        "Yuvan Shankar Raja": "https://www.youtube.com/playlist?list=PLocuwgpJy9A0wUb5S9cTUh-C4yW9xrycP",
        "Harris Jayaraj": "https://www.youtube.com/watch?v=Sj3JcTmKosU",
        "Vidyasagar": "https://music.youtube.com/playlist?list=PLEgLAfNh0RfSE2DeZIySPwFRYjHNGY4ZW",
        "M.S. Viswanathan": "https://www.youtube.com/playlist?list=PLI9J3C8amofHxZnOAYkHC9dg40upmeyFv"
    },
    "Devotional": {
        "A.R. Rahman": "https://www.youtube.com/playlist?list=PLxIPumcDtzc3YzI-N28cFfwa5JBdxqH6j",
        "Ilaiyaraaja": "https://www.youtube.com/channel/UCVlWr_LN9y80smEMr0KTBOA",
        "Yuvan Shankar Raja": "https://www.youtube.com/playlist?list=PLocuwgpJy9A0wUb5S9cTUh-C4yW9xrycP",
        "Harris Jayaraj": "https://www.youtube.com/watch?v=Sj3JcTmKosU",
        "Vidyasagar": "https://music.youtube.com/playlist?list=PLEgLAfNh0RfSE2DeZIySPwFRYjHNGY4ZW",
        "M.S. Viswanathan": "https://www.youtube.com/playlist?list=PLI9J3C8amofHxZnOAYkHC9dg40upmeyFv"
    }
}

# 🎭 Mood and Composer Selection
mood = st.selectbox("🎭 Select your mood", list(composer_playlists.keys()))
composer = st.selectbox("🎼 Choose your favorite composer", list(composer_playlists[mood].keys()))
playlist_url = composer_playlists[mood][composer]

st.subheader(f"🎧 {composer}'s {mood} Playlist")
st.markdown(f"🔗 [Click to listen on YouTube]({playlist_url})")
st.markdown(f"📎 Playlist URL: `{playlist_url}`")
if "playlist?list=" in playlist_url or "watch?v=" in playlist_url:
    st.video(playlist_url)

# 🕉️ OM Chanting Section
st.subheader("🕉️ Sadhguru's OM Chanting")
st.video("https://www.youtube.com/embed/rCZ78UzGsWU")
st.markdown("Let the sound of OM guide your breath and stillness. Just listen and be present.")

# 🔮 Chakra Ritual Module with Verified Popular Videos
chakra_songs = {
    "Root Chakra (Muladhara)": [
        ("LAM Chanting – Healing Music", "https://www.youtube.com/watch?v=-RBBNJtLatg")
    ],
    "Sacral Chakra (Svadhisthana)": [
        ("VAM Chanting – Cozy Cycles", "https://www.youtube.com/watch?v=6X2IIw5kCJM")
    ],
    "Solar Plexus Chakra (Manipura)": [
        ("RAM Chanting – Meditative Mind", "https://www.youtube.com/watch?v=84tqM81_XgM")
    ],
    "Heart Chakra (Anahata)": [
        ("YAM Chanting – Blossom Everyday", "https://www.youtube.com/watch?v=zuxu4mv8luc")
    ],
    "Throat Chakra (Vishuddha)": [
        ("HAM Chanting – Music for Body and Spirit", "https://www.youtube.com/watch?v=h63rN2z0h2I")
    ],
    "Third Eye Chakra (Ajna)": [
        ("OM Chanting – Chakra VibrAtion", "https://www.youtube.com/watch?v=nTCHrMag07o")
    ],
    "Crown Chakra (Sahasrara)": [
        ("AUM Chanting – Kavita Seth (Swarananda)", "https://www.youtube.com/watch?v=4jzxUpLfDoc")
    ]
}

chakra_affirmations = {
    "Root Chakra": "I am grounded, safe, and secure.",
    "Sacral Chakra": "I embrace pleasure, creativity, and flow.",
    "Solar Plexus Chakra": "I am confident, powerful, and radiant.",
    "Heart Chakra": "I radiate love and compassion.",
    "Throat Chakra": "I speak my truth with clarity and grace.",
    "Third Eye Chakra": "I trust my intuition and inner wisdom.",
    "Crown Chakra": "I am connected to divine consciousness."
}

st.subheader("🧘 Chakra Rituals")
selected_chakra = st.selectbox("Select a Chakra to Explore", list(chakra_songs.keys()))
chakra_key = selected_chakra.split(" ")[0] + " Chakra"

st.markdown(f"💬 **Affirmation:** *{chakra_affirmations.get(chakra_key, '')}*")
st.markdown(f"🎶 **Mantras for {selected_chakra}:**")
for song, url in chakra_songs[selected_chakra]:
    st.markdown(f"- [{song}]({url})")

# 📺 Embed Soulvest YouTube Channel
st.subheader("📺 Featured Soulvest Video")
st.markdown("""
<iframe width="100%" height="400" src="https://www.youtube.com/embed/EU6srdZF_MA" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.markdown("[🔗 Visit Soulvest Channel](https://www.youtube.com/@soulvest1111)")
