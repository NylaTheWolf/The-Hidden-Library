# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("")


# The game starts here.



label start:

    $player = playerData()
    $mapManager = mapManager()
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    
    scene bg room
    show atrium 1
    # call atrium
    # TODO: actually implement the script.
    "You open your eyes to find that your plan worked. You have successfully made it to the hidden library."
    call atrium(player)
    show screen game_overlay
    # Player returns here after closing inventory screen
    show screen game_overlay
    pause
    # show screen game_overlay
    
    # "Inventory"
    # return
    # $ renpy.pause()

label loop:
    # call screen game_overlay
    show screen game_overlay
    "What do you want to do?"
    jump loop

    # TESTING PURPOSES ONLY
screen game_overlay:
    # modal True
    frame align (0, 0) xsize 500:
        textbutton "Inventory":
            xalign 0.5
            action Call("open_inventory") # opens inventory screen
            # action Show("inventory_screen") # opens inventory screen
    frame align (0.5, 0.5) xsize 500:
        textbutton "Quit":
            xalign 0.5
            # action Return() # ends game
            action Quit() # ends game
# $ renpy.pause()
# pause
# return