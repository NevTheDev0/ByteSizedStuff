import random
import streamlit as st

first_name = [
    "Dead",
    "Rotten",
    "Ugly",
    "Nervous",
    "Sick",
    "Fast",
    "Plastic",
    "Savage",
    "Cheap",
    "Dumb",
    "Broken",
    "Toxic",
    "Cracked",
    "Filthy",
    "Lame",
    "Stupid",
    "Greasy",
    "Paranoid",
    "Empty",
    "Illegal"
]

last_name = [
    "Rats",
    "Bricks",
    "Teeth",
    "Cigs",
    "Bones",
    "Kids",
    "Knives",
    "Trash",
    "Freaks",
    "Coffins",
    "Needles",
    "Doom",
    "Pills",
    "Vans",
    "Guts",
    "Threats",
    "Hooks",
    "Boots",
    "Chains",
    "Punches"
]


optional_addon = [
    "in the Microwave", 
    "of Suburbia", 
    "from Hell", 
    "on Fire", 
    "at Walmart", 
    "& the Trauma", 
    "vs the World", 
    "in Detention", 
    "Reloaded", 
    "2025", 
    "With the stuff", 
    "on VHS", 
    "ft. LoblachiPanMan"
]


st.title("Punk Band Name Generator")
st.markdown("🤘 *If you ever become famous, and you used this, please let me know I would like to attend your concert* 🤘")


if "history" not in st.session_state:
    st.session_state.history = []

if "starred" not in st.session_state:
    st.session_state.starred = []

if st.button("🎸 Generate your Punk Band Name 🔥"):
    name = f"{random.choice(first_name)} {random.choice(last_name)} {random.choice(optional_addon) if random.randint(0,1) else ''}"
    st.session_state.history.append(name)
    st.header(name)

    st.session_state["latest_name"] = name

if "latest_name" in st.session_state:
    if st.button("💾 Save This Banger"):
        name = st.session_state["latest_name"]
        if name not in st.session_state.starred:
            st.session_state.starred.append(name)

if st.session_state.starred:
    st.subheader("⭐ Saved Band Names")
    for name in reversed(st.session_state.starred):
        st.write(f"⭐ {name}")

st.markdown("---")

st.subheader("Your Past Band Names")
for n in st.session_state.history[::-1]:
    st.write(n)
