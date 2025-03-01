class Robot():
    def __init__(self):
        self.is_placed = False # Flag to make sure Sam is placed first
        self.posX = 0
        self.posY = 0
        self.face = "North"

    # Print Sam's location
    def report(self):
        if not self.is_placed:
            print("Please place Sam on the board!")
        else:
            print(f"Coordinates: ({self.posX}, {self.posY}) | Facing: {self.face.title()}")
    
    def validPos(self, xcoord, ycoord):
        if 0 <= xcoord <= 4 and 0 <= ycoord <= 4:
            return True
        
    def validDirection(self, direction):
        if direction == "North" or direction == "South" or direction == "East" or direction == "West":
            return True

    # Place Sam on table
    def place(self, x, y, facing):
        face = facing.title()
        # Validate placement
        if self.validPos(x, y) == True and self.validDirection(face) == True:
            self.posX = x
            self.posY = y
            self.face = face
            self.is_placed = True
        else:
            print("Please provide coordinates within (0, 0) and (4, 4) and a direction of North, South, East or West")

    def forward(self, pos):
        return pos + 1 if pos < 4 else pos
    
    def backward(self, pos):
        return pos - 1 if pos > 0 else pos

    # Move Sam 1 space
    def move(self):
        if self.is_placed == True:
            
            # facing north => increase Y
            if self.face == "North":
                self.posY = self.forward(self.posY)

            # facing south => decrease Y
            elif self.face == "South":
                self.posY = self.backward(self.posY)

            # facing east => increase X
            elif self.face == "East":
                self.posX = self.forward(self.posX)

            # facing west => decrease X
            else:
                self.posX = self.backward(self.posX)
    
    def right(self):
        if self.is_placed:
            directions = ["North", "East", "South", "West"]
            self.face = directions[(directions.index(self.face) + 1) % 4]

    def left(self):
        if self.is_placed:
            directions = ["North", "West", "South", "East"]
            self.face = directions[(directions.index(self.face) + 1) % 4]

sam = Robot()

sam.place(2, 2, "east")
sam.report()
sam.move()
sam.report()


