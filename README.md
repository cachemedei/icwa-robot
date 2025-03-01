# Sam the Robot

You have a toy robot on a tabletop, a grid of 5 x 5 units with no obstructions. You can issue commands to the robot to allow it to roam around the tabletop. But be careful, don't let it fall off!

## Sam is able to follow these commands

### place(x, y, facing)
- This puts Sam on the table at coordinates (X, Y) and facing either North, South, East or West
- The origin (0, 0) is the South-West corner
- You can place Sam as many times as you want but before anything else you must place him on the table first!

### move()
- This command moves Sam forward 1 space in the direction he is currently facing

### left()
- Sam will turn to face whichever direction is left to where he is currently facing (if facing North, Sam will turn to face West)

### right()
- Sam will turn to face whichever direction is right to where he is currently facing (if facing North, Sam will turn to face East)

### report()
- Sam will tell you his coordinates and which direction he is currently facing

## Running Sam's Program
- This program has been written in Python, running the file, toy_robot.py, in a terminal will allow you to test out all of Sam's commands