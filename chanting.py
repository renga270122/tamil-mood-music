import streamlit as st
import json
import os

def render_chanting_section():
    st.markdown("## 🕉️ Mantras & Ashtakams")

    chant_types = {
        "Mantras": {
            "Ganesha": {
                "text": "Om Gan Ganapataye Namah",
                "youtube": "https://www.youtube.com/watch?v=3s4Ayg_bMHY"
            },
            "Shiva": {
                "text": "Om Namah Shivaya",
                "youtube": "https://www.youtube.com/watch?v=stzDiC7vNG8"
            },
            "Vishnu": {
                "text": "Om Namo Narayanaya",
                "youtube": "https://www.youtube.com/watch?v=eCNrTEkuAuQ"
            },
            "Lakshmi": {
                "text": "Om Shreem Mahalakshmiyei Namah",
                "youtube": "https://www.youtube.com/watch?v=HEcn2Bvakr4"
            },
            "Durga": {
                "text": "Om Dum Durgayei Namah",
                "youtube": "https://www.youtube.com/watch?v=TwTcZ37QzfQ"
            },
            "Hanuman": {
                "text": "Om Hanumate Namah",
                "youtube": "https://www.youtube.com/watch?v=6DH_6o6c6vE"
            },
            "Lakshmi Narasimhar": {
                "text": "Om Lakshmi Narasimharaya Namah",
                "youtube": "https://www.youtube.com/watch?v=aai1k4SX_uk"
            },
            "Saraswati": {
                "text": "Om Aim Saraswatyai Namah",
                "youtube": "https://www.youtube.com/watch?v=5bYkX3b8HhM"
            },
            "Gayatri": {
                "text": "Om Bhur Bhuvah Swah...",
                "youtube": "https://www.youtube.com/watch?v=ndZ-mBhkPrs"
            },
            "Maha Mrityunjaya": {
                "text": "Om Tryambakam Yajamahe Sugandhim Pushtivardhanam...",
                "youtube": "https://www.youtube.com/watch?v=OV9LXGOXjgs"
            }
        },
        "Ashtakams": {
            "Shiva Ashtakam": {
                "text": "Manojavam Marutatulyavegam Jitendriyam Buddhimatam Varishtham...",
                "youtube": "https://www.youtube.com/watch?v=gXdMyhGX5Fs"
            },
            "Lakshmi Ashtakam": {
                "text": "Namastestu Mahamaye Shri Pithe Surapujite...",
                "youtube": "https://www.youtube.com/watch?v=FrUa0ovoZJQ"
            },
            "Durga Ashtakam": {
                "text": "Sarva Mangala Mangalye Shive Sarvartha Sadhike...",
                "youtube": "https://www.youtube.com/watch?v=SPl0Cs3a5do"
            },
            "Hanuman Chalisa": {
                "text": "Bajrang Bana or Hanuman Ashtak verses...",
                "youtube": "https://www.youtube.com/watch?v=HywkwkCLN4k"
            },
            "Kala Bhairavar Ashtagam": {
                "text": "Om Kala bhairavaya namaha...",
                "youtube": "https://www.youtube.com/watch?v=BsEqI1NZA-E"
            },
            "Vishnu Sahasra Namam": {
                "text": "Om Namo Narayana...",
                "youtube": "https://www.youtube.com/watch?v=ATflA6WOy0I&t=938s"
            },
            "Kanda Sashti kavasam": {
                "text": "Vetrivel Muruganuku Arohara...",
                "youtube": "https://www.youtube.com/watch?v=9rQ1P8GqcUg"
            },
            "Kanda Guru kavasam": {
                "text": "Vetrivel Muruganuku Arohara...",
                "youtube": "https://www.youtube.com/watch?v=wMXQOOnw9cY"
            },
            "Vel Maral": {
                "text": "Vetrivel Muruganuku Arohara...",
                "youtube": "https://www.youtube.com/watch?v=5wQkjC3FR3U"
            }
        }
    }

    chant_category = st.radio("Choose chant type", list(chant_types.keys()))
    selected_chant = st.selectbox("Select chant", list(chant_types[chant_category].keys()))

    if selected_chant:
        chant = chant_types[chant_category][selected_chant]
        st.markdown(f"### {selected_chant}")
        st.code(chant["text"])
        st.video(chant["youtube"])

        if st.button(f"💖 Save {selected_chant} to My Rituals"):
            entry = {
                "category": chant_category,
                "name": selected_chant,
                "text": chant["text"],
                "youtube": chant["youtube"]
            }
            with open("my_rituals.json", "a") as f:
                f.write(json.dumps(entry) + "\n")
            st.success(f"{selected_chant} added to your rituals.")

    # 🧘 My Rituals Dashboard
    st.markdown("## 🧘 My Rituals Dashboard")
    if os.path.exists("my_rituals.json"):
        with open("my_rituals.json", "r") as f:
            entries = f.readlines()

        # Remove duplicates based on (category, name)
        seen = set()
        unique_entries = []
        for line in reversed(entries):  # Show latest first
            data = json.loads(line)
            key = (data["category"], data["name"])
            if key not in seen:
                seen.add(key)
                unique_entries.append(data)

        if unique_entries:
            for data in unique_entries[:5]:  # Show last 5 unique
                st.markdown(f"**{data['name']}** ({data['category']})")
                st.code(data["text"])
                st.markdown(f"[🎧 Replay on YouTube]({data['youtube']})")
        else:
            st.info("No unique rituals found.")
    else:
        st.info("No rituals saved yet.")
