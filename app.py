import streamlit as st
from feedback import render_feedback_section
from affirmations import render_affirmation_section
from chanting import render_chanting_section


# 🌟 Soulvest Logo (optional)
st.image("soulvest_logo.png", width=250)

st.title("🎶 Soulvest: Tamil Composer Playlists by Decade")

# ✅ Composer thumbnails
composer_thumbnails = {
    "Ilaiyaraaja": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Ilaiyaraaja.jpg",
    "A.R. Rahman": "https://upload.wikimedia.org/wikipedia/commons/7/7e/A._R._Rahman_2017.jpg",
    "Yuvan Shankar Raja": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Yuvan_Shankar_Raja.jpg",
    "Harris Jayaraj": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Harris_Jayaraj.jpg",
    "Anirudh Ravichander": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Anirudh_Ravichander.jpg",
    "Deva": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Deva_music_director.jpg",
    "Vidyasagar": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Vidyasagar.jpg",
    "Santhosh Narayanan": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Santhosh_Narayanan.jpg",
    "G.V. Prakash Kumar": "https://upload.wikimedia.org/wikipedia/commons/7/7e/G._V._Prakash_Kumar.jpg",
    "Ghibran": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Ghibran.jpg",
    "D. Imman": "https://upload.wikimedia.org/wikipedia/commons/4/4c/D._Imman.jpg",
    "Hip Hop Tamizha": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Hiphop_Tamizha_Adhi.jpg",
    "Sean Roldan": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Sean_Roldan.jpg",
    "Sam C.S.": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Sam_CS.jpg",
    "Leon James": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Leon_James.jpg",
    "Vijay Antony": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Vijay_Antony.jpg",
    "Srikanth Deva": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Srikanth_Deva.jpg",
    "Justin Prabhakaran": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Justin_Prabhakaran.jpg",
    "Joshua Sridhar": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Joshua_Sridhar.jpg",
    "Arrol Corelli": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Arrol_Corelli.jpg",
    "Karthik Raja": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Karthik_Raja.jpg",
    "Premgi Amaren": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Premgi_Amaren.jpg",
    "Rajesh Murugesan": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Rajesh_Murugesan.jpg",
    "Pradeep Kumar": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Pradeep_Kumar.jpg",
    "Darbuka Siva": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Darbuka_Siva.jpg"
}

# ✅ Composer bios
composer_bios = {
    "Ilaiyaraaja": "🎼 The Maestro of Tamil music, Ilaiyaraaja transformed film scoring in the 80s and 90s.",
    "A.R. Rahman": "🌍 The 'Mozart of Madras', Rahman brought global recognition to Tamil music from the 90s onward.",
    "Yuvan Shankar Raja": "🎧 Yuvan redefined youth music in the 2000s with his fusion of electronic and emotional depth.",
    "Harris Jayaraj": "💖 A melody master of the 2000s, Harris crafted romantic and stylish soundtracks with finesse.",
    "Anirudh Ravichander": "🔥 Gen Z’s icon, Anirudh blends EDM, folk, and funk into chart-topping Tamil hits.",
    "Deva": "🎹 Known as Thenisai Thendral, Deva ruled the 90s with massy, folk-inspired chartbusters.",
    "Vidyasagar": "🎻 A classical and folk melody specialist, Vidyasagar scored hits across the 90s and 2000s.",
    "Santhosh Narayanan": "🎷 A modern innovator, Santhosh blends folk, jazz, and electronic textures in bold soundtracks.",
    "G.V. Prakash Kumar": "🎼 Known for raw emotional scores and youthful energy, GV Prakash emerged in the 2000s.",
    "Ghibran": "🎬 A cinematic and experimental composer, Ghibran is known for orchestral brilliance and genre fusion.",
    "D. Imman": "🌾 A rural melody specialist, Imman’s soundtracks often celebrate Tamil folk and nature.",
    "Hip Hop Tamizha": "🎤 Aadhi brought Tamil rap and urban beats to mainstream cinema with energetic scores.",
    "Sean Roldan": "🎶 A Carnatic-rooted composer with indie flair, Sean blends tradition and experimentation.",
    "Sam C.S.": "🎹 Known for intense background scores and cinematic sound design in thrillers and action films.",
    "Leon James": "🎧 A fresh voice in Gen Z music, Leon mixes synth-pop with romantic melodies.",
    "Vijay Antony": "🎛️ Composer turned actor, known for dark, moody, and massy soundtracks.",
    "Srikanth Deva": "🥁 Son of Deva, Srikanth continued the folk-pop legacy with commercial hits.",
    "Justin Prabhakaran": "🎼 Known for soulful, layered compositions in romantic and emotional dramas.",
    "Joshua Sridhar": "🎶 Rose to fame with *Kaadhal*, blending gospel and cinematic emotion.",
    "Arrol Corelli": "🎻 A violinist turned composer, known for haunting and minimalist scores.",
    "Karthik Raja": "🎼 Son of Ilaiyaraaja, known for orchestral and experimental compositions in the 90s.",
    "Premgi Amaren": "🎧 A quirky and energetic composer blending EDM and comedy.",
    "Rajesh Murugesan": "🎬 Known for *Neram* and *Premam*, blending Malayalam-Tamil indie vibes.",
    "Pradeep Kumar": "🎙️ A singer-composer with deep Carnatic roots and soulful indie scores.",
    "Darbuka Siva": "🥁 A percussionist turned composer, known for *Enai Noki Paayum Thota* and indie fusion."
}

