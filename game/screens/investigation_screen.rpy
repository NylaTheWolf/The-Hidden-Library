image investigation_textbox:
    "gui/textbox2.png"

screen investigation_text(who, what):
    window:
        # (580, 980, 771, 82)
        xpos 0.5
        ypos 980
        anchor (0.5, 1.0)
        ysize 20   
        background "investigation_textbox"
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what:
            id "what"
            color "#f3f3f3" 
            xalign 0.5