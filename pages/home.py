import streamlit as st
from utils.welcome import show_welcome_message
from pages.quotes import get_daily_quote
from pages.trivia import get_random_trivia

# 🌟 Soulful Sidebar Trivia
st.sidebar.markdown("### 🎠 Did You Know?")
st.sidebar.markdown("""
<div style='padding: 0.5rem; font-size: 16px; line-height: 1.6; background: #f3e5f5; border-radius: 10px;'>
    <em>{}</em>
</div>
""".format(get_random_trivia()), unsafe_allow_html=True)

st.markdown("### 🌈 Daily Inspiration")
st.info(f"“{get_daily_quote()}”")  


# 📐 Mobile-friendly styling
st.markdown("""
    <style>
        .welcome-banner {
            font-size: 20px;
            line-height: 1.6;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            padding: 1rem;
        }
        .welcome-date {
            font-size: 16px;
            color: #666;
        }
        .welcome-quote {
            font-size: 18px;
            font-style: italic;
            color: #444;
        }
        @media screen and (max-width: 600px) {
            .welcome-banner {
                font-size: 22px;
                padding: 0.5rem;
            }
            .welcome-date {
                font-size: 18px;
            }
            .welcome-quote {
                font-size: 20px;
            }
        }
    </style>
""", unsafe_allow_html=True)


def render_home():  
    # 🌟 Modular welcome message (e.g., time-based greeting, quote)
    show_welcome_message()

    # 🏠 Main title
    st.title("🏠 Welcome to Soulvest Music")

    # 🎶 Intro message
    st.markdown("""
    Soulvest Music is your sanctuary for healing, empowerment, and soulful rituals.  
    Explore affirmations, chants, playlists, and personalized rituals to uplift your spirit.
    """)

    # 💖 Footer
    st.markdown("---")
    st.caption("Crafted with love and devotion 💖 by Soulvest.ai")
