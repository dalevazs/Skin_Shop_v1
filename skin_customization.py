import streamlit as st
from skin_module import LegendarySkin, SeasonalSkin, CustomSkin
from storage_module import load_custom_skins, save_custom_skin

# Load assets
base_character = "assets/character_base_2.png"

# Define base skins
base_skins = [
    LegendarySkin("Dragon Blaze", "Legendary", 20, "assets/skin_dragon_blaze_2.png", "Flaming Aura"),
    SeasonalSkin("Snowflake", "Epic", 15, "assets/skin_snowflake_2.png", "Winter"),
    CustomSkin("Rainbow", "Rare", 10, "assets/skin_rainbow_2.png", ["Color Change", "Pattern Selection"]),
]

# Combine base skins and custom skins
custom_skins = load_custom_skins()
all_skins = base_skins + custom_skins

# Streamlit UI
st.title("Skin Customization System")

# Display base character
st.subheader("Base Character")
st.image(base_character, caption="Base Character", use_column_width=True)

# Skin selection
skin_names = ["None"] + [skin.name for skin in all_skins]
selected_skin_name = st.selectbox("Choose a skin to apply:", skin_names)

# Display selected skin
selected_skin = None
if selected_skin_name != "None":
    selected_skin = next(skin for skin in all_skins if skin.name == selected_skin_name)
    st.subheader(f"Selected Skin: {selected_skin.name}")
    st.image(selected_skin.image, caption=selected_skin.display_info(), use_column_width=True)
    st.text(selected_skin.display_info())

# Create a new custom skin
st.subheader("Create a Custom Skin")
base_skin_name = st.selectbox("Choose a base skin:", [skin.name for skin in base_skins])
custom_name = st.text_input("Enter a name for your custom skin:")
custom_options = st.text_area("Enter customization options (comma-separated):")

if st.button("Save Custom Skin"):
    if custom_name and custom_options:
        base_skin = next(skin for skin in base_skins if skin.name == base_skin_name)
        customization_list = [opt.strip() for opt in custom_options.split(",")]
        save_custom_skin(
            custom_name,
            base_skin.rarity,
            base_skin.base_price,
            base_skin.image_path,  # Use the stored image path
            customization_list,
        )
        st.success(f"Custom skin '{custom_name}' saved! Reload the app to see it in the dropdown.")
    else:
        st.error("Please provide a name and customization options!")