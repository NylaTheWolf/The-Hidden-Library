image stairs_idle:
    xysize (478, 850)
    "images/interactables/stairs.png"

image stairs_hover:
    xysize (478, 850)
    "images/interactables/stairs_hover.png"

label room6: #grand catalogue
    # image bg room 6
    scene bg room 6
    show screen room6_interactables
    "A multi-story card catalog within a larger room than the atrium, the scaffolding of which has become part of the walls."
    "Looking up, you catch movement in your peripheral. The room appears to shift slightly, settling itself into sensible right angles and level surfaces.{w} It's not reassuring."
    "...{i}Was it trying to be?{/i}"
    call room6_interact

label room6_interact:
    call screen room6_interactables

screen room6_interactables:
    imagebutton auto "images/interactables/stairs_%s.png":
        focus_mask True
        pos (1140, 160)
        idle "stairs_idle"
        hover "stairs_hover"
        action Jump("climb_stairs")

label climb_stairs:
    show stairs_idle:
        pos (1140, 160)
    "There is a staircase leading up the side of the card catalog. It's clean and untouched, not matching the roughness of the carpet and lightly weathered wood cabinet. The march of time seemed to have passed it by."
    menu:
        "Ascend.":
            "There are 21 steps on the movable staircase that rests against the catalog. You walk upwards for a while, thinking through the rooms you’ve already passed through."
            "Is there a pattern to them? The layout of the Library is unlike others you’ve been to — {w}rooms branch off without clear connection in subject matter or time period..."
            "There are still 21 steps in front of you."
            "{i}What?{/i}"
            jump continue_climbing_stairs
        "Leave it.":
            jump room6_interact

label continue_climbing_stairs:
            menu:
                "Ascend.":
                    jump ascend
                "Look back.":
                    "You turn and look below.{w} You can barely see the floor. The walls stretch impossibly far below you."
                    "Behind you are stairs with uncountably many steps already traveled."
                    jump panicked_choices

label ascend:
    "You continue upwards. You see the stairs pass under your feet."
    "There are still 21 steps in front of you."
    jump continue_climbing_stairs

label panicked_choices:
    menu:
        "Ascend":
            jump ascend
        "Look back.":
            "You still see countless steps behind you. There are still 21 steps in front of you."
            jump continue_climbing_stairs
        "Panic.":
            "{i}Oh. {w} Oh no. {w} No no no.{/i}"
            "You’re suddenly lightheaded. Your chest hurts, it’s a struggle to breathe. Your muscles feel weak and shaky. You lean on the rail to try and steady yourself."
            "{i}Is that normal? Isn’t it usually just knees? Knees aren’t muscles. Right?{/i}"
            "You need to get it together."
            "{i}Okay. Alright. Fine. I don’t need to panic. I got up here somehow. I can get back down.{/i}"
            jump panicked_choices
        "Step down.":
            "You take several deep breaths. They don’t help, so you take one more sharp inhale and move your foot to the step below as quickly as you can."
            "Too quickly. Your foot misses the stair entirely—"
            "{i}Is there a stair below me at all?{/i}"
            "—and you lose your grip on the railing."
            "..."
            "..."
            "..."
            "..."
            "You hit the floor with far less force than you expected, but it still knocks the wind out of you."
            "Above you rests the movable staircase with exactly 21 steps, no taller than before."
            jump room6_interact