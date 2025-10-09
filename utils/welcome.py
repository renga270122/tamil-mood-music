import streamlit as st
from datetime import datetime
import pytz
import random

def show_welcome_message():
    india_tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india_tz)
    hour = now.hour

    # 🌗 Light/Dark mode toggle
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    theme = st.radio("🌓 Choose your theme", ["light", "dark"], index=0 if st.session_state.theme == "light" else 1)
    st.session_state.theme = theme

    # 🌄 Time-based greeting and gradient
    if hour < 12:
        greeting = "Good morning"
        gradient = "linear-gradient(135deg, #fff3e0, #ffe0b2)"  # sunrise
    elif hour < 17:
        greeting = "Good afternoon"
        gradient = "linear-gradient(135deg, #e1f5fe, #b3e5fc)"  # daylight
    else:
        greeting = "Good evening"
        gradient = "linear-gradient(135deg, #ede7f6, #d1c4e9)"  # twilight

    # Override gradient for dark mode
    if theme == "dark":
        gradient = "linear-gradient(135deg, #212121, #424242)"

    today = now.strftime("%A, %d %B %Y — %I:%M %p")
    quotes = [
        "Let your soul sing, and your spirit rise.",
        "You are the light that heals and inspires.",
        "Every breath is a chance to begin again.",
        "Peace begins with a single intention.",
        "Your energy is sacred. Protect it. Share it. Celebrate it.",
        "The universe moves with you when you move with love."
    ]
    quote = random.choice(quotes)

    # 🎨 Styling with animation and theme
    st.markdown(f"""
        <style>
            .soulvest-welcome {{
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 1rem;
                border-radius: 12px;
                margin-bottom: 1rem;
                background: {gradient};
                animation: fadeInBox 1.5s ease-in-out;
            }}
            .soulvest-welcome h1 {{
                color: {'#f8bbd0' if theme == 'dark' else '#6a1b9a'};
                font-size: 28px;
                margin-bottom: 0.5rem;
                text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
            }}
            .soulvest-welcome h3 {{
                font-size: 20px;
                color: {'#e1bee7' if theme == 'dark' else '#4a148c'};
                margin-bottom: 0.5rem;
                text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
            }}
            .soulvest-welcome p {{
                font-size: 16px;
                color: {'#eeeeee' if theme == 'dark' else '#333'};
                margin: 0.3rem 0;
                text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
            }}
            .soulvest-welcome .quote {{
                font-style: italic;
                font-size: 18px;
                color: {'#f5f5f5' if theme == 'dark' else '#444'};
                opacity: 0;
                animation: fadeInQuote 2s ease-in forwards;
                text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
            }}
            @keyframes fadeInQuote {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            @keyframes fadeInBox {{
                from {{ transform: translateY(20px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            @media screen and (max-width: 600px) {{
                .soulvest-welcome h1 {{ font-size: 24px; }}
                .soulvest-welcome h3 {{ font-size: 18px; }}
                .soulvest-welcome p {{ font-size: 17px; }}
                .soulvest-welcome .quote {{ font-size: 19px; }}
            }}
        </style>
    """, unsafe_allow_html=True)

    # 🌟 Welcome banner
    st.markdown(f"""
        <div class="soulvest-welcome">
            <h1>🙏 {greeting}, and welcome to <span style="color:#d81b60;">Soulvest</span></h1>
            <h3>Your sanctuary for healing music, affirmations, and spiritual growth</h3>
            <p>🗓️ <strong>{today}</strong></p>
            <p class="quote">💬 “{quote}”</p>
        </div>
    """, unsafe_allow_html=True)
