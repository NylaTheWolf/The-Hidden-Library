# Script for the inventory system.

# Starting inventory
default inventory = [ item("Box of Matches", "box_of_matches.png"), 
    item("Pocket Knife", "pocket_knife.png"), 
    item("Torn Page", "torn_page.png"),
    item("Crumpled Letter", "crumpled_letter.png"),
    item("Blank Notebook", "blank_notebook.png"),
    item("Fountain Pen", "fountain_pen.png")]

default inventory_slot_count = 21 # Total number of inventory slots available to the player.

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
    # call screen inventory_screen
    show screen inventory_alt
    # "Back to the game"
    show screen game_overlay
    # return
    # "Your Inventory"
    # return
    # $ renpy.pause()

# screen inventory_screen():
#     modal True
#     zorder 101
#     vbox:
#         xpos 0.5 ypos 0.0 # top center
#         xanchor 0.5 yanchor 0.0
#         frame: 
#             background "black"
#             xsize 300
#             text "Inventory" xalign 0.5 yalign 0.5 size 40 color "#FFFFFF"
#     # text "Inventory" at top size 40
#     vbox:
#         # pos (1.0, 0.0) anchor (1.0, 0.0)
#         xpos 0.5 ypos 1.0
#         xanchor 0.5 yanchor 1.0
#         yoffset -50
#         frame: 
#             background "black"
#             xsize 150
#             # xalign 1.0 yalign 0.0
#             textbutton "Close" xalign 0.5 yalign 0.5 action Return() # closes inventory screen
#     # text "success" xalign 0.5 yalign 0.5 size 30
#     vpgrid:
#         cols 4
#         spacing 5
#         rows 10
#         xpos 0.5 ypos 0.5
#         for i in inventory:
#             frame xsize 200 ysize 200:
#                 textbutton i.name:
#                     xalign 1 yalign 1
#                     # acti  # shows item info screen when item is clicked
#                     action NullAction() # placeholder for item info screen action