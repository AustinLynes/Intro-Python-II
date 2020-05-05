# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, *args):
        self.name = args[0]
        self.description = args[1]
        if len(args) > 2:
            self.n_to = args[2]
            self.s_to = args[3]
            self.e_to = args[4]
            self.w_to = args[5]
