label room3(player):
    image bg room2 = Transform("room2temp", zoom=.75)
    scene bg room2
    
    show screen game_overlay
    show screen minimap(player)
    "Evil room 3 text"