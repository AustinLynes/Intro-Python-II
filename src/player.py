# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    name = ""
    cur_room = None
    inventory = []

    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room

    def move(self, direction):
        self.cur_room = direction

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