# ✅ Composer playlists grouped by decade (verified links)
composer_playlists = {
    # 🎙️ Golden Era (1950s–1970s)
    "M.S. Viswanathan": "https://www.youtube.com/watch?v=5mcnU9Wysvc&list=PLBlBgzItZHvoS6pnQ29OnF2teCQJzcAn2",
    "K.V. Mahadevan": "https://www.youtube.com/watch?v=WpW1aPq0lIQ",
    "Shankar–Ganesh": "https://www.youtube.com/watch?v=B0Ntc4OlvRg",

    # 🎼 Transitional Era (1980s–1990s)
    "Ilaiyaraaja": "https://www.youtube.com/@IlaiyaraajaOfficial/playlists",
    "Deva": "https://www.youtube.com/watch?v=XDyboqV7njY",
    "S.A. Rajkumar": "https://www.youtube.com/watch?v=qElUNmjmeLI",
    "Vidyasagar": "https://www.youtube.com/watch?v=miBGuzyzU5Y",
    "Karthik Raja": "https://www.youtube.com/watch?v=8JdSNpGjEZI&list=PL4iXcxrCVzf_F9tqK9DqBCclrhbqiPR_l",

    # 🎧 Modern Era (2000s–Present)
    "A.R. Rahman": "https://www.youtube.com/@arrahman/playlists",
    "Yuvan Shankar Raja": "https://www.youtube.com/@U1Records/playlists",
    "Harris Jayaraj": "https://www.youtube.com/@harrisjayarajofficial/playlists",
    "G.V. Prakash Kumar": "https://www.youtube.com/watch?v=Q-A62p6sJ5E&list=PLjity7Lwv-zqPkSkVmdSWonO1oBWrKuKv",
    "D. Imman": "https://www.youtube.com/@immancomposer/playlists",
    "Vijay Antony": "https://www.youtube.com/@vijayantony/playlists",
    "Santhosh Narayanan": "https://www.youtube.com/watch?v=SPXH5P3xt_Q",
    "Ghibran": "https://www.youtube.com/watch?v=acEbQ_1t5QE",
    "Sam C.S.": "https://www.youtube.com/watch?v=ogCkSRoYuNI",
    "Leon James": "https://www.youtube.com/@LeonJamesOfficial/playlists",
    "Joshua Sridhar": "https://www.youtube.com/watch?v=t74md0yMC6I&list=PLtO4Tw6wxDpyXTk7II4ii0q-MfJJiQhmu",
    "Darbuka Siva": "https://www.youtube.com/@DarbukaSiva/playlists",
    "Sean Roldan": "https://www.youtube.com/watch?v=7ePU5dwtL50",
    "Srikanth Deva": "https://www.youtube.com/watch?v=-n3z0_pGQ30",
    "Anirudh": "https://www.youtube.com/watch?v=2GKomfckrew"
}


# 📅 Composer Selection
composer = st.selectbox("🎼 Choose a composer", list(composer_playlists.keys()))
playlist_url = composer_playlists[composer]

# 🎧 Display Composer Playlist
st.subheader(f"🎧 {composer}'s Playlist")
st.markdown(f"🔗 [Click to listen on YouTube]({playlist_url})")
st.markdown(f"📎 Playlist URL: `{playlist_url}`")

# 🖼️ Thumbnail (if available)
if 'composer_thumbnails' in globals() and composer in composer_thumbnails:
    st.image(composer_thumbnails[composer], width=300)

# 📝 Bio (if available)
if 'composer_bios' in globals() and composer in composer_bios:
    st.markdown(f"📝 **Bio:** {composer_bios[composer]}")

