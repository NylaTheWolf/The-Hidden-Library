label room6: #grand catalogue
    image bg room6 = Transform("room6temp", zoom=.75)
    scene bg room6
    "A multi-story card catalog within a larger room than the atrium, the scaffolding of which has become part of the walls."
    menu:
        "Where should I go?"
        "The door on the left":
            call room2(player)
        "The door on the right":
            call room6(player)