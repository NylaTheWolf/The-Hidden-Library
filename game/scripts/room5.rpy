default other_choices = 0
default force_match = False

label room5:
    $ force_match = False
    scene bg room 5
    # show screen placeholder_interactables
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
    # TODO: Sound
    "You pull your matchbox from your pocket and strike a match. It flares to life between your shaking fingers, casting flickering light onto the shelves and across the walls."
    "{i}Why does everything look so different in the dark?{/i}"
    "You sweep your hand in an arc, trying to understand the layout the room relative to where you're standi—"
    "{i}Fuck!{/i}"
    "You drop the match. It slips from your fingers without resistance and without ceremony.{w}\n\nThe dry papers on the floor catch immediately."
    "{i}Wait! No wait I didn't meant to—{/i}"
    "The heat is unbearable. The flames lick up the walls and the sound of crackling paper fills the room as texts on the higher shelves catch fire."
    "e. The exposed skin of your face and hands cracks and blisters."
    "Smoke fills the small space quickly.{w}\n\nYour lungs are a small space, and the smoke fills them too."
    "You stumble backwards and find a door behind you. You wrench it open, stumble through, and slam it shut."
    "You gasp a few breaths of non-smoke before you realize you feel fine.{w}Your hands and face are smooth, pain-free skin, and your chest isn't burning."
    "{i}That was real, right?! It{/i} hurt{i}, it had to be real.{/i}"
    "{i}Say something! It was real!{/i}"
    "{i}I know it was.{/i}"
    call screen placeholder_interactables
    