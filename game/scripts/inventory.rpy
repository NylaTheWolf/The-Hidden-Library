# Script for the inventory system.

# Starting inventory
default inventory = [ item("Box of Matches", "box_of_matches.png"), 
    item("Pocket Knife", "pocket_knife.png"), 
    item("Torn Page", "torn_page.png"),
    item("Crumpled Letter", "crumpled_letter.png"),
    item("Blank Notebook", "blank_notebook.png"),
    item("Fountain Pen", "fountain_pen.png")]

init python:
    class item:
        def __init__(self, name, image):
            self.name = name
            # self.description = description
            self.image = image
    def add_item(name, image):
        inventory[name] = item(name, image)

label open_inventory:
    hide screen game_overlay
    call screen inventory_screen
    # "Back to the game"
    # return
    # "Your Inventory"
    # return
    # $ renpy.pause()

screen inventory_screen:
    modal True
    zorder 10
    text "Inventory" xalign 0.5 yalign 0.1 size 50
    textbutton "Close" xalign 0.5 yalign 0.9 action Return() # closes inventory screen
    # text "success" xalign 0.5 yalign 0.5 size 30
    vpgrid:
        cols 2
        spacing 5
        rows 10
        for i in inventory:
            textbutton i.name:
                xalign 1 yalign 1
                # acti  # shows item info screen when item is clicked
                action Return()