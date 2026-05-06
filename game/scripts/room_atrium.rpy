define atriumBaseText = "holy shit what a crazy library"
default atriumText = ""
image bell_idle:
    # anchor (0.5, 0.5)
    # xysize (200, 200)
    "images/interactables/bell.png"
image bell_hover:
    # anchor (0.5, 0.5)
    # xysize (200, 200)
    "images/interactables/bell_hover.png"

label atrium:
    scene bg atrium
    show screen game_overlay
    show screen atrium_interactables
    # $ interactables = room_interact_screens["atrium"]
    # $ renpy.show_screen(interactables)
    python:
        atriumText = atriumBaseText
        if(playerObj.rooms["atrium"].visited):
            atriumText += " again?" #adds to displayed string for debugging purposes, put proper return text here later
        playerObj.rooms["atrium"].visited = True #sets the room's data as being visited

    "[atriumText]"
    
    # call investigate
    # window hide
    call atrium_interact

label atrium_interact:
    call screen atrium_interactables

screen atrium_interactables():
    modal False
    zorder 102
    imagebutton auto "images/interactables/bell_%s.png":
        focus_mask True
        # xysize (200, 200)
        # anchor (0.5, 0.5)
        pos (500, 800)
        idle "bell_idle"
        hover "bell_hover"
        selected "bell_idle"
        action [Jump("ring_bell")]
    imagebutton auto "images/interactables/zine_%s.png":
        focus_mask True
        pos (1298, 719)
        idle "images/interactables/zine.png"
        hover "images/interactables/zine_hover.png"
        action Jump()

label ring_bell:
    # TODO: Steam achievement
    # TODO: Sound effect
    show bell_idle:
        # anchor (0.5, 0.5)
        # xysize (200, 200)(728, 762, 112, 98)
        pos (500, 800)
    "You ring the bell."
    jump atrium_interact

label read_zine:
    