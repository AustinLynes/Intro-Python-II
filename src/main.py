import os

from player import Player
from level import rooms
from item import Item

commands = ["north", "south", "east", "west", "quit"]

# clear screen


def clear_screen():
    # if im on windows.. use cls
    if os.name == "nt":
        __ = os.system("cls")
    # else im on sonmething unix based.. so clear will work
    else:
        __ = os.system("clear")


def seperator(str):
    return ((85-len(str)) * "-") + str


def right_justify(str):
    return ((95-len(str)) * " ") + str


def right_justify_help(str):
    return ((85-len(str)) * " ") + str


def main():
    # cleaning the screen..
    # doing this at the begining and end of the frame allows for consistency
    # on the display.
    clear_screen()  # pre render clean

    # clear the screen on the first pass.
    # clear_screen()
    # wether the program should continue
    # True triggers a quit
    # create the player and set him inside the outside room
    player = Player(name="player", cur_room=rooms["front-yard-0"])
    # while i say to continue. do so...
    quit = False
    inventory_open = False
    commands_open = False
    # console information

    yellow = "\033[93m"
    yellow_end = "\033[0m"

    grey = "\033[90m"
    grey_end = "\033[0m"

    blue = "\033[94m"
    blue_end = "\033[0m"

    error_msg = ""
    red = "\033[91m"
    red_end = "\033[0m"

    confirm_msg = ""
    green = "\033[92m"
    green_end = "\033[0m"

    def handle_commands(command_list, player):

        nonlocal confirm_msg, error_msg, quit, room_has_items, inventory_open, commands_open
        error_msg = ""
        confirm_msg = ""
        # if the user initiates the __MOVE__ super command ===>  `move` or `mv`
        if command_list[0] == "move" or command_list[0] == "mv":
            # if the user initiates the __NORTH__ direction ===>  `north` or `n`
            if not len(command_list) > 1:
                error_msg = "please specify a <direction> if you want to move. ex: n, s, e, w"
                return  # short circut if there is not a first command

            if command_list[1] == "n" or command_list[1] == "north":
                if "n_to" in dir(player.cur_room):
                    player.move(player.cur_room.n_to)
                else:
                    error_msg = "sorry cannot move North.. chose a different direction.."
            # if the user initiates the __SOUTH__ direction ===>  `south` or `s`
            elif command_list[1] == "s" or command_list[1] == "south":
                if "s_to" in dir(player.cur_room):
                    player.move(player.cur_room.s_to)
                else:
                    error_msg = "sorry cannot move South.. chose a different direction.."
            # if the user initiates the __EAST__ direction ===>  `east` or `e`
            elif command_list[1] == "e" or command_list[1] == "east":
                if "e_to" in dir(player.cur_room):
                    player.move(player.cur_room.e_to)
                else:
                    error_msg = "sorry cannot move East.. chose a different direction.."
            # if the user initiates the __WEST__ direction ===>  `west` or `w`
            elif command_list[1] == "w" or command_list[1] == "west":
                if "w_to" in dir(player.cur_room):
                    player.move(player.cur_room.w_to)
                else:
                    error_msg = "sorry cannot move West.. chose a different direction.."

        # if the user initiates the __TAKE__ super command ===>  `take` or `tk`
        elif command_list[0] == "tk" or command_list[0] == "take":
            # if there are no items
            if not len(command_list) > 1:
                error_msg = "please specify a item if you want to take something. note.. if a room has no items you cannot take anything."
                return  # short circut if there is nothing specified to grab

            if not room_has_items:
                error_msg = "Sorry no items to take..."
                return  # short circut if there is nothing specified to grab
            # else look through the players items and see if the command works.. if so.. then do it
            else:
                # look through all the players current rooms' items
                for (ind, el) in enumerate(player.cur_room.items):
                    # if any of the elements names match the command entered capitolized
                    if(el.name == command_list[1].capitalize()):
                        # then add that item to the players inventory
                        player.add_to_inventory(player.cur_room.items[ind])
                        confirm_msg = player.cur_room.items[ind].on_take()
                        # finally remove it from the room
                        player.cur_room.items.remove(
                            player.cur_room.items[ind])
        elif command_list[0] == "dr" or command_list[0] == "drop":
            # check the commands to see if there is a seccond argument..
            # this is expected..
            if not len(command_list) > 1:
                error_msg = "please specify a item if you want to drop something."
                return  # short circut if there is nothing specified to drop
            # check to see if the player has items to drop
            # if the inventorys emtpy we need to short circut also..
            if not len(player.inventory) > 0:
                error_msg = "please specify a item if you want to drop something."
            else:
                for (ind, el) in enumerate(player.inventory):
                    if el.name == command_list[1].capitalize():
                        player.cur_room.items.append(player.inventory[ind])
                        player.drop_item(player.inventory[ind])
        # open inventory
        elif command_list[0] == "i" or command_list[0] == "inventory":
            if inventory_open is False:
                inventory_open = True
            else:
                inventory_open = False
        elif command_list[0] == "--help":
            if commands_open is False:
                commands_open = True
            else:
                commands_open = False
        elif command_list[0] == "q" or command_list[0] == "quit()":
            quit = True

    while quit is False:

        # region ROOM INFORMATION
        # cur_room name
        print('\n\n\n')
        print(f"{player.cur_room.name}\n")
        # cur_room description

        print(f"{player.cur_room.description}\n")
        print(f"  in the room you see...\n")

        room_has_items = len(player.cur_room.items) > 0

        if room_has_items:
            for ind in range(len(player.cur_room.items)):
                print(f"  {grey}>{grey_end} {player.cur_room.items[ind].name}")
        else:
            print(f"  {grey}>{grey_end} nothing{grey}...{grey_end}")
        # my avalable commands
        # [ N , E, S, W, Q]
        # endregion
        # region INVENTORY
        if inventory_open:
            print(f"\n{grey}{seperator(f'{grey_end} Inventory')}\n")
            inventory_empty = len(player.inventory) == 0
            if not inventory_empty:
                for ind in range(len(player.inventory)):
                    print(f" > {player.inventory[ind].name}")
            else:
                print(f"{grey}empty{grey_end}")
        # endregion

        print(f'\n{grey}{seperator("--")}{grey_end}\n\n{grey}{right_justify_help("--help for commands")}{grey_end}\n')

        if(len(error_msg) != 0):
            print(f"{red}{error_msg}{red_end}\n")
        if(len(confirm_msg) != 0):
            print(f"{green}{confirm_msg}{green_end}\n")

        # region COMMANDS
        if commands_open:
            print(f"command:")
            print(f"{grey}>{grey_end} Move{grey}:{grey_end}" +
                  right_justify(f"{yellow}mv{yellow_end} or {yellow}move{yellow_end}"))
            movement = [x for x in commands[:4]]
            if room_has_items:
                print(f"{grey}>{grey_end} Take{grey}:{grey_end}" +
                      right_justify(f"{yellow}tk{yellow_end} or {yellow}take{yellow_end}"))
            print(f"direction:")
            for (ind, el) in enumerate(movement):
                print(
                    f"{grey}>{grey_end} {el.capitalize()}{grey}:{grey_end}" + right_justify(f"{yellow}{commands[ind][:1]}{yellow_end} or {yellow}{commands[ind]}{yellow_end}"))
            application = [x for x in commands[4:]]
            print("application:")
            for (ind, el) in enumerate(application):
                print(
                    f"{grey}>{grey_end} {el.capitalize()}{grey}:{grey_end}" + right_justify(f"{yellow}{application[ind][:1]}{yellow_end} or {yellow}{application[ind]}{yellow_end}"))
        # endregion

        # region HELP
            print(seperator('---\n'))
            print(
                f"to move please input {yellow}<command>{yellow_end} + {yellow}<direction>{yellow_end} \n\nex: {yellow}mv n{yellow_end} or {yellow}move north{yellow_end}\n")
            print(seperator('---\n'))
        # endregion

        command = input(
            f"{blue}Please Enter a Command{blue_end}:\n\n").split(" ")

        handle_commands(command, player)
        clear_screen()  # post render clean


main()
