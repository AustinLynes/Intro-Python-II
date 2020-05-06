# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name = ""
    description = ""
    items = {}

    def __init__(self, name, description, items, **kwargs):
        self.name = name
        self.description = description
        self.items = items

