import streamlit as st

def render_playlist_explorer(composer_thumbnails, composer_bios, composer_playlists, singer_thumbnails, singer_bios, singer_playlists):
    st.title("🎧 Soulvest Playlist Explorer")

    mode = st.radio("Browse by:", ["Tamil Composer", "Singer"], horizontal=True)

    if mode == "Tamil Composer":
        st.markdown("🎶 Soulvest: Tamil Composer Playlists by Decade")

        composer = st.selectbox("🎼 Choose a composer", list(composer_playlists.keys()), key="composer_selector")
        playlist_url = composer_playlists[composer]

        st.subheader(f"🎧 {composer}'s Playlist")
        st.markdown(f"🔗 [Click to listen on YouTube]({playlist_url})")
        st.markdown(f"📎 Playlist URL: `{playlist_url}`")

        if composer in composer_thumbnails:
            st.image(composer_thumbnails[composer], width=300)

        if composer in composer_bios:
            st.markdown(f"📝 **Bio:** {composer_bios[composer]}")

    else:
        st.title("🎤 Soulvest: Singer-Based Playlists")

        selected_singer = st.selectbox("🎙️ Choose a singer", list(singer_playlists.keys()), key="singer_selector")
        singer_url = singer_playlists[selected_singer]

        st.subheader(f"🎶 {selected_singer}'s Playlist")
        st.markdown(f"🔗 [Click to listen on YouTube]({singer_url})")
        st.markdown(f"📎 Playlist URL: `{singer_url}`")

        if selected_singer in singer_thumbnails:
            st.image(singer_thumbnails[selected_singer], width=300)

        if selected_singer in singer_bios:
            st.markdown(f"📝 **Bio:** {singer_bios[selected_singer]}")
