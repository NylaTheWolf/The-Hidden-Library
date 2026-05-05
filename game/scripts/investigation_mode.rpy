# Reference: https://www.reddit.com/r/RenPy/comments/1l4qyhs/setting_up_a_point_and_click_system_in_renpy/

default investigation_mode = False

label investigate:
    $ investigation_mode = True
    "You investigate the area." (advance=False)
    pause