# default lastRoom = "atrium"
# default currentRoom = "atrium"
# default lastExit = None
# default lastEntry = None
# default exitX = 0
# default exitY = 0
# default relativeX = 0
# default relativeY = 0
# default relativeRotation = 0

# default

init python:
    import copy
    class playerData:
        def __init__(self):
            self.rooms = { #room names are temporary and subject to change
                "atrium": copy.deepcopy(roomData("The Atrium", "room_atrium", "bg atrium.jpg", "images/minimap_image/tempAtriumMap.png")),
                "room2": copy.deepcopy(roomData("Flooded Picture Books", "room2", "bg room 2.png", "images/minimap_images/tempRoom2Map.png")),
                "room3": copy.deepcopy(roomData("The Card Catalogue", "room3", "bg room 3.png", "images/minimap_images/tempRoom3Map.png")),
                "room3_2": copy.deepcopy(roomData("The Card Catalogue", "room3", "bg room 3.png", "images/minimap_images/tempAtriumMap.png")),
                "room4": copy.deepcopy(roomData("Ancient Reading Room", "room4", "bg room 4.png", "images/minimap_images/tempAtriumMap.png")),
                "room5": copy.deepcopy(roomData("Natural Sciences", "room5", "bg room 5.png", "images/minimap_images/tempAtriumMap.png")),
                "room6": copy.deepcopy(roomData("The Grand Catalogue", "room6", "bg room 6.png", "images/minimap_images/tempRoom6Map.png"))
            }
            #should both be set whenever a player leaves a room
            self.lastRoom = "atrium"
            self.currentRoom = "atrium"
            self.lastExit = None 
            self.lastEntry = None
            self.exitX = 0
            self.exitY = 0
            self.relativeX = 0
            self.relativeY = 0
            self.relativeRotation = 0

        def move_room(self, lastRoom, lastExit, currentRoom, lastEntry, x, y, rotation):
            investigation_mode = False
            self.lastRoom = lastRoom
            self.lastExit = lastExit
            self.currentRoom = currentRoom
            self.lastEntry = lastEntry
            self.relativeRotation += rotation
            self.relativeRotation = self.relativeRotation%4
            print(f"{rotation}, {self.relativeRotation}")
            if (self.relativeRotation == 0 or self.relativeRotation == 2):
                print("rotated")
                self.relativeX += (x * ((self.relativeRotation*-1)+1))
                self.relativeY += (y * ((self.relativeRotation*-1)+1))
            else:
                self.relativeX += x
                self.relativeY += y
            

            self.exitX = self.relativeX
            self.exitY = self.relativeY
            
            self.rooms[self.currentRoom].enterDirection = lastEntry
            self.rooms[self.lastRoom].visited = True
            # Hide interactables of previous room when moving rooms
            if lastRoom in room_interact_screens:
                renpy.hide_screen(room_interact_screens[lastRoom])
            mapManager.update_rooms()

    class roomData:
        def __init__(self, displayName, label, imagePath, mapImagePath):
            self.displayName = displayName #a title for the room to reference in in game menus/dialogue
            self.label = label #the path to the actual scene (label) for the room
            self.imagePath = imagePath
            self.mapImagePath = mapImagePath
            self.visited = False #whether or not the player has been here before. Can be used in dialogue/for the map
            self.enterDirection = 0 #which direction the player entered from. Used for adding connections to the map
            # self.interactables = interactables