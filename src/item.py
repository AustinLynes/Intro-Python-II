# item should  have a name and a description
# name should one word. easier for parsing..


class Item:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f"You took the {self.name}."

    def on_drop(self):
        return f"you dropped {self.name}."
