class playerData:
    def __init__(self):
        self.rooms = { #room names are temporary and subject to change
            "atrium": roomData("The Atrium", "room_atrium"),
            "room2": roomData("Flooded Picture Books", "room2"),
            "room3": roomData("The Card Catalogue", "room3"),
            "room4": roomData("Ancient Reading Room", "room4"),
            "room5": roomData("Natural Sciences", "room5"),
            "room6": roomData("The Grand Catalogue", "room6")
        }

class roomData:
    def __init__(self, displayName, label):
        self.displayName = displayName #a title for the room to reference in in game menus/dialogue
        self.label = label #the path to the actual scene (label) for the room
        self.visited = False #whether or not the player has been here before. Can be used in dialogue/for the map
        self.enterDirection = "North" #which direction the player entered from. Used for adding connections to the map