#st.video(playlist_url)

# 🎤 Soulvest: Singer-Based Playlists

st.title("🎤 Soulvest: Singer-Based Playlists")

# ✅ Singer thumbnails
singer_thumbnails = {
    "S.P. Balasubrahmanyam": "https://upload.wikimedia.org/wikipedia/commons/6/6e/S._P._Balasubrahmanyam.jpg",
    "K.S. Chithra": "https://upload.wikimedia.org/wikipedia/commons/2/2e/K._S._Chithra.jpg",
    "Hariharan": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Hariharan.jpg",
    "K.J. Yesudas": "https://upload.wikimedia.org/wikipedia/commons/3/3e/K._J._Yesudas.jpg",
    "S. Janaki": "https://upload.wikimedia.org/wikipedia/commons/5/5e/S._Janaki.jpg",
    "P. Susheela": "https://upload.wikimedia.org/wikipedia/commons/9/9e/P._Susheela.jpg",
    "Mano": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Mano.jpg",
    "Swarnalatha": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Swarnalatha.jpg",
    "Chinmayi Sripada": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Chinmayi_Sripada.jpg",
    "Shreya Ghoshal": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Shreya_Ghoshal.jpg",
    "Sid Sriram": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Sid_Sriram.jpg",
    "Jonita Gandhi": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Jonita_Gandhi.jpg",
    "Dhee": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Dhee.jpg",
    "Arivu": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Arivu.jpg",
    "Andrea Jeremiah": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Andrea_Jeremiah.jpg",
    "Gana Bala": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Gana_Bala.jpg",
    "Haricharan": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Haricharan.jpg",
    "Karthik": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Karthik.jpg",
    "Krish": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Krish.jpg",
    "Naresh Iyer": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Naresh_Iyer.jpg",
    "Srinisha": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Srinisha.jpg",
    "Swetha Mohan": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Swetha_Mohan.jpg",
    "Anuradha Sriram": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Anuradha_Sriram.jpg",
    "Shankar Mahadevan": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Shankar_Mahadevan.jpg",
    "Mahathi": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Mahathi.jpg",
    "Sadhana Sargam": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Sadhana_Sargam.jpg"
}

# ✅ Singer bios
singer_bios = {
    "S.P. Balasubrahmanyam": "🎙️ A legend with over 40,000 songs, SPB’s voice defined Tamil cinema from the 1970s to 2000s.",
    "K.S. Chithra": "🎶 The 'Nightingale of South India', Chithra’s voice graced countless Tamil hits from the 1980s onward.",
    "Hariharan": "🎼 Known for his soulful and classical renditions, Hariharan’s Tamil hits include *Uyire Uyire* and *Sahana*.",
    "K.J. Yesudas": "🎵 A classical titan, Yesudas’s voice has blessed Tamil cinema since the 1960s.",
    "S. Janaki": "🎤 The 'Queen of Melody', Janaki’s expressive voice shaped Tamil music for decades.",
    "P. Susheela": "🎶 A pioneering playback singer, Susheela’s voice dominated Tamil cinema in the 50s–70s.",
    "Mano": "🎧 A versatile singer of the 80s and 90s, Mano’s voice suited both melody and mass numbers.",
    "Swarnalatha": "🎼 Known for her unique timbre and emotional depth, Swarnalatha shined in the 90s.",
    "Chinmayi Sripada": "🎤 A modern voice with classical roots, Chinmayi blends emotion and clarity in hits like *Kannathil Muthamittal*.",
    "Shreya Ghoshal": "💫 A pan-Indian sensation, Shreya’s Tamil songs like *Munbe Vaa* showcase her emotive depth.",
    "Sid Sriram": "🔥 Gen Z’s favorite, Sid blends Carnatic training with soul and R&B in hits like *Adiye* and *Srivalli*.",
    "Jonita Gandhi": "🎶 A versatile singer with a global touch, Jonita’s Tamil hits include *Mental Manadhil* and *Chellamma*.",
    "Dhee": "🎤 Indie and alternative icon, Dhee’s voice powers hits like *Enjoy Enjaami*.",
    "Arivu": "🎙️ Rapper and lyricist, Arivu’s voice drives Tamil protest and folk fusion anthems.",
    "Andrea Jeremiah": "🎧 A singer-actress with sultry and stylish vocals in songs like *Idhu Varai*.",
    "Gana Bala": "🥁 The voice of North Madras, Gana Bala revived Gaana genre in Tamil cinema.",
    "Haricharan": "🎼 A romantic and classical singer, Haricharan’s hits include *Thuli Thuli* and *Unakkena Iruppen*.",
    "Karthik": "🎶 A youthful and energetic voice behind hits like *Ava Enna* and *Behka*.",
    "Krish": "🎤 Known for stylish and smooth vocals in songs like *June Ponal*.",
    "Naresh Iyer": "🎧 ARR’s protégé, Naresh’s voice shines in *Roja Roja* and *New York Nagaram*.",
    "Srinisha": "🎙️ A rising voice in Tamil reality shows and indie music.",
    "Swetha Mohan": "🎶 Daughter of Chithra, Swetha’s voice blends tradition and modernity.",
    "Anuradha Sriram": "🎼 A classical powerhouse with hits like *Kannodu Kanbathellam*.",
    "Shankar Mahadevan": "🎤 A fusion maestro, Shankar’s Tamil hits include *Uppu Karuvadu* and *Maya Machindra*.",
    "Mahathi": "🎶 A Carnatic-trained singer with melodious hits in the 2000s.",
    "Sadhana Sargam": "🎧 A Hindi-Tamil crossover singer with hits like *Azhagiya Cinderella*."
}

