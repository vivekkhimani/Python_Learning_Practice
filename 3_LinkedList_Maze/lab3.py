from rooms import Room
import maze

my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dining room?"))
my_rooms.append(Room("This room is exit. Good Job!"))

my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
my_rooms[1].setEast(my_rooms[2])
my_rooms[2].setWest(my_rooms[1])

my_maze = maze.MyMaze(my_rooms[0],my_rooms[2])

print(my_rooms[0])
user_input = input("Enter direction to move north west east south./n")

def TestVar(user_input):
    if user_input.lower() == "west":
        test_var = my_maze.moveWest()
    elif user_input.lower() == "north":
        test_var = my_maze.moveNorth()
    
    elif user_input.lower() == "south":
        test_var = my_maze.moveSouth()

    elif user_input.lower() == "east":
        test_var = my_maze.moveEast()
    
    elif user_input.lower() == "reset":
        test_var = "Reset"
    
    return test_var

print(my_rooms[0])
user_input = input("Enter direction to move north west east south./n")

while True:
    if TestVar(user_input) == False:
        print("Direction invalid. Try again.")
        print(my_rooms[my_maze.getCurrent()])
        user_input = input("Enter direction to move north west east south./n")
        
    elif TestVar(user_input) == True:
        print("You went",user_input)
        if my_maze.atExit() == True:
            print(my_rooms[my_maze.getCurrent()])
            print("Congratulations")
            break
        
        else:
            print(my_rooms[my_maze.getCurrent()])
            user_input = input("Enter direction to move north west east south./n")
            
    elif TestVar(user_input) == "Reset":
        my_maze.reset()
        print("You went back to start.")
            
            
            
        

