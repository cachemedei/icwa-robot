from toy_robot import Robot

def command_sam():
    x = int(input("Choose Sam's X coordinate (Between 0 and 4): "))
    y = int(input("Choose Sam's Y coordinate (Between 0 and 4): "))
    direction = input("Which direction do you want Sam to face? (North, South, East or West)? ")

    return (x, y, direction)

def main():
    sam = Robot()

    while True:
        print("Commands for Sam: PLACE, MOVE, LEFT, RIGHT, REPORT, EXIT")
        command = input("Enter a command for Sam: ").strip().upper()

        if command == "PLACE":
            x, y, direction = command_sam()
            sam.place(x, y, direction)
            print(f"Sam is at ({sam.posX}, {sam.posY}) facing {sam.face}")

        elif command == "MOVE":
            if sam.is_placed:
                sam.move()
                print(f"Sam is now at ({sam.posX}, {sam.posY})")
            else:
                print("Please place Sam on the table!")

        elif command == "LEFT":
            if sam.is_placed:
                sam.left()
                print(f"Sam is now facing {sam.face}")
            else:
                print("Please place Sam on the table!")

        elif command == "RIGHT":
            if sam.is_placed:
                sam.right()
                print(f"Sam is now facing {sam.face}")
            else:
                print("Please place Sam on the table!")

        elif command == "REPORT":
            sam.report()

        elif command == "EXIT":
            break

        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()