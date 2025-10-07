import streamlit as st
st.image("soulvest_logo.png", width=250)

# ✅ Updated mood songs with valid YouTube URLs
mood_songs = {
    "Happy": [
        ("Vaathi Coming", "https://www.youtube.com/watch?v=fRD_3vJagxk"),
        ("Anbil Avan", "https://www.youtube.com/watch?v=bXa-wbiXiOw"),
    ],
    "Sad": [
        ("Unakkenna Venum Sollu", "https://www.youtube.com/watch?v=2ATOZ8ndw0U"),
        ("Ennodu Nee Irundhaal", "https://www.youtube.com/watch?v=THHyfxCGs8A"),
    ],
    "Devotional": [
        ("Kurai Ondrum Illai", "https://www.youtube.com/watch?v=idtx3ARDG0E"),
        ("Om Jai Jagdish Hare", "https://www.youtube.com/watch?v=H_9JanyPGso"),
    ]
}

st.title("🎶 Tamil Mood Music & 🕉️ OM Chanting")

# Mood selector
mood = st.selectbox("Select your mood", list(mood_songs.keys()) + ["OM Chanting"])

# Display songs based on mood
if mood in mood_songs:
    st.subheader(f"🎵 Recommended {mood} Songs")
    for song, url in mood_songs[mood]:
        st.markdown(f"[{song}]({url})")

# OM Chanting section
elif mood == "OM Chanting":
    st.subheader("🕉️ Sadhguru's OM Chanting")
    st.video("https://www.youtube.com/watch?v=rCZ78UzGsWU")  # Sadhguru OM Chant
    st.markdown("Let the sound of OM guide your breath and stillness. Just listen and be present.")

# Chakra ritual module with curated popular YouTube URLs
chakra_songs = {
    "Root Chakra (Muladhara)": [
        ("LAM Chanting – Root Chakra Healing", "https://www.youtube.com/watch?v=ycT_XWMD-Zo")  # 100K+ views
    ],
    "Sacral Chakra (Svadhisthana)": [
        ("VAM Chanting – Sacral Chakra Healing", "https://www.youtube.com/watch?v=6X2IIw5kCJM")  # 100K+ views
    ],
    "Solar Plexus Chakra (Manipura)": [
        ("RAM Chanting – Solar Plexus Activation", "https://www.youtube.com/watch?v=jG_ybyCXLNU"),  # 100K+ views
        ("Solar Plexus Guided Meditation", "https://www.youtube.com/watch?v=upWxfS4JzF8")  # 100K+ views
    ],
    "Heart Chakra (Anahata)": [
        ("YAM Chanting – Heart Chakra Healing", "https://www.youtube.com/watch?v=08RqaskbT4A")  # 100K+ views
    ],
    "Throat Chakra (Vishuddha)": [
        ("HAM Chanting – Throat Chakra Meditation", "https://www.youtube.com/watch?v=W6b4Hldi2v8")  # 100K+ views
    ],
    "Third Eye Chakra (Ajna)": [
        ("OM Chanting – Third Eye Activation", "https://www.youtube.com/watch?v=tpg_1F0E-QQ")  # 100K+ views
    ],
    "Crown Chakra (Sahasrara)": [
        ("AUM Chanting – Crown Chakra Meditation", "https://www.youtube.com/watch?v=rRp1sso0xMM")  # 100K+ views
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

