label room3(player):
    image bg room3 = Transform("room2temp", zoom=.75)
    scene bg room3
    
    show screen game_overlay
    "Evil room 3 text"
    call room3(player)

label room3_2(player): #the version of room 3 entered from the west of room2
    call room3(player)