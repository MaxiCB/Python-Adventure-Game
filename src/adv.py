# Create all rooms

from player import Player
from item import Item
from room import Room

item = {
    'torch':    Item('Torch', 'This may prove useful', 'Un-Common'),
    'lighter':    Item('Lighter', 'Maybe we can just burn the place down', 'Common'),
    'skull':    Item('Skull', 'Well this makes me uncomfortable', 'Common'),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['torch'], item['skull']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link all rooms together after creation

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create a new player
# Place player in 'Outside' room

currentRoom = room['outside']
character = Player(currentRoom)

# Write a loop
# * Prints current room name
# * Prints the current room description
# * Waits for user input
# * Decides what action to take based on the input
# If the user inputs a cardinal direction (n, s, e, w), attempt to move to the room in that direction
# Print a error message if the move is invalid

# If the user enter 'q' exit the game

# Function to display current room information on changing of current room
def showRoomInfo():
    print(f'Room Name: {currentRoom.name}')
    print(f'Room Description: {currentRoom.description}')
    print(f'Room Items: {currentRoom.printItems()}\n')


playing = True

# Can add print's here to mak the game more polished

while(playing):
    request = input('[N] North [S] South [E] East [W] West [I] Room Info [B] Player Info [T <Item>] Take Item [D <Item>] Drop Item  [Q] Quit\n\n').lower().split(' ')

    if len(request) == 1:
        if request[0] == 'q':
            print('\nThanks for playing!')
            playing = False
        elif request[0] == 'n':
            if hasattr(currentRoom, 'n_to'):
                currentRoom = currentRoom.n_to
                character.changeRoom(currentRoom)
                showRoomInfo()
            else:
                print('\nInvalid Input')
        elif request[0] == 's':
            if hasattr(currentRoom, 's_to'):
                currentRoom = currentRoom.s_to
                character.changeRoom(currentRoom)
                showRoomInfo()
            else:
                print('\nInvalid Input')
        elif request[0] == 'e':
            if hasattr(currentRoom, 'e_to'):
                currentRoom = currentRoom.e_to
                character.changeRoom(currentRoom)
                showRoomInfo()
            else:
                print('\nInvalid Input')
        elif request[0] == 'w':
            if hasattr(currentRoom, 'w_to'):
                currentRoom = currentRoom.w_to
                character.changeRoom(currentRoom)
                showRoomInfo()
            else:
                print('\nInvalid Input')
        elif request[0] == 'i':
            # Shot the room information again
            showRoomInfo()
        elif request[0] == 'b':
            # Show the players inventory
            print(f'Player Items: {character.printItems()}\n')
    elif len(request) == 2:
        if request[0] == 'take':
            # Need to check room to see if current item is available
            takenItem = currentRoom.checkItem(request[1])
            if takenItem:
                # Need to add item to character inventory
                character.addItem(takenItem)
                print(f'\n{takenItem} has been picked up!')
            else: 
                print('Invalid input')
        elif request[0] == 'drop':
            droppedItem = character.drop(request[1])
            if droppedItem:
                # Need to add the dropped item to the current room
                currentRoom.dropItem(droppedItem)
                print(f'\n{droppedItem} has been dropped!')
            else:
                print('Invalid input')
        else:
            print('Invalid input')
    else:
        print('Invalid input')