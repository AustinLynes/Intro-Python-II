# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, *args):
        self.name = args[0]
        self.cur_room = args[1]


