# Create all rooms

from player import Player
from room import Room

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
    print(f'Room Information: {currentRoom.description}\n')

playing = True

# Can add print's here to mak the game more polished

while(playing):
    request = input('[N] North [S] South [E] East [W] West [I] Room Info  [Q] Quit\n\n').lower()

    if request == 'q':
        print('\nThanks for playing!')
        playing = False
    elif request == 'n':
        if hasattr(currentRoom, 'n_to'):
            currentRoom = currentRoom.n_to
            character.changeRoom(currentRoom)
            showRoomInfo()
        else:
            print('\nInvalid Input')
    elif request == 's':
        if hasattr(currentRoom, 's_to'):
            currentRoom = currentRoom.s_to
            character.changeRoom(currentRoom)
            showRoomInfo()
        else:
            print('\nInvalid Input')
    elif request == 'e':
        if hasattr(currentRoom, 'e_to'):
            currentRoom = currentRoom.e_to
            character.changeRoom(currentRoom)
            showRoomInfo()
        else:
            print('\nInvalid Input')
    elif request == 'w':
        if hasattr(currentRoom, 'w_to'):
            currentRoom = currentRoom.w_to
            character.changeRoom(currentRoom)
            showRoomInfo()
        else:
            print('\nInvalid Input')
    elif request == 'i':
        print(f'Room Name: {currentRoom.name}')
        print(f'Room Information: {currentRoom.description}\n')