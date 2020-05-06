from room import Room
from item import Item

# Declare all the rooms

# with open("src/rooms/outside.txt", "r") as f:
#     rooms = f.read()
#     _r = rooms.split(" --\n")
#     print(_r)  # to split the rooms
#     for i in _r:
#         print(i.split(" : "))
#     # print(_r.split(":"))  # to split the name and description


# f.closed

items = {
    'coin': Item("Coin", "a piece of munny"),
    'coin-bag': Item("Coings", "a baggie of coins!"),
    'ruby': Item("Ruby", "a piece of munny"),
    "gem-bag": Item("Gems", "a baggie of gems!"),
    "short-sword":Item("Sword", "A Rusty Short Sword"),
    "small-key":Item("Key","used to unlock any door in this dungeon") # from zelda!
}

rooms = {
    'outside': Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [items["short-sword"]]
    ),
    'foyer': Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and east.",
        []
    ),

    'overlook': Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
        [items['coin'], items['ruby']]
    ),

    'narrow': Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air.",
        []
    ),

    'treasure': Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber!\nBetter Grab the Loot and get out of here!",
        [items['gem-bag'], items['coin-bag']]
    ),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
