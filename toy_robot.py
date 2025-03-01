class Robot():
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.face = "North"

    # Print Sam's location
    def report(self):
        print(f"Coordinates: ({self.posX}, {self.posY}) | Facing: {self.face}")

    # Place Sam on table
    def place(self, x, y, facing):
        self.posX = x
        self.posY = y
        self.face = facing

    # Move Sam 1 space
    def move(self):
        # facing north => increase Y
        if self.face == "North":
            self.posY += 1
            if self.posY > 4:
                self.posY = 4

        # facing south => decrease Y
        elif self.face == "South":
            self.posY -= 1
            if self.posY < 0:
                self.posY = 0

        # facing east => increase X
        elif self.face == "East":
            self.posX += 1
            if self.posX > 4:
                self.posX = 4

        # facing west => decrease X
        elif self.face == "West":
            self.posX -= 1
            if self.posX < 0:
                self.posX = 0
    
    def right(self):
        if self.face == "North":
            self.face = "East"
        elif self.face == "East":
            self.face = "South"
        elif self.face == "South":
            self.face = "West"
        else: self.face = "North"

    def left(self):
        if self.face == "North":
            self.face = "West"
        elif self.face == "East":
            self.face = "North"
        elif self.face == "South":
            self.face = "East"
        else: self.face = "South"

sam = Robot()
sam.report()
sam.place(2, 4, "East")
sam.report()
sam.right()
sam.move()
sam.move()
sam.report()