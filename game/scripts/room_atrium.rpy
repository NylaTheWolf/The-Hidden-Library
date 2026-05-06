define atriumBaseText = "holy shit what a crazy library"
default atriumText = ""
image bell_idle:
    # anchor (0.5, 0.5)
    "images/interactables/bell.png"
image bell_hover:
    # anchor (0.5, 0.5)
    "images/interactables/bell_hover.png"

label atrium:
    scene bg atrium
    show screen game_overlay
    $ interactables = room_interact_screens["atrium"]
    $ renpy.call_screen(interactables)
    python:
        atriumText = atriumBaseText
        if(playerObj.rooms["atrium"].visited):
            atriumText += " again?" #adds to displayed string for debugging purposes, put proper return text here later
        playerObj.rooms["atrium"].visited = True #sets the room's data as being visited

    "[atriumText]"
    jump investigate
    # call investigate

screen atrium_interactables:
    modal False
    imagebutton xsize 200 ysize 200:
        focus_mask True
        # xsize 20 ysize 20
        # (733, 1122, 135, 88)
        xpos 733 ypos 800
        anchor (0.5, 0.5)
        idle "bell_idle"
        hover "bell_hover"
        action [Jump("ring_bell")]

label ring_bell:
    "You ring the bell."
    call screen atrium_interactables