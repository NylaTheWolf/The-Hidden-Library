label room3:
    # image bg room 3
    scene bg room3
    show screen placeholder_interactables
    
    # show screen game_overlay
    "Evil room 3 text"
    # call room3
    call screen placeholder_interactables

label room3_2: #the version of room 3 entered from the west of room2
    call room3
    # call screen placeholder_interactables