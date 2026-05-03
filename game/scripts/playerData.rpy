init python:
    class playerData:
        def __init__(self):
            self.rooms = { #room names are temporary and subject to change
                "atrium": roomData("The Atrium", "room_atrium", "atrium 1.jpg", "images/minimap_image/tempAtriumMap.png"),
                "room2": roomData("Flooded Picture Books", "room2", "room2temp.png", "images/minimap_image/tempRoom2Map.png"),
                "room3": roomData("The Card Catalogue", "room3", "atrium 1.jpg", "images/minimap_image/tempAtriumMap.png"),
                "room4": roomData("Ancient Reading Room", "room4", "atrium 1.jpg", "images/minimap_image/tempAtriumMap.png"),
                "room5": roomData("Natural Sciences", "room5", "atrium 1.jpg", "images/minimap_image/tempAtriumMap.png"),
                "room6": roomData("The Grand Catalogue", "room6", "room6temp.png", "images/minimap_image/tempRoom6Map.png")
            }
            #should both be set whenever a player leaves a room
            self.lastRoom = "atrium"
            self.currentRoom = "atrium"
            self.lastExit = None 
            self.lastEntry = None
            self.exitX = 0
            self.exitY = 0

        def move_room(self, lastR, lastE, currentR, currentE, x, y):
            self.lastRoom = lastR
            self.lastExit = lastE
            self.currentRoom = currentR
            self.lastEntry = currentE
            self.exitX = x
            self.exitY = y
            self.rooms[self.currentRoom].enterDirection = currentE
            self.rooms[self.lastRoom].visited = True

    class roomData:
        def __init__(self, displayName, label, imagePath, mapImagePath):
            self.displayName = displayName #a title for the room to reference in in game menus/dialogue
            self.label = label #the path to the actual scene (label) for the room
            self.imagePath = imagePath
            self.mapImagePath = mapImagePath
            self.visited = False #whether or not the player has been here before. Can be used in dialogue/for the map
            self.enterDirection = 0 #which direction the player entered from. Used for adding connections to the map
            