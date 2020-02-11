# Write a class to hold player information
# Players should have inventory?, current room, name?


class Player:
    def __init__(self, current_room):
        self.currentRoom = current_room
        self.inventory = []

    def changeRoom(self, new_room):
        self.currentRoom = new_room

    def addItem(self, item):
        self.inventory.append(item)
    
    def dropItem(self, item):
        if len(self.inventory) > 0:
            item_index = -1
            for index, player_item in enumerate(self.inventory):
                if player_item.name.lower() == item:
                    item_index = index
            if item_index > -1:
                dropped_item = self.inventory.pop(item_index)
                return dropped_item
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
