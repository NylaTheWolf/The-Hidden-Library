label room2: #the room with water damaged children's books
    # image bg room 2
    scene bg room 2
    $ interactables = room_interact_screens[playerObj.lastRoom]
    $ renpy.hide_screen(interactables)
    show screen placeholder_interactables
    "Room 702a - 18th to 22nd century children's writings - water damaged"
    # show screen 
    call screen placeholder_interactables

# screen room2_interactables:
    

screen placeholder_interactables:
    text "placeholder" pos (0.0, 0.0)