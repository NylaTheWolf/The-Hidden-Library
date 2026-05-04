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
    call atrium(player)
