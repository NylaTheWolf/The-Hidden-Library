image papers_idle:
    "images/interactables/papers.png"
    
image papers_hover:
    "images/interactables/papers_hover.png"

label room2: #the room with water damaged children's books
    # image bg room 2
    scene bg room 2
    $ interactables = room_interact_screens[playerObj.lastRoom]
    $ renpy.hide_screen(interactables)
    show screen placeholder_interactables
    "Room 702a - 18th to 22nd century children's writings - water damaged"
    # show screen 
    call room2_interact

label room2_interact:
    call screen room2_interactables

screen room2_interactables:
    imagebutton auto "images/interactables/papers_%s.png":
        focus_mask True
        pos (971, 900)
        idle "papers_idle"
        hover "papers_hover"
        action Jump("examine_papers")

label examine_papers:
    show papers_idle:
        pos (971, 900)
    "A stack of colorful papers sits in disorder on the bottom shelf."
    menu:
        "Look closer.":
            "You kneel to look more closely. They’re…"
            "{i}Wait. Is the floor wet?{/i}"
            "Your knee sinks into the carpet just as deeply as your feet, and you belatedly notice the faint squishing sound. Your shoes are waterproof. Your pant leg is not."
            "The drawings here are of families. Some are on colorful craft paper, others copy paper or ripped pages of books."
            " One — a sketch of a child stick figure positioned in the center of a blank page — disintegrates in your hands, worn and waterstained acidic paper flaking into pieces."
            menu:
                "Leave it":
                    jump room2_interact
        "Leave it":
            jump room2_interact

screen placeholder_interactables:
    text "p" pos (0.0, 0.0)