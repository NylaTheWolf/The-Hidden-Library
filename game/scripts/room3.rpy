label room3:
    scene bg room 3
    show screen placeholder_interactables
    "Card Catalog 1286sm"
    "The plaque outside this room is no help. The number and letters mean nothing to you."
    "The room itself is laid out in a way that strikes you as utilitarian if the people who would work here were allergic to the concepts of parallel and perpendicular."
    "The card catalog cabinets sit heavy, spread across the room in a zig-zagging fashion with tables positioned in gaps between them."
    # pause(2.0)
    "You are alone."
    # TODO: Keep this dialogue up to keep its impact?
    call screen placeholder_interactables

label room3_2: #the version of room 3 entered from the west of room2
    call room3 from _call_room3
    # call screen placeholder_interactables