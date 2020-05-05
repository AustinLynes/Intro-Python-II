from room import Room
from player import Player

import os
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

# Make a new player object that is currently in the 'outside' room.

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

commands = ("n", "s", "e", "w", "q")


def clearScreen():
    if os.name == "nt":
        __ = os.system("cls")
    else:
        __ = os.system("clear")


def command_to_dir(command):
    str = ""

    if command == "n":
        str = "Move North"
    elif command == "s":
        str = "Move South"
    elif command == "e":
        str = "Move East"
    elif command == "w":
        str = "Move West"
    elif command == "q":
        str = "QUIT"

    return str
# start of program


def main():
    clearScreen()
    # wether the program should continue
    quit = False
    # create the player and set him inside the outside room
    player = Player("player", room['outside'])
    # while i say to continue. do so...
    global message
    red = '\033[91m'
    red_end = '\033[0m'
    yellow = '\033[93m'
    yellow_end = '\033[0m'
    grey = '\033[90m'
    grey_end = '\033[0m'

    message = ""

    while quit is False:
        # cur_room name
        print(f'{player.cur_room.name}\n')
        # cur_room description

        print(f'{player.cur_room.description}\n')
        # my avalable commands
        # [ N , E, S, W, Q]

        print(f'------------------\n')

        for i in range(len(commands)):
            print(
                f'{grey}> {yellow}{commands[i]}{yellow_end}{grey}:{grey_end} {command_to_dir(commands[i])}')

        print('')
        print(f'------------------\n')

        if(message != ""):
            print(f"{red}{message}{red_end}\n")

        inp = input("Please Enter a Command:  \n").split(" ")

        if inp[0] == "q":
            quit = True

        if command_to_dir(inp[0]) == "Move North":
            message = ""
            if hasattr(player.cur_room, "n_to"):
                player.cur_room = player.cur_room.n_to
            else:
                message = "sorry cannot move North.. chose a different direction.."
        if command_to_dir(inp[0]) == "Move South":
            message = ""
            if hasattr(player.cur_room, "s_to"):
                player.cur_room = player.cur_room.s_to
            else:
                message = "sorry cannot move South.. chose a different direction.."
        if command_to_dir(inp[0]) == "Move East":
            message = ""
            if hasattr(player.cur_room, "e_to"):
                player.cur_room = player.cur_room.e_to
            else:
                message = "sorry cannot move East.. chose a different direction.."
        if command_to_dir(inp[0]) == "Move West":
            message = ""
            if hasattr(player.cur_room, "w_to"):
                player.cur_room = player.cur_room.w_to
            else:
                message = "sorry cannot move West.. chose a different direction.."
            # clear my screen
        clearScreen()


main()
