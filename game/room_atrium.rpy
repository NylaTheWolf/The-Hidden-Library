label atrium:
    image bg atrium = Transform("atrium 1", zoom=.75)
    scene bg atrium
    "holy shit what a crazy library"

    menu: #note for menus, we could implement context sensitive direciton based on where the player entered from, but only if we have time
        "Where should I go?"
        "The West door":
            call room2
        "The East door":
            call room6