define atriumBaseText = "Cold grey light from the windows and skylight reaches across the expanse of the atrium to the entry, touching rows of bookshelves and casting shifting shadows on the floor. "
default atriumText = ""
image bell_idle:
    # anchor (0.5, 0.5)
    xysize (200, 162)
    "images/interactables/bell.png"
image bell_hover:
    # anchor (0.5, 0.5)
    xysize (200, 162)
    "images/interactables/bell_hover.png"

image zine_idle:
    xysize (400, 165)
    "images/interactables/zine.png"

image zine_hover:
    xysize (400, 165)
    "images/interactables/zine_hover.png"

image books_idle:
    "images/interactables/books.png"

image books_hover:
    "images/interactables/books_hover.png"

label atrium:
    scene bg atrium
    show screen game_overlay onlayer hud_layer
    show screen atrium_interactables
    # if (minimap_open):
    #     hide screen minimap
    #     $ minimap_open = False
    # $ interactables = room_interact_screens["atrium"]
    # $ renpy.show_screen(interactables)
    python:
        atriumText = atriumBaseText
        if(playerObj.rooms["atrium"].visited):
            atriumText = "A chill permeates throughout the atrium." # debug sentence.
        playerObj.rooms["atrium"].visited = True #sets the room's data as being visited
    "[atriumText]"

    call atrium_interact from _call_atrium_interact

label atrium_interact:
    call screen atrium_interactables

screen atrium_interactables():
    modal False
    # zorder 50
    imagebutton auto "images/interactables/bell_%s.png":
        focus_mask True
        # anchor (0.5, 0.5)
        pos (660, 730)
        idle "bell_idle"
        hover "bell_hover"
        selected "bell_idle"
        action [Jump("ring_bell")]
    imagebutton auto "images/interactables/zine_%s.png":
        focus_mask True
        pos (1000, 650)
        idle "zine_idle"
        hover "zine_hover"
        action Jump("cryptid_zine")
    imagebutton auto "images/interactables/books_%s.png":
        focus_mask True
        pos (675, 550)
        idle "books_idle"
        hover "books_hover"
        # TODO: Make insensitive when dialogue is still up
        action Jump("read_books")

label ring_bell:
    # TODO: Steam achievement
    # TODO: Sound effect
    show bell_idle:
        pos (660, 730)
    show books_idle:
        pos (675, 550)
    show zine_idle:
        pos (1000, 650)
    "You ring the bell."
    jump atrium_interact

label cryptid_zine:
        show books_idle:
            pos (675, 550)
        show zine_idle:
            pos (1000, 650)
        show bell_idle:
            pos (660, 730)
        "You pick up the booklet laying on the desk. On the cover is a colored sketch of Mothman."
        "At the top of the page is a title: \"Cryptozine: Cryptids and Urban Legends!\""
        menu:
            "Skim through the book.":
                "You flip through some of the pages. The zine consists of accounts of different urban legends in the submitter’s town."
                "Some share their own personal experiences with these legends and cryptids, surely hard proof that these legends are, in fact, real."
                "Each article is accompanied by corresponding sketches. While skimming through the booklet, a particular article catches your attention:"
                hide screen game_overlay onlayer hud_layer
                window hide
                n "{b}{i}The Library of the Lost: Books Lost to Time{/i}{/b}\nBy Lena Ore\n"
                n "Stories have been part of human history since we were able to communicate with each other, but the fact of the matter is that, unfortunately, too many of them are lost to time. Think of the Library of Alexandria—so much history lost to fire and warfare."
                n "To this day, the loss of stories, and thus, the loss of culture, is a persistent issue. Major corporations are fighting against libraries and other archival efforts to preserve out-of-print media under the guise of \"copyright protection.\" Too often, the public are the losers in these fights."
                n "But what if stories weren’t lost forever? What if, like energy, they are never truly lost, only transformed and transferred. What if, in a place hidden from our eyes, they persist?"
                nvl clear
                n "In my hometown, there are whispers of such a place: a place where any written work that is lost is transported to a hidden library."
                n "This library holds millions of works that have been lost to the winds of time. Growing up, I’ve even heard some people claim that it holds stories from the {i}future{/i}."
                n "Most people in my hometown talk about the library as if it was just folklore, a campfire story, our own “Bloody Mary” (sorry to the Bloody Mary person back in Vol. 2!)."
                n "All my life, we’d make jokes like, \"Oh, my left sock must’ve been sucked up by the library!\""
                n "But there are some people—academics, even—that swear up and down that the library is real. If you go digging, you can find accounts of people claiming that they’ve been to the library or found evidence of its existence."


                nvl clear
                show screen game_overlay onlayer hud_layer
                jump atrium_interact
            "Leave it.":
                jump atrium_interact
            
label read_books:
    show books_idle:
        pos (675, 550)
    show zine_idle:
        pos (1000, 650)
    show bell_idle:
        pos (660, 730)
    "Resting on the reference desk's shelf are a few non-descript, thick hard-cover books. But one in particular stands out to you."
    "It's a thick, cloth-bound book. The edges of the spine seem to be fraying a bit from being read many, many times over and over, perhaps even by different owners."
    "{i}A family heirloom, perhaps?{/i}"
    menu:
        "Take and open the book.":
            hide books_idle
            "You open the old book from the middle, careful as to not further mess up the pages."
            "The first thing you notice is the scribbly, child-like drawings on the pages. A figure is standing in the white void. In front of them are a pile of scattered papers engulfed in flames, burning in front of their eyes..."
            "You force your eyes away from the sketch, choosing instead to look at the dense, two-columned texts above the drawing. It’s written in a script you don’t recognize at all."
            "Your eyes skim over to the top corner of the pages. They’re numbered, as expected. But the left page is labeled page 41,793, while the right page is number 999."
            menu:
                "Turn the page.":
                    "The next pages are numbered 809,721 and 30,478. There is another childish drawing, but this time of a stick figure shoved in a birdcage."
                    "Even as a stick figure, you can see the visibly uncomfortable contortion of its limbs drawn up as close to the person’s body as possible."
                    "Maybe there’s a foreword for this book?"
                    "You think you hear a distant part of your brain telling you to just put it down."
                    menu:
                        "Find the first page.":
                            jump keep_reading_book
                        "Leave it alone.":
                            "Yes, probably for the best. Nothing to be concerned about."
                            jump atrium_interact
                "Put it down.":
                    "Yes, probably for the best. Nothing to be concerned about."
                    jump atrium_interact
            jump atrium_interact
        "Leave it.":
            jump atrium_interact

label keep_reading_book:
    "Carefully, so as to not further wear down the delicate parchment, you grab a stack of pages near the front cover and turn them over."
    "You repeat this a few times. Your body goes on autopilot as your brain drifts into thinking about your purpose here."
    "You can’t just move on. You need to find them, the things would give all of this meaning, the things that will help you underst—"
    "Wait.\n\nHow long have you been flipping through this book?"
    "As you snap back to reality, you realize that the stack of pages resting on the cover...has not gotten any smaller."
    menu:
        "Find the first page.":
            "You slam the book shut and slip your thumb between the flyleaf and the cover."
            "Or, at least you try to. You immediately feel the texture of ancient parchment under your thumb instead of the cloth cover." 
            "You try to keep your thumb on the flyleaf itself, but it clearly isn’t. There, again, is the obscure, densely typed script with a nonsensical page number: 987,183."
            menu:
                "Find the first page.":
                    "You try to find the beginning of this book, but to no avail. Every time you think you catch the very first page, a new stack of pages seemingly forms right under your hand, like they're spilling out of the book."
                    "Come to think of it, you’re still in the middle of this book."
                    "You can’t rely on the wildly arbitrary page numbers to backtrack (currently, you’re on pages 34,899 and 15,992,384), but maybe you could at least find the first page you saw."
                    menu:
                        "Find it.":
                            "You scour through pages and pages of unfamiliar, strange drawings and script."
                            "None of the drawings repeat. None of the pages are any closer to the beginning or end of this book."
                            "Does anything exist outside of this book? The idea of pulling yourself away from it is inconceivable."
                            "You feel the otherworldliness of this thing creeping from your fingertips into your body, into your very soul. Oh God, it’s consuming you, {i}eating{/i} at you—"
                            "You blink, and the book is suddenly across the room. You hadn’t even registered the fact that you had launched it from your grasp."
                            "It’s as if your survival instincts kicked in to keep you as far away from it as possible, like it would burn you."
                            show books_idle:
                                pos (675, 550)
                            "You blink again, and the book is back on the desk. Don’t pick it up again."
                            menu:
                                "Leave it.":
                                    jump atrium_interact
                                "Leave it.":
                                    jump atrium_interact
                                "Leave it.":
                                    jump atrium_interact
    jump atrium_interact