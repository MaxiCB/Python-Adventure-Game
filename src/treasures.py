# Treasures have value

from item import Item


class Treasure(Item):


    def __init__(self, name, description, rarity, value):
        self.value = value
        super().__init__(name, description, rarity)

    def print_treasure(self):
        return "Item: {}, {}, {}, {}".format(self.name, self.description, self.rarity, self.value)