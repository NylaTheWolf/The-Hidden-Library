label room2: #the room with water damaged children's books
    image bg room2 = Transform("room2temp", zoom=.75)
    scene bg room2
    "Room 702a - 18th to 22nd century children's writings - water damaged"
    menu:
        "Where should I go?"
        "The East door":
            call atrium
        "The South door":
            call room3
        "The West door":
            call room3