# Script for reading letters, books, etc.
define n = nvl_narrator

label letter_read(item):
    if (item.is_readable):
        hide screen inventory_alt
        # inventory will be open by the time you return so don't change the variable
        hide screen show_item_info
        hide screen game_overlay onlayer hud_layer
        hide screen minimap
        $ minimap_open = False
        window hide
        if item.name == "Notebook":
            # TODO: space out the top of the screen from the first line
            # special popup for notebook
            n "The first few pages are filled with the information you've collected about the library, with authors and page numbers cited and a side column of personal notes and asides."
            n "An acquaintance once told you that your notes read like an academic paper."
            n "You’re not sure it was a compliment."
        elif item.name == "Torn Page":
            n "The requirements are trivial, the steps I followed simple. If it decides it wants you, it will take you. This is simply {i}a{/i} way to get its attention."
            n "I entered the library from my home, but I regret that choice now. I theorized that if I condemned a large amount of books to the library at once it might allow me to enter along with them,{w} so I chose one of my bookshelves, away from the others, struck a match, and lit it on fire."
            n "I waited for it to catch, and then placed my hands on the burning shelf and pushed backwards, against the wall."
        else:
            # general popup for other readable items. Not sure how to get it to read an array of strings
            if item.item_text is not None:
                n "[item.item_text]"
        
        nvl clear
        show screen inventory_alt # return to inventory
        show screen game_overlay onlayer hud_layer