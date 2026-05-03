image map atriumMap = "images/minimap_images/tempAtriumMap.png"
image map room2Map = "images/minimap_images/tempRoom2Map.png"
image map room6Map = "images/minimap_images/tempRoom6Map.png"

init python:
    class mapManager:
        def __init__(self):
            self.rooms = {
                #will add the others later once I add pngs
                "atrium": minimapRoomData("images/minimap_images/tempAtriumMap.png"),
                "room2": minimapRoomData("images/minimap_images/tempRoom2Map.png"),
                "room6": minimapRoomData("images/minimap_images/tempRoom6Map.png")
            }
            #use for draw order to simulate character updating map in real time
            self.connectionList = []
            #hardcoded for current atrium map png, change later
            self.mapScale = 1
            self.top = 0
            self.bottom = 200
            self.left = 0
            self.right = 200

        def update_rooms(self, player):
            if player.lastExit != None:
                #check if the last room/exit combo the player used was already traversed
                #praying that python reference/value types work the same as c based languages
                current = self.rooms[player.lastRoom].connections[player.lastExit]
                if current == None:
                    #if not, establish a new link
                    current = minimapRoomConnection(
                        player.lastExit, 
                        player.lastEntry, 
                        player.exitX,
                        player.exitY,
                        self.rooms[player.lastRoom],
                        self.rooms[player.currentRoom]
                    )
                    self.connectionList.append(current)

        #horrendously inneficient code but its fine for a small project
        def format_map(self):
            for r in self.rooms.values():
                #N/S/E/W are indexes 0-3
                for i in range(4):
                    connection = r.connections[i]
                    if connection != None:
                        cWidth, cHeight = renpy.image_size(connection.this.image)
                        self.left = min(self.left, connection.offsetX)
                        self.right = max(self.right, connection.offsetX + cWidth)
                        self.top = min(self.top, connection.offsetY)
                        self.bottom = max(self.bottom, connection.offsetY + cHeight)
            #relative size for frame (idk if I want to use this yet)
            self.mapScale = min(200/self.right, 200/self.bottom)
            return self.right - self.left, self.bottom - self.top

        def draw_map(self):
            drawRooms = []
            atriumTransform = Transform(xalign = 0.5, yalign = 0.5)
            drawRooms.append((atriumTransform, self.rooms["atrium"].image))
            for r in self.connectionList:
                cWidth, cHeight = renpy.image_size(r.this.image)
                cTop = r.offsetX
                cLeft = r.offsetY
                drawn = False
                
                #normalize to 0,0 as top left coordinates
                cLeft -= self.left
                cTop -= self.top
                #convert to renpy screen positions (aka 100% = screen width - image width)
                tx = 0
                if (self.right - self.left) - cWidth != 0:
                    tx = cLeft/((self.right - self.left) - cWidth)
                ty = 0
                if (self.bottom - self.top) - cHeight != 0:
                    ty = cTop/((self.bottom - self.top) - cHeight)
                transform = Transform(xalign = tx, yalign = ty)
                for dr in drawRooms:
                    #avoid duplicate draws while still being able to draw the same room in multiple places
                    #potentially it would be better to just have rooms with impossible entrances be represented by multiple objects, but idk
                    if tx == dr[0].xalign and ty == dr[0].yalign:
                        drawn = True
                if drawn == False:
                    drawRooms.append((transform, r.this.image))
            return drawRooms



    class minimapRoomData:
        #connections is a list of minimapRoomConnections (N=0,E=1,S=2,W=3)
        def __init__(self, image, connections = [None, None, None, None]):
            self.connections = connections
            self.image = image
        def draw_connection(self, connection):
            self.connections[connection.exitDirection] = connection
    
    class minimapRoomConnection:
        #offsets are relative cooradinates to atrium (top left). 
        #offsets are stored in connections rather than rooms because depending on which exit a player uses,
            #the room might initially appear in a different place if trying to follow euclidian space
            #(for example, room2 has an exit to room 3 to the south and east, so depending on which the player first takes it needs to show up appropriately on the map)
            #Theres for sure a better way to do this but my python is rusty
        #this and other are references to minimapRoomData objects
        def __init__(self, exitDirection, entryDirection, offsetX, offsetY, this, other):
            self.exitDirection = exitDirection
            self.entryDirection = entryDirection
            self.offsetX = offsetX
            self.offsetY = offsetY
            self.this = this
            self.other = other

            
    mapManager = mapManager()


screen minimap(player):
    $mapManager.update_rooms(player)
    $frameX, frameY = mapManager.format_map()
    $print("w:"+frameX+", h:"+frameY)
    frame align (1.0, 1.0) xsize frameX ysize frameY:
        
        $currentRoom = 0
        for r in mapManager.draw_map():
            $trans, imagePath = r
            $print("x:"+trans.xalign+", y:"+trans.yalign)
            add imagePath:
                at trans

        
