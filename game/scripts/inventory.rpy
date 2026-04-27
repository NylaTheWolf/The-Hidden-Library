# Script for the inventory system.

# Starting inventory
default inventory = { item("Box of Matches", "box_of_matches.png"), 
    item("Pocket Knife", "pocket_knife.png"), 
    item("Torn Page", "torn_page.png"), 
    item("Crumpled Letter", "crumpled_letter.png"),
    item("Blank Notebook", "blank_notebook.png"),
    item("Fountain Pen", "fountain_pen.png")}

init python:
    class item:
        def __init__(self, name, image):
            self.name = name
            # self.description = description
            self.image = image
    def add_item(name, image):
        inventory[name] = item(name, image)

