import json
from skin_module import CustomSkin

STORAGE_FILE = "storage.json"

# Load custom skins from JSON
def load_custom_skins():
    try:
        with open(STORAGE_FILE, "r") as file:
            data = json.load(file)
            return [
                CustomSkin(
                    item["name"],
                    item["rarity"],
                    item["base_price"],
                    item["image_path"],
                    item["customization_options"],
                )
                for item in data
            ]
    except FileNotFoundError:
        return []

# Save a new custom skin to JSON
def save_custom_skin(name, rarity, base_price, image_path, customization_options):
    new_skin = {
        "name": name,
        "rarity": rarity,
        "base_price": base_price,
        "image_path": image_path,
        "customization_options": customization_options,
    }
    try:
        with open(STORAGE_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(new_skin)
    with open(STORAGE_FILE, "w") as file:
        json.dump(data, file, indent=4)