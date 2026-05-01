# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show atrium 1
    # call atrium
    # TODO: actually implement the script.
    show screen game_overlay
    # show screen HUD
    "You open your eyes to find that your plan worked. You have successfully made it to the hidden library."
    # show screen game_overlay
    # Player returns here after closing inventory screen
    # "This is to make sure a player can access their inventory at any time during the game."
    # pause
    jump atrium
    
    # "Inventory"
    # return
    # $ renpy.pause()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

# TESTING PURPOSES
label loop:
#     # call screen game_overlay
    show screen game_overlay
    "What do you want to do?"
    "This is to make sure a player can access their inventory at any time during the game."
    jump loop

screen game_overlay:
    modal False
    zorder 100
    # frame pos (0, 0) xsize 150 ysize 60:
    #     # textbutton "Inventory":
    #     # text "Inventory" xalign 0.5 yalign 0.5 size 30
    #     # has hbox
    #     background None
    imagebutton auto "inventory_button_%s.png" xsize 150 ysize 60:
        focus_mask True
        xpos 0 ypos 0
        xanchor 0 yanchor 0
        # xoffset -4 yoffset -5.5
        # xalign 0.0 yalign 0.0
        # xalign 0.5 yalign 0.5
        # padding (10,10,10,10)
        idle "components/inventory/images/inventory_button.png"
        hover "components/inventory/images/inventory_button_hover.png"
        # action Call("open_inventory") # opens inventory screen
        action Show("inventory_alt") # opens inventory screen
    # frame align (0.5, 0.5) xsize 500:
    #     textbutton "Quit":
    #         xalign 0.5
    #         # action Return() # ends game
    #         action Quit() # ends game
# $ renpy.pause()
# pause
# return