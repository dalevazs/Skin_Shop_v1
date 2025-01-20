from PIL import Image

# Base Skin class
class Skin:
    def __init__(self, name, rarity, base_price, image):
        self.name = name
        self.rarity = rarity
        self.base_price = base_price
        self.image = image

    def calculate_price(self):
        return self.base_price

    def display_info(self):
        return f"{self.name} | {self.rarity} | ${self.calculate_price()}"

# Subclasses for specific skin types
class LegendarySkin(Skin):
    def __init__(self, name, rarity, base_price, image, visual_effects):
        super().__init__(name, rarity, base_price, image)
        self.visual_effects = visual_effects

    def calculate_price(self):
        return self.base_price + 10  # Additional cost for visual effects

    def display_info(self):
        return f"{super().display_info()}, Visual Effects: {self.visual_effects}"

class SeasonalSkin(Skin):
    def __init__(self, name, rarity, base_price, image, season):
        super().__init__(name, rarity, base_price, image)
        self.season = season

    def calculate_price(self):
        return self.base_price + 5  # Additional cost for seasonal availability

    def display_info(self):
        return f"{super().display_info()}, Available During: {self.season}"

class CustomSkin(Skin):
    def __init__(self, name, rarity, base_price, image, customization_options):
        super().__init__(name, rarity, base_price, image)
        self.customization_options = customization_options

    def calculate_price(self):
        return self.base_price + (2 * len(self.customization_options))  # Additional cost per customization option

    def display_info(self):
        return f"{super().display_info()}, Customization Options: {', '.join(self.customization_options)}"