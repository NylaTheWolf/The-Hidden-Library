# Script for reading letters, books, etc.
define n = nvl_narrator

label letter_read(item):
    if (item.is_readable):
        hide screen inventory_alt
        hide screen show_item_info
        hide screen game_overlay
        hide screen minimap
        window hide
        if item.name == "Notebook":
            # TODO: space out the top of the screen from the first line
            # special popup for notebook
            n "The first few pages are filled with the information you've collected about the library, with authors and page numbers cited and a side column of personal notes and asides."
            n "An acquaintance once told you that your notes read like an academic paper."
            n "You’re not sure it was a compliment."
        else:
            # general popup for other readable items. Not sure how to get it to read an array of strings
            n "[item.item_text]"
        
        nvl clear
        show screen inventory_alt # return to inventory
        show screen game_overlay