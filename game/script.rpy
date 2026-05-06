# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("")


# The game starts here.

default playerObj = playerData()
default mapManager = minimapManager()
image bg atrium:
    "images/bg atrium.jpg"
    xysize(1920, 1080)

# config.layers
# $ renpy.add_layer("hud_layer", above="screens")
default interactables = ""

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg atrium
    # $ interactables = room_interact_screens["atrium"]
    # $ renpy.show_screen(interactables)
    show screen atrium_interactables

    $ initial_inventory_setup()
    $ minimap_open = False # whether the minimap is currently open
    show screen game_overlay onlayer hud_layer

    "You open your eyes to find that your plan worked. You have successfully made it to the hidden library."
    # Player returns here after closing inventory screen
    # "This is to make sure a player can access their inventory at any time during the game."
    # pause
    jump atrium
    
    # "Inventory"
    # return
    # $ renpy.pause()

screen game_overlay:
    tag hud
    modal False
    # zorder 106
    # TODO: Make a nicer inventory button with an icon.
    # TODO: Add tooltip overlay to items?
    imagebutton auto "inventory_button_%s.png" xsize 150 ysize 60:
        focus_mask True
        xpos 0 ypos 0
        xanchor 0 yanchor 0
        idle "components/inventory/images/inventory_button.png"
        hover "components/inventory/images/inventory_button_hover.png"
        action Show("inventory_alt") # opens inventory screen
    frame align (.5, 0) xsize 500:
        textbutton "Map":
            xalign .5
            if (not minimap_open):
                action [Show("minimap"), SetVariable("minimap_open", True)]
            else:
                action [Hide("minimap"), SetVariable("minimap_open", False)]