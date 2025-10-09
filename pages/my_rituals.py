import streamlit as st
import json
import os
from datetime import datetime
from collections import Counter

def render_my_rituals():
    st.title("📜 My Ritual Journal")

    if not os.path.exists("my_rituals.json"):
        st.info("No rituals saved yet.")
        return

    with open("my_rituals.json", "r") as f:
        entries = f.readlines()

    if not entries:
        st.info("Your ritual archive is empty.")
        return

    # Parse entries with fallback date
    rituals = []
    for line in entries:
        try:
            data = json.loads(line)
            if "date" not in data:
                data["date"] = datetime.now().strftime("%Y-%m-%d")
            rituals.append(data)
        except json.JSONDecodeError:
            continue

    # 🌈 Tag filtering
    tag_options = ["Peaceful", "Energizing", "Devotional", "Reflective", "Grateful"]
    selected_tag = st.selectbox("🌈 Filter by mood tag", ["All"] + tag_options, key="tag_filter")

    filtered = [
        r for r in rituals
        if selected_tag == "All" or selected_tag.lower() in r.get("tags", [])
    ]

    # 🔍 Search
    search_term = st.text_input("🔍 Search rituals by name or category", key="ritual_search")
    if search_term:
        filtered = [
            r for r in filtered
            if search_term.lower() in r["name"].lower() or search_term.lower() in r["category"].lower()
        ]

    # 📊 Weekly summary
    st.markdown("### 📊 Weekly Ritual Summary")
    week_counts = Counter([r["category"] for r in filtered if r["date"] >= (datetime.now().strftime("%Y-%m-%d"))])
    for category, count in week_counts.items():
        st.write(f"🔸 {category}: {count} saved this week")

    # 🧘 Ritual display
    st.markdown("### 🧘 All Matching Rituals")
    for i, data in enumerate(reversed(filtered)):
        st.markdown(f"**{data['name']}** ({data['category']}) — *{data['date']}*")
        st.code(data["text"])
        st.markdown(f"[🎧 Replay on YouTube]({data['youtube']})")

        # 🗑️ Delete with confirmation
        confirm_key = f"confirm_delete_{i}"
        delete_key = f"delete_{i}"

        st.markdown("---")
        st.checkbox(f"✅ Confirm deletion of '{data['name']}'", key=confirm_key)

        if st.session_state.get(confirm_key):
            if st.button(f"🗑️ Delete '{data['name']}'", key=delete_key):
                updated_entries = []
                for line in entries:
                    try:
                        ritual = json.loads(line)
                        if not (
                            ritual.get("name") == data.get("name") and
                            ritual.get("date") == data.get("date")
                        ):
                            updated_entries.append(line)
                    except json.JSONDecodeError:
                        updated_entries.append(line)

                with open("my_rituals.json", "w") as f:
                    f.writelines(updated_entries)

                st.success(f"Deleted '{data['name']}' from your rituals.")
                st.rerun()

        st.markdown("---")

    # 📁 Export
    if st.button("📁 Export All Rituals to Text"):
        export_text = "\n\n".join([
            f"{r['name']} ({r['category']}) — {r['date']}\n{r['text']}"
            for r in filtered
        ])
        st.download_button("Download Rituals", export_text, file_name="soulvest_rituals.txt")
