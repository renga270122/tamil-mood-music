# utils/welcome.py
import streamlit as st
from datetime import datetime
import pytz
import random

def show_welcome_message():
    india_tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india_tz)

    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

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

    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: #f9f5f0; border-radius: 10px;'>
        <h1 style='color: #6a1b9a;'>🙏 {greeting}, and welcome to <span style="color:#d81b60;">Soulvest</span></h1>
        <h3>Your sanctuary for healing music, affirmations, and spiritual growth</h3>
        <p>🗓️ <strong>{today}</strong></p>
        <p style='font-style: italic;'>💬 “{quote}”</p>
    </div>
    """, unsafe_allow_html=True)
