import streamlit as st
import json
from datetime import datetime

def render_tamil_playlist():
    st.title("🎶 Tamil Cine Songs Playlist")

    playlists = {
        "Healing & Peaceful": [
            {
                "name": "Anbe Sivam – Theme",
                "youtube": "https://www.youtube.com/watch?v=QWvWZzFzK9I",
                "lyrics": "Anbe Sivam... Love is God"
            },
            {
                "name": "Vaseegara – Minnale",
                "youtube": "https://www.youtube.com/watch?v=ZzvK5QGvZzE",
                "lyrics": "Vaseegara en nenjinikka..."
            }
        ],
        "Devotional & Soulful": [
            {
                "name": "Kurai Ondrum Illai – MS Subbulakshmi",
                "youtube": "https://www.youtube.com/watch?v=9RkZKzFzK9I",
                "lyrics": "Kurai Ondrum Illai Marai Moorthy Kanna..."
            },
            {
                "name": "Isaiyil Thodanguthamma – Hey Ram",
                "youtube": "https://www.youtube.com/watch?v=YzvK5QGvZzE",
                "lyrics": "Isaiyil thodanguthamma..."
            }
        ],
        "Uplifting & Motivational": [
            {
                "name": "Unnai Arindhaal – Yennai Arindhaal",
                "youtube": "https://www.youtube.com/watch?v=VzvK5QGvZzE",
                "lyrics": "Unnai arindhaal uyirai arindhaal..."
            },
            {
                "name": "Vidai Kodu Engal Naade – Kannathil Muthamittal",
                "youtube": "https://www.youtube.com/watch?v=AzvK5QGvZzE",
                "lyrics": "Vidai kodu engal naade..."
            }
        ]
    }

    mood = st.radio("Choose your playlist mood", list(playlists.keys()), key="playlist_mood_selector_playlist")
    selected_song = st.selectbox("Select a song", [song["name"] for song in playlists[mood]], key="playlist_song_selector_playlist")

    if selected_song:
        song = next(s for s in playlists[mood] if s["name"] == selected_song)
        st.markdown(f"### 🎵 {song['name']}")
        st.write(f"📝 Lyrics snippet: *{song['lyrics']}*")
        st.markdown(f"[🎧 Listen on YouTube]({song['youtube']})")

        if st.button(f"💖 Save {song['name']} to My Rituals", key=f"save_song_button_{song['name']}"):
            tags = ["Peaceful"] if mood == "Healing & Peaceful" else ["Devotional"] if mood == "Devotional & Soulful" else ["Energizing"]
            entry = {
                "category": "Tamil Cine Song",
                "name": song["name"],
                "text": song["lyrics"],
                "youtube": song["youtube"],
                "date": datetime.now().strftime("%Y-%m-%d"),
                "tags": tags
            }
            with open("my_rituals.json", "a") as f:
                f.write(json.dumps(entry) + "\n")
            st.success(f"{song['name']} added to your rituals.")
