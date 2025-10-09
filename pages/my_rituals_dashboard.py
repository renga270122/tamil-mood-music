import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from pages.rituals_loader import load_rituals, save_rituals, get_ritual_stats

def render_ritual_dashboard():
    st.title("📓 My Rituals Dashboard")

    rituals = load_rituals()
    total, daily = get_ritual_stats(rituals)
    categories = Counter(r["category"] for r in rituals)
    tags = Counter(tag for r in rituals for tag in r.get("tags", []))

    # 🔢 Summary
    st.markdown(f"🧮 **Total Rituals:** {total}")
    st.markdown(f"📅 **Today's Rituals:** {daily}")
    st.markdown("---")

    # 📊 Category Chart
    if categories:
        fig, ax = plt.subplots()
        ax.bar(categories.keys(), categories.values(), color="#7D3C98")
        ax.set_title("Rituals by Category")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    # 🔍 Filter by category
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(categories.keys()))
    filtered = [r for r in rituals if selected_category == "All" or r["category"] == selected_category]

    # 🧘 Ritual Cards
    for i, r in enumerate(reversed(filtered)):
        with st.expander(f"{r.get('name', 'Unnamed')} — {r.get('date', 'Unknown')}"):
            st.write(r.get("text", "No text available"))
            if r.get("youtube"):
                st.markdown(f"[🎧 YouTube]({r['youtube']})")
            st.caption(f"Tags: {', '.join(r.get('tags', []))}")

            # ✅ Confirm + Delete
            confirm_key = f"confirm_delete_{i}"
            delete_key = f"delete_{i}"
            st.checkbox(f"✅ Confirm deletion of '{r['name']}'", key=confirm_key)
            if st.session_state.get(confirm_key):
                if st.button(f"🗑️ Delete '{r['name']}'", key=delete_key):
                    updated = [
                        entry for entry in rituals
                        if not (entry["name"] == r["name"] and entry["date"] == r["date"])
                    ]
                    save_rituals(updated)
                    st.success(f"Deleted '{r['name']}' from your rituals.")
                    st.experimental_rerun()

    # 🌈 Tag Cloud
    if tags:
        st.markdown("### 🌈 Popular Tags")
        for tag, count in tags.most_common(10):
            st.write(f"• {tag} ({count})")
