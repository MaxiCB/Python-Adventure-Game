# Implement a class to hold room information
# Rooms should have a name, and description


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def checkItem(self, item):
        if len(self.items) > 0:
            item_index = -1
            for index, room_item in enumerate(self.items):
                if room_item.name.lower() == item:
                    item_index = index
            if item_index > -1:
                taken_item = self.items.pop(item_index)
                return taken_item
            else:
                return False
        else:
            return False

    def dropItem(self, item):
        self.items.append(item)

    def printItems(self):
        if len(self.items) == 0:
            return "This room seems to have no usable items"
        elif len(self.items) == 1:
            return "a {} can been seen".format(self.items[0])
        elif len(self.items) == 2:
            return "a {} and {} can be seen".format(self.items[0], self.items[1])
        else:
            return "{} can be seen".format(", ".join(item.name for item in self.items))
