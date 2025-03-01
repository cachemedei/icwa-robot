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


sam = Robot()
sam.report()
sam.place(2, 4, "East")
sam.report()