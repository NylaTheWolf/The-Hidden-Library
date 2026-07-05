image papers_idle:
    "images/interactables/papers.png"
    
image papers_hover:
    "images/interactables/papers_hover.png"

label room2: #the room with water damaged children's books
    # image bg room 2
    scene bg room 2
    $ interactables = room_interact_screens[playerObj.lastRoom]
    $ renpy.hide_screen(interactables)
    "The carpeted floor is thick and soft below your feet. You sink into it gently, taking an inch or so off your already short stature."
    "There is something slightly dizzying about the layout. Are the corners not quite square? Is the floor slanted, just slightly, as it continues towards the shelves?"
    "Roughly bound books and binders line the upper shelves, the lower shelves are stacked with loose paper."
    "The silence stretches, the smell of old paper and mold reaches you.{w}\n\nYou are alone."
    call room2_interact from _call_room2_interact

label room2_interact:
    hide screen minimap
    $ minimap_open = False
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