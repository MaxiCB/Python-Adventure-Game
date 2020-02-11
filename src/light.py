# Light is a subclass of item
# List should have a light level and lit status
from item import Item


class LightSource(Item):
    def __init__(self, name, description, rarity, light_level, lit_status):
        self.light_level = light_level
        self.lit_status = lit_status
        super().__init__(name, description, rarity)

    def print_light(self):
        return "Light Source: {}, {}, {}, {}, {}".format(self.name, self.description, self.rarity, self.light_level, self.lit_status)
