from room import Room
from item import Item


items = {
    "coin": Item("Coin", "a piece of munny"),
    "coin-bag": Item("Coings", "a baggie of coins!"),
    "ruby": Item("Ruby", "a piece of munny"),
    "gem-bag": Item("Gems", "a baggie of gems!"),
    "short-sword": Item("Sword", "A Rusty Short Sword"),
    # from zelda!
    "small-key": Item("Key", "used to unlock any door in this dungeon"),
    "nail": Item("Nail", "used for crafting"),
    "pen": Item("Pen", "used for writing")
}

rooms = {
    "front-yard-0": Room(
        "Front Yard: South Entrance",
        "to the north you see a great wooden double door locked with a chain, to the east and west you see open yard and a few bushes",
        []
    ),
    "front-yard-1": Room(
        "Front Yard: East Window",
        "to the north you see a boarded up window woth loosly fit nails a couple of them look like you can remove them. to the east you see more yard and a fountain.",
        [items["nail"]]
    ),
    "front-yard-2": Room(
        "Front Yard: East Fountain",
        "the yard looks like it ends here. but there looks to be something shiny in the fountian!",
        [items["ruby"], items["small-key"]]
    ),
    "front-yard-3": Room(
        "Front Yard: West Window",
        "to the north you see a glass window with nice red satin curtians and a light flickering inside. to the west you see more yard and a fountain.",
        []
    ),
    "front-yard-4": Room(
        "Front Yard: West Garden",
        "the yard looks like it ends here, but rummaging through the flowers you see a few mysterious thing",
        [items["coin"]]
    ),
    "mansion-entrance": Room(
        "Mansion 1F: Entrance Hall",
        "you enter to see a gigantic room with a grand staircase to the north and a door to each the east and west, looking around you see a box. inside it you find a pen.",
        [items["pen"]]
    ),
}

"""

   N
W [X] E
   S


              [ me0 ]
[ fy4 ][ fy3 ][ fy0 ][ fy1 ][ fy2 ]

"""
# region FY 0
# fy0 can move EAST into fy1
rooms["front-yard-0"].e_to = rooms["front-yard-1"]
# fy0 can move WEST into fy3
rooms["front-yard-0"].w_to = rooms["front-yard-3"]
# fy0 can move NORTH into me0
rooms["front-yard-0"].n_to = rooms["mansion-entrance"]
# endregion

# region FY 1
# fy1 can move WEST into fy0
rooms["front-yard-1"].w_to = rooms["front-yard-0"]
# fy1 can move EAST into fy3
rooms["front-yard-1"].e_to = rooms["front-yard-2"]
# endregion

# region FY 2
# fy2 can move west into fy1
rooms["front-yard-2"].w_to = rooms["front-yard-1"]
# endregion

# region FY 3
# fy3 can move EAST into fy0
rooms["front-yard-3"].e_to = rooms["front-yard-0"]
# fy3 can move WEST into fy4
rooms["front-yard-3"].w_to = rooms["front-yard-4"]
# endregion

# region FY 4
# fy4 can move west into fy3
rooms["front-yard-4"].e_to = rooms["front-yard-3"]
# endregion

# region ME 0
# me0 can move SOUTN into fy0
rooms["mansion-entrance"].s_to = rooms["front-yard-0"]
# endregion
