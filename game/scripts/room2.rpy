label room2(player): #the room with water damaged children's books
    image bg room2 = Transform("room2temp", zoom=.75)
    scene bg room2
    "Room 702a - 18th to 22nd century children's writings - water damaged"
    show screen game_overlay
    show screen minimap(player)
    menu:
        "Where should I go?"
        "The East door":
            $player.move_room("room2", 1, "atrium", 3, 0, 0)
            call atrium(player)
        "The South door":
            $player.move_room("room2", 2, "room3", 0, -200, 200)
            call room3(player)
        "The West door":
            $player.move_room("room2", 3, "room3", 3, -400, 0)
            call room3(player)