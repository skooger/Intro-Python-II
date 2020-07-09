from room import Room
from player import player


# Declare all the rooms

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

#Game helper functions
def print_game(player):
    print(f'{player.name}, {player.room}')
    #add item functionality

def handle_user_input(user_input,player):
    if 'south' in user_input:
        direction = 's_to'
    elif 'north' in user_input:
        direction = 'n_to'
    elif 'east' in user_input:
        direction = 'e_to'
    elif 'west' in user_input:
        direction = 'w_to'
    else:
        direction = ''
    if hasattr(player.room, direction):
        player.room = getattr(player.room, direction)
    elif user_input == '0':
        print(f'Thanks for playing, {player.name}!')
    else:
        print(f'{player.name}, you can\'t go that way.')

# Make a new player object that is currently in the 'outside' room.
name = input('Enter your character name.')
player = Player(name,room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user_input = ' '

while user_input != '0':
    print_game(player)
    user_input = input('''What do you want to do? Type in the direction north/south/west/east
                        Press 0 to quit''')
    handle_user_input(user_input,player)               