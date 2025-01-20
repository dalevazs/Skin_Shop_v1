import streamlit as st
from skin_module import LegendarySkin, SeasonalSkin, CustomSkin

# Load assets
base_character = "assets/character_base_2.png"

# Define skins
skins = [
    LegendarySkin("Dragon Blaze", "Legendary", 20, "assets/skin_dragon_blaze_2.png", "Flaming Aura"),
    SeasonalSkin("Snowflake", "Epic", 15, "assets/skin_snowflake_2.png", "Winter"),
    CustomSkin("Rainbow", "Rare", 10, "assets/skin_rainbow_2.png", ["Color Change", "Pattern Selection"]),
]

# Streamlit UI
st.title("Skin Customization System")

# Display base character
st.subheader("Base Character")
st.image(base_character, caption="Base Character", use_column_width=True)

# Skin selection
skin_names = ["None"] + [skin.name for skin in skins]
selected_skin_name = st.selectbox("Choose a skin to apply:", skin_names)

# Display selected skin
if selected_skin_name != "None":
    selected_skin = next(skin for skin in skins if skin.name == selected_skin_name)
    st.subheader(f"Selected Skin: {selected_skin.name}")
    st.image(selected_skin.image, caption=selected_skin.display_info(), use_column_width=True)
    st.text(selected_skin.display_info())
else:
    st.subheader("No Skin Selected")
    st.text("Select a skin from the dropdown menu to apply it.")