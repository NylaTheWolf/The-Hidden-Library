image map atriumMap = "images/minimap_images/tempAtriumMap.png"
image map room2Map = "images/minimap_images/tempRoom2Map.png"
image map room6Map = "images/minimap_images/tempRoom6Map.png"

init 1 python:
    import copy
    import json
    class minimapManager:
        def __init__(self):
            self.rooms = {
                #will add the others later once I add pngs
                "atrium": copy.deepcopy(minimapRoomData("images/minimap_images/tempAtriumMap.png")),
                "room2": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom2Map.png")),
                "room6": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom6Map.png")),
                "room3": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom3Map.png")),
                "room3_2": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom3Map.png")),
                "room4": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom3Map.png")),
                "room5": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom3Map.png"))
            }
            cData = json.load(renpy.file("data/roomConnections.json"))
            for roomKey in cData:
                for direction in cData[roomKey]:
                    cn = cData[roomKey][direction]
                    cnParams = cn["connectionParams"]
                    ctParams = cn["triggerParams"]
                    #lastRoom, lastExit, currentRoom, lastEntry, x, y
                    connection = copy.deepcopy(minimapClickTrigger(
                        Transform(xalign = float(ctParams[0]), yalign = float(ctParams[1])),
                        float(ctParams[2]),
                        float(ctParams[3]),
                        (
                            roomKey,
                            int(direction),
                            cnParams[0],
                            int(cnParams[1]),
                            int(cnParams[2]),
                            int(cnParams[3])
                            )
                        ))
                    self.rooms[roomKey].clickTransitions.append(connection)
                    


            #use for draw order to simulate character updating map in real time
            self.connectionList = []
            #hardcoded for current atrium map png, change later
            self.mapScale = 1
            self.top = 0
            self.bottom = 200
            self.left = 0
            self.right = 200
            self.currentFrame = (0,0)

        def update_rooms(self):
            if playerObj.lastExit != None:
                #check if the last room/exit combo the player used was already traversed
                current = self.rooms[playerObj.lastRoom].connections[playerObj.lastExit]
                if current == None:
                    #if not, establish a new link
                    current = minimapRoomConnection(
                        playerObj.lastExit, 
                        playerObj.lastEntry, 
                        playerObj.exitX,
                        playerObj.exitY,
                        self.rooms[playerObj.lastRoom],
                        self.rooms[playerObj.currentRoom]
                    )
                    self.rooms[playerObj.lastRoom].connections[playerObj.lastExit] = current
                    self.connectionList.append(current)

        #use this to get the bounds of the map
        def format_map(self):
            for r in self.rooms.values():
                #N/S/E/W are indexes 0-3
                for i in range(4):
                    connection = r.connections[i]
                    if connection != None:
                        cWidth, cHeight = renpy.image_size(connection.other.image)
                        self.left = min(self.left, connection.offsetX)
                        self.right = max(self.right, connection.offsetX + cWidth)
                        self.top = min(self.top, connection.offsetY)
                        self.bottom = max(self.bottom, connection.offsetY + cHeight)
            #relative size for frame (idk if I want to use this yet, depends on minimap vs map distinction)
            self.mapScale = min(200/self.right, 200/self.bottom)
            return self.right - self.left, self.bottom - self.top

        #horrendously inneficient code but its fine for a small project
        def draw_map(self):
            drawRooms = []
            frameWidth = self.right - self.left
            frameHeight = self.bottom - self.top
            #hardcoded atrium draw, change if check values once image updated
            atrX = 0.5
            atrY = 0.5
            if frameWidth != 200:
                atrX = -self.left/(frameWidth - 200)
            if frameHeight != 200:
                atrY = -self.top/(frameHeight - 200)
            atriumTransform = Transform(xalign = atrX, yalign = atrY)
            drawRooms.append((atriumTransform, self.rooms["atrium"].image))
            #loop for rest
            for r in self.connectionList:
                cWidth, cHeight = renpy.image_size(r.other.image)
                cTop = r.offsetY
                cLeft = r.offsetX
                drawn = False
                
                #normalize to 0,0 as top left coordinates
                cLeft -= self.left
                cTop -= self.top
                #convert to renpy screen positions (aka 100% = screen width - image width)
                tx = 0.5
                if frameWidth - cWidth != 0:
                    tx = cLeft/(frameWidth - cWidth)
                ty = 0.5
                if frameHeight - cHeight != 0:
                    ty = cTop/(frameHeight - cHeight)
                transform = Transform(xalign = tx, yalign = ty)
                for dr in drawRooms:
                    #avoid duplicate draws while still being able to draw the same room in multiple places
                    #potentially it would be better to just have rooms with impossible entrances be represented by multiple objects, but idk
                    if tx == dr[0].xalign and ty == dr[0].yalign:
                        drawn = True
                    if self.rooms[playerObj.currentRoom] == r.other:
                        self.currentFrame = (tx, ty)
                        
                if drawn == False:
                    drawRooms.append((transform, r.other.image))
                    
                    
            return drawRooms
            
        def make_triggers(self):
            return self.rooms[playerObj.currentRoom].clickTransitions

    class minimapRoomData:
        #connections is a list of minimapRoomConnections (N=0,E=1,S=2,W=3)
        def __init__(self, image, connections = [None, None, None, None]):
            self.connections = connections
            self.image = image
            #where we store the click events used for player navigation, added by room labels
            self.clickTransitions = []
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
        
    class minimapClickTrigger:
        def __init__(self, transform, width, height, connectionParams, special = None):
            self.transform = transform
            self.width = width
            self.height = height
            self.connectionParams = connectionParams
            #special is a yet undefined data type used for conditional movement such as the one blocked by the crowbar
            self.special = special
        def create_trigger(self):
            if(special == None):
                return (self.transform, self.width, self.height, self.connectionParams)
        def on_click(self):
            #theres gotta be a better way of doing this but idk python well enough
            a,b,c,d,e,f = self.connectionParams
            playerObj.move_room(a,b,c,d,e,f)
            renpy.call(self.connectionParams[2])

            
    mapManager = minimapManager()


screen minimap():
    python: 
        if mapManager == None:
            mapManager = minimapManager(playerData())
    $frameX, frameY = mapManager.format_map()
    frame align (0.5, 0.5) xsize frameX ysize frameY:
        padding (0,0)
        background None
        
        $currentRoom = 0
        for r in mapManager.draw_map():
            $trans, imagePath = r
            add imagePath:
                at trans
        $currentFrameX, currentFrameY = mapManager.currentFrame
        frame align(currentFrameX, currentFrameY) xsize 200 ysize 200:
            padding(0,0)
            background Solid("#00000011")
            for ct in mapManager.make_triggers():
                #have to recast these for some reason because it turns them into strings??? idk
                $w = float(ct.width)
                $h= float(ct.height)
                $x = float(ct.transform.xalign)
                $y = float(ct.transform.yalign)
                textbutton "Move":
                    text_size 20
                    xsize w
                    ysize h
                    xalign x
                    yalign y
                    action Function(ct.on_click)




        
