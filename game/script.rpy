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
    # TODO: actually implement the script.
    "You open your eyes to find that your plan worked. You have successfully made it to the hidden library."
    call screen game_overlay
    # "Inventory"
    # return
    # $ renpy.pause()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # TESTING PURPOSES ONLY
screen game_overlay:
    modal True
    frame align (0.5, 1) xsize 500:
        textbutton "Inventory":
            xalign 0.5
            action Call("open_inventory") # opens inventory screen
            # action Show("inventory_screen") # opens inventory screen
    frame align (0.5, 0.5) xsize 500:
        textbutton "Quit":
            xalign 0.5
            action Return() # ends game
# $ renpy.pause()
# pause
# return