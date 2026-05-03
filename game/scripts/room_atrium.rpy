define atriumBaseText = "holy shit what a crazy library"
default atriumText = ""

label atrium(player):
    image bg atrium = Transform("atrium 1", zoom=.75)
    scene bg atrium
    python:
        atriumText = atriumBaseText
        if(player.rooms["atrium"].visited):
            atriumText += " again?" #adds to displayed string for debugging purposes, put proper return text here later
        player.rooms["atrium"].visited = True #sets the room's data as being visited

    "[atriumText]"

    show screen game_overlay
    show screen minimap(player)

    menu: #note for menus, we could implement context sensitive direciton based on where the player entered from, but only if we have time
        "Where should I go?"
        "The West door":
            $player.move_room("atrium", 3, "room2", 1, -200, 0)
            call room2(player)
        "The East door":
            $player.rooms["room6"].enterDirection = "East"
            call room6(player)

    call atrium(player)