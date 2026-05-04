label room3:
    image bg room3 = Transform("room3", zoom=.75)
    scene bg room3
    
    show screen game_overlay
    "Evil room 3 text"
    call room3

label room3_2: #the version of room 3 entered from the west of room2
    call room3