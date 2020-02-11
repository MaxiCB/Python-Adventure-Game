# Write a class to hold player information
# Players should have inventory?, current room, name?

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = []

    def changeRoom(self, newRoom):
        self.currentRoom = newRoom