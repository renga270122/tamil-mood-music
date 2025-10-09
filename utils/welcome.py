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

    # 🌈 Styling block
    st.markdown("""
        <style>
            .soulvest-welcome {
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 1rem;
                border-radius: 12px;
                margin-bottom: 1rem;
                background: linear-gradient(135deg, #fce4ec, #f3e5f5);
            }
            .soulvest-welcome h1 {
                color: #6a1b9a;
                font-size: 28px;
                margin-bottom: 0.5rem;
            }
            .soulvest-welcome h3 {
                font-size: 20px;
                color: #333;
                margin-bottom: 0.5rem;
            }
            .soulvest-welcome p {
                font-size: 16px;
                color: #555;
                margin: 0.3rem 0;
            }
            .soulvest-welcome .quote {
                font-style: italic;
                font-size: 18px;
                color: #444;
                opacity: 0;
                animation: fadeIn 2s ease-in forwards;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @media screen and (max-width: 600px) {
                .soulvest-welcome h1 {
                    font-size: 24px;
                }
                .soulvest-welcome h3 {
                    font-size: 18px;
                }
                .soulvest-welcome p {
                    font-size: 17px;
                }
                .soulvest-welcome .quote {
                    font-size: 19px;
                }
            }
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
