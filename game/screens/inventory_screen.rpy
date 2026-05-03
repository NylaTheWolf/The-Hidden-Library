###
# Inventory screen code/style originally by Patchmonk (https://github.com/Patchmonk/Simple-Renpy-Inventory).
# Modified by Tori to fit project code and preferences.
###
define n = nvl_narrator

screen inventory_alt():
    modal True
    zorder 101
    frame style style["Inventory_frame"]: # This frame contains the inventory buttons and the scrollbar.
        imagebutton style style["Inv_close_btn"]: # This button closes the inventory screen.
            idle "Close"
            hover "Close_hover"
            action Hide("inventory_alt")
            # action [Hide("inventory_alt"), Hide("item_iteraction")]
        

        vbox style style["Inv_vbox"]:  # This vbox contains the title and the grid of inventory slots.
            frame style style["Inv_title_frame"]:
                text "Inventory" style style["Inv_title"] color "BABABA"

            viewport id "vp":
                # The original dynamics vscrollbar bar argument is removed here, In this version we are using the Renpy function, If you want to use the previous version you can always check the previous git version.
                ysize 475
                xsize 1160
                draggable True
                mousewheel True
                scrollbars "vertical"  
                vscrollbar_xsize 10
                vscrollbar_ysize 475  
                vscrollbar_ypos 0
                vscrollbar_xpos -21
                vscrollbar_base_bar "components/inventory/images/gui/inv_vscrollbar_base_bar.png" 
                vscrollbar_thumb "components/inventory/images/gui/inv_vscrollbar_thumb.png"
                vscrollbar_unscrollable "hide"

                vpgrid cols 7 style style["Inv_grid"]: # This vpgrid displays the inventory slots.
                    for slot in range(inventory_slot_count):  # This loop iterates over all the inventory slots. 
                        
                        ## Code modified by Nyla/Tori
                        frame: # This frame contains the inventory slot item.
                            maximum(155, 155)
                            if slot < len(inventory): # If the slot is not empty, the slot background image will display.
                                button:
                                    hovered Show("show_item_info", item=inventory[slot])
                                    unhovered Hide("show_item_info")
                                    # action Show("show_item_info", item=inventory[slot])
                                    # action CaptureFocus("show_tooltip")
                                    # action Show("item_iteraction", item=inventory[slot])
                                    # action [Show("letter"), Hide("inventory_alt"), Hide("show_item_info")]
                                    # if inventory[slot].readable:
                                    action Call("letter_read", item=inventory[slot], from_current=True)
                                    
                                background Image("components/inventory/images/gui/slot_bg.png") xalign 0.5 yalign 0.5
                                $ image_name = inventory[slot].image
                                if (renpy.loadable(image_name, "components/inventory/images/icons/")): # Check if the item image exists in the icons folder.
                                    add Image("components/inventory/images/icons/" + image_name, xalign=0.5, yalign=0.5) size (120, 120)
                                else:
                                    # If image not added, use placeholder image
                                    add Image("components/inventory/images/icons/placeholder.png", xalign=0.5, yalign=0.5) size (120, 120)
                                $ Inv_item_name = inventory[slot].name.replace('_', ' ')
                                text Inv_item_name style style["Inv_item_name"]
                            else:
                                # If the slot is empty, the background is displayed.
                                background Image("components/inventory/images/gui/slot_bg.png") xalign 0.5 yalign 0.5

## Testing different popups

screen show_item_info(item):
    zorder 102
    # frame:
    #     xsize 300 ysize 100
    #     xpos 0.5 ypos 0.5
        # text item.name
        # text item.name
        # text item.name
    fixed:
        area(1500, 200, 300, 580)
        # xalign 0.2 yalign 0.5
        add "#000000b3"
        if item.description is not None:
            text item.description color "#FFFFFF"
        else:
            text "No description available." color "#FFFFFF"

screen item_iteraction(item):
    zorder 103
    frame:
        xsize 300
        xpos 0.3 ypos 0.5
        text "This is an item."
        # text item.name

label letter_read(item):
    if (item.is_readable):
        hide screen inventory_alt
        hide screen show_item_info
        window hide
        
        # show screen letter
        n "[item.item_text]"
        nvl clear
        show screen inventory_alt # return to inventory
        # pause

screen letter:
    modal True
    zorder 104
    frame style style["Inventory_frame"]:
        xpos 0.5 ypos 0.5
        xanchor 0.5 yanchor 0.5
        text "This is a letter." color "#FFFFFF"
        imagebutton style style["Inv_close_btn"]: # This button closes the inventory screen.
            idle "Close"
            hover "Close_hover"
            action Hide("letter")