default other_choices = 0
default force_match = False

label room5:
    $ force_match = False
    scene bg room 5
    show screen placeholder_interactables
    "You enter slowly. Shelves line the oddly angled walls. The room contains no tables or chairs."
    "Instead, a large mound of books and splintered pieces of shelves is heaped against two of the doors."
    "Ahead, the single barricaded door awaits. Dust hangs heavily in the air."
    "{i}Am I alone?{/i}"
    # TODO: Play sound
    "The door swings shut behind you. The dark is all-encompassing."
    jump room5_choices

label room5_choices:
    if not force_match:
        menu:
            "Try the door behind you.":
                # TODO sound
                "You fumble for the door handle. It rattles loosely.{w}\nYou push hard. The door doesn’t move."
                "You throw all your weight into pulling the handle.{w}Something inside it snaps, the sound amplified by the small space."
                "You keep your balance, clutching the heavy door handle now loose in your left hand."
                $ other_choices += 1
                if other_choices >= 2:
                    $ force_match = True
                jump room5_choices
            "Try the door across the room.":
                "Your quick, determined steps into the center of the room fall away almost immediately as you realize you don’t know if you’re pointed towards the other door anymore."
                "You reach forward blindly in the dark, and connect with nothing."
                $ other_choices += 1
                if other_choices >= 2:
                    $ force_match = True
                jump room5_choices
            "Light a match.":
                jump light_match
    else:
        menu:
            "Light a match.":
                jump light_match
            "Light a match.":
                jump light_match
            "Light a match.":
                jump light_match


label light_match:


    # call screen placeholder_interactables
    