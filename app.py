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

# Chakra ritual module with valid YouTube URLs
chakra_songs = {
    "Root Chakra (Muladhara)": [
        ("Bhumi Devi Stotram", "https://www.youtube.com/watch?v=Z2qVwJZ7PzE"),
        ("Om Lam Chant", "https://www.youtube.com/watch?v=JZzKzZ1PqZQ")
    ],
    "Sacral Chakra (Svadhisthana)": [
        ("Om Vam Chant", "https://www.youtube.com/watch?v=GoJdOUSBCmo")
    ],
    "Solar Plexus Chakra (Manipura)": [
        ("Om Ram Chant", "https://www.youtube.com/watch?v=dveOdwmB-Pc")
    ],
    "Heart Chakra (Anahata)": [
        ("Shiva Shambho", "https://www.youtube.com/watch?v=GPe268zbINg"),
        ("Om Yam Chant", "https://www.youtube.com/watch?v=e8HBVKmkgj4")
    ],
    "Throat Chakra (Vishuddha)": [
        ("Om Ham Chant", "https://www.youtube.com/watch?v=FFeviHnotek")
    ],
    "Third Eye Chakra (Ajna)": [
        ("Om Sham Chant", "https://www.youtube.com/watch?v=yIDE-0X46Bo")
    ],
    "Crown Chakra (Sahasrara)": [
        ("OM Chanting for Crown Chakra", "https://www.youtube.com/watch?v=09rowVTVSb8")
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