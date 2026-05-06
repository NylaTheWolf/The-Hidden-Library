# Reference: https://www.reddit.com/r/RenPy/comments/1l4qyhs/setting_up_a_point_and_click_system_in_renpy/

default investigation_mode = False
define i = Character(None, screen="investigation_text")

label investigate:
    python:
        currentRoom = playerObj.currentRoom
        if currentRoom in room_interact_screens:
            interactables = room_interact_screens[playerObj.currentRoom]
            renpy.call_screen(interactables)
    # $ interactables = room_interact_screens[playerObj.currentRoom]
    # $ renpy.call_screen(interactables)
    window hide
    $ investigation_mode = True
    # i "..." (advance=False)
    # pause
    # if not investigation_mode:
    #     return
    # else:
    #     jump investigate