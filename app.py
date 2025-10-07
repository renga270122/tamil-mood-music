import streamlit as st

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