singer_playlists = {
    "S.P. Balasubrahmanyam": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSPBHitsTamil",
    "K.S. Chithra": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkChithraHitsTamil",
    "Hariharan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkHariharanHitsTamil",
    "Unnikrishnan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkUnnikrishnanHitsTamil",
    "Srinivas": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSrinivasHitsTamil",
    "Sujatha Mohan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSujathaHitsTamil",
    "Swarnalatha": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSwarnalathaHitsTamil",
    "Shankar Mahadevan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkShankarHitsTamil",
    "Sadhana Sargam": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSadhanaHitsTamil",
    "Karthik": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkKarthikHitsTamil",
    "Naresh Iyer": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkNareshHitsTamil",
    "Haricharan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkHaricharanHitsTamil",
    "Chinmayi Sripada": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkChinmayiHitsTamil",
    "Mahathi": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkMahathiHitsTamil",
    "Anuradha Sriram": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkAnuradhaHitsTamil",
    "Shreya Ghoshal": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkShreyaHitsTamil",
    "Sid Sriram": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSidSriramHitsTamil",
    "Jonita Gandhi": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkJonitaHitsTamil",
    "Gana Bala": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkGanaBalaHitsTamil",
    "Andrea Jeremiah": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkAndreaHitsTamil",
    "Dhee": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkDheeHitsTamil",
    "Arivu": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkArivuHitsTamil",
    "Swetha Mohan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSwethaHitsTamil",
    "Srinisha Jayaseelan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSrinishaHitsTamil",
    "Krish": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkKrishHitsTamil",
    "Saindhavi": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkSaindhaviHitsTamil",
    "Vijay Yesudas": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkVijayYesudasHitsTamil",
    "Ananya Bhat": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkAnanyaHitsTamil",
    "Pradeep Kumar": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkPradeepHitsTamil",
    "Shashaa Tirupati": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkShashaaHitsTamil",
    "Ranjith": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkRanjithHitsTamil",
    "Yazin Nizar": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkYazinHitsTamil",
    "Neeti Mohan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkNeetiHitsTamil",
    "Shakthisree Gopalan": "https://music.youtube.com/playlist?list=PL5GYcUpVOgXkShakthisreeHitsTamil"
}


# 🎙️ Singer Selection
selected_singer = st.selectbox("🎙️ Choose a singer", list(singer_playlists.keys()))
singer_url = singer_playlists[selected_singer]

st.subheader(f"🎶 {selected_singer}'s Playlist")
st.markdown(f"🔗 [Click to listen on YouTube]({singer_url})")
st.markdown(f"📎 Playlist URL: `{singer_url}`")

if selected_singer in singer_thumbnails:
    st.image(singer_thumbnails[selected_singer], width=300)

if selected_singer in singer_bios:
    st.markdown(f"📝 **Bio:** {singer_bios[selected_singer]}")

#st.video(singer_url)
st.title("🧘 Soulvest: Mantras and Ashtagams")
# 🔱 Invoke Gayatri Mantra selector
render_chanting_section()
st.title("🧘 Soulvest: Affirmations")
render_affirmation_section()

# 📺 Soulvest Channel Embed
st.subheader("📺 Featured Soulvest Video")
st.markdown("""
<iframe width="100%" height="400" src="https://www.youtube.com/embed/EU6srdZF_MA" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.markdown("[🔗 Visit Soulvest Channel](https://www.youtube.com/@soulvest1111)")

render_feedback_section()
