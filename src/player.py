# Write a class to hold player information
# Players should have inventory?, current room, name?

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = []

    def changeRoom(self, newRoom):
        self.currentRoom = newRoom

    def addItem(self, item):
        self.inventory.append(item)
    
    def dropItem(self, item):
        if len(self.inventory) > 0:
            itemIndex = -1
            for index, player_item in enumerate(self.inventory):
                if player_item.name.lower() == item:
                    itemIndex = index
            if itemIndex > -1:
                droppedItem = self.inventory.pop(itemIndex)
                return droppedItem
            else:
                return False
        else:
            return False

    def printItems(self):
        if len(self.inventory) == 0:
            return "You have no items, keep looking!"
        elif len(self.inventory) == 1:
            return "You have a {}".format(self.inventory[0])
        elif len(self.inventory) == 2:
            return "You have a {} and {}".format(self.inventory[0], self.inventory[1])
        else:
            return "You have {}".format(", ".join(item.name for item in self.inventory))