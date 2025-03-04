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
- This program has been written in Python, running the file, robot_script.py, in the terminal will allow you to test out all of Sam's commands

## Tests
- Prior to this project I had not yet learnt how to write tests so I spent some time researching Pythons' unittest module
- I tested to ensure the program:
    - Only accepted whole integers between 0 and 4 for moving Sam
    - That the distance moved was only 1 space
    - That the correct direction was moved based on which way the robot was facing