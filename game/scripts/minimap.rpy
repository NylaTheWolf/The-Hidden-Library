image decal scratchout = "images/minimap_images/decal1"
image decal qqq = "images/minimap_images/decal3"
image decal hallway = "images/minimap_images/decal2"

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
                "room4": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom4Map.png")),
                "room5": copy.deepcopy(minimapRoomData("images/minimap_images/tempRoom5Map.png"))
            }
            cData = json.load(renpy.file("data/roomConnections.json"))
            for roomKey in cData:
                for direction in cData[roomKey]["exits"]:
                    cn = cData[roomKey]["exits"][direction]
                    cnParams = cn["connectionParams"]
                    ctParams = cn["triggerParams"]
                    rotation = 0
                    if len(cnParams)>4:
                        rotation = int(cnParams[4])
                    imW, imH = renpy.image_size(self.rooms[cnParams[0]].image)
                    imW2, imH2 = renpy.image_size(self.rooms[roomKey].image)
                    tx = int(cnParams[2])
                    
                    # if rotation == 2:
                    #     print("init rotate")
                    #     tx*=-1
                    #     tx += -imW/2 +imW2/2
                    # else:
                    tx += imW/2 - imW2/2
                    ty = int(cnParams[3])
                    # if rotation == 2:
                    #     ty *= -1
                    #     ty += -imH/2 +imH2/2
                    # else:
                    ty += imH/2 -imH2/2
                    connection = copy.deepcopy(minimapClickTrigger(
                        Transform(xalign = float(ctParams[0]), yalign = float(ctParams[1])),
                        float(ctParams[2]),
                        float(ctParams[3]),
                        (
                            roomKey,
                            int(direction),
                            cnParams[0],
                            int(cnParams[1]),
                            tx,
                            ty
                        ),
                        rotation
                    ))
                    self.rooms[roomKey].clickTransitions.append(connection)
                    


            #use for draw order to simulate character updating map in real time
            self.connectionList = []
            #hardcoded for current atrium map png, change later
            self.mapScale = 1
            self.top = -147
            self.bottom = 146
            self.left = -150
            self.right = 150
            self.currentFrame = (0,0,299,293)

        def update_rooms(self):
            
            if playerObj.lastExit != None:
                if playerObj.currentRoom == "atrium":
                    fy = 0
                    if (self.bottom - self.top - 293) != 0:
                        fy = (-147-self.top)/(self.bottom-self.top - 293)
                    fx = 0
                    if (self.right - self.left - 299) != 0:
                        fx = (-150-self.left)/(self.right - self.left - 299)
                    self.currentFrame = (fx,fy, 299, 293)
                    playerObj.relativeX = 0
                    playerObj.relativeY = 0
                    playerObj.relativeRotation = 0
                else:
                    #check if the last room/exit combo the player used was already traversed
                    current = self.rooms[playerObj.lastRoom].connections[playerObj.lastExit]
                    #if not, establish a new link
                    current = minimapRoomConnection(
                        playerObj.lastExit, 
                        playerObj.lastEntry, 
                        playerObj.relativeX,
                        playerObj.relativeY,
                        self.rooms[playerObj.lastRoom],
                        self.rooms[playerObj.currentRoom],
                        playerObj.relativeRotation*90
                    )
                    renpy.change_zorder("master", "hud", 105)
                    self.rooms[playerObj.lastRoom].connections[playerObj.lastExit] = current
                    self.connectionList.append(current)

        #use this to get the bounds of the map
        def format_map(self):
            for r in self.rooms.values():
                #N/S/E/W are indexes 0-3
                for i in range(len(r.connections)):
                    connection = r.connections[i]
                    if connection != None:
                        cWidth, cHeight = renpy.image_size(connection.other.image)
                        self.left = min(self.left, connection.offsetX - cWidth/2)
                        self.right = max(self.right, connection.offsetX + cWidth/2)
                        self.top = min(self.top, connection.offsetY)
                        self.bottom = max(self.bottom, connection.offsetY + cHeight)
            #relative size for frame (idk if I want to use this yet, depends on minimap vs map distinction)
            self.mapScale = min(200/self.right, 200/self.bottom)
            return int(self.right - self.left), int(self.bottom - self.top)

        #horrendously inneficient code but its fine for a small project
        def draw_map(self):
            drawRooms = []
            frameWidth = self.right - self.left
            frameHeight = self.bottom - self.top
            #hardcoded atrium draw, change if check values once image updated
            atrX = (-self.left)/(frameWidth)
            atrY = (-self.top)/(frameHeight)
            atriumTransform = Transform(xalign = atrX, yalign = atrY, anchor = (0.5, 0.5))
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
                tx = (cLeft)/(frameWidth)
                ty = (cTop)/(frameHeight)
                
                transform = Transform(xalign = tx, yalign = ty, anchor = (0.5, 0.5), rotate_pad = False)
                if(r.rotation != 0):
                    transform.rotate = r.rotation
                for dr in drawRooms:
                    #avoid duplicate draws while still being able to draw the same room in multiple places
                    #potentially it would be better to just have rooms with impossible entrances be represented by multiple objects, but idk
                    if tx == dr[0].xalign and ty == dr[0].yalign:
                        drawn = True
                if self.rooms[playerObj.currentRoom] == r.other:
                    fw = (cLeft-cWidth/2)/(frameWidth-cWidth)
                    fh = (cTop-cHeight/2)/(frameHeight-cHeight)
                    self.currentFrame = (fw, fh, cWidth, cHeight)
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
        def __init__(self, exitDirection, entryDirection, offsetX, offsetY, this, other, rotation):
            self.exitDirection = exitDirection
            self.entryDirection = entryDirection
            self.offsetX = offsetX
            self.offsetY = offsetY
            self.this = this
            self.other = other
            self.rotation = rotation
        
    class minimapClickTrigger:
        def __init__(self, transform, width, height, connectionParams, rotation,special = None):
            self.transform = transform
            self.width = width
            self.height = height
            self.connectionParams = connectionParams
            self.rotation = rotation
            #special is a yet undefined data type used for conditional movement such as the one blocked by the crowbar
            self.special = special
        def create_trigger(self):
            tx = self.transform.xalign
            ty = self.transform.yalign
            if (playerObj.relativeRotation)%4 == 2:
                tx = 1.0-tx
                ty = 1.0-ty
            if(self.special == None):
                return (Transform(xalign = tx, yalign = ty), self.width, self.height)
        def on_click(self):
            #theres gotta be a better way of doing this but idk python well enough
            key,b,c,d,xpos,ypos = self.connectionParams
            playerObj.move_room(key,b,c,d,xpos,ypos,self.rotation)
            #renpy.transition(moveoutbottom)
            renpy.hide_screen("minimap")
            
            renpy.call(self.connectionParams[2])
           

screen minimap():
    python: 
        if mapManager == None:
            mapManager = minimapManager()
    $ frameX, frameY = mapManager.format_map()
    frame align (0.5, 0.5) xsize frameX ysize frameY:
        padding (0,0)
        background Solid("#fff")
        
        $currentRoom = 0
        for r in mapManager.draw_map():
            $trans, imagePath = r
            $tempRot = trans.rotate
            add imagePath:
                at trans
                
        $currentFrameX, currentFrameY, currentW, currentH = mapManager.currentFrame
        frame align(currentFrameX, currentFrameY) xsize currentW ysize currentH:
            padding(0,0)
            background Solid("#00000011")
            for ct in mapManager.make_triggers():
                #have to recast these for some reason because it turns them into strings??? idk
                $trans2, w, h = ct.create_trigger()
                textbutton "Move":
                    text_size 20
                    xsize w
                    ysize h
                    anchor (0.5, 0.5)
                    at trans2
                    action Function(ct.on_click)




        
