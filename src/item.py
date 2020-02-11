# Implement a class to hold item information
# Items should have a name, description, and rarity level

class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def print_desc(self):
        return "Item: {}, {}".format(self.name, self.description)
    
    def __repr__(self):
        return "{}".format(self.name)

    def __str__(self):
        return "{}".format(self.name)