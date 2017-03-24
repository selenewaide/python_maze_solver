import sys
from maze_scripts.around_the_maze import*

wasHere = None
correctPath = None #The solution to the maze

width = None
height = None




def solveMaze():
    
    global width, height
    global wasHere, correctPath
    
    maze = create_world("world2.dat") # Create Maze (0 = path, 1 = wall)
    
    print("Original maze:", end = "")
    print_grid(maze)
    
    width = len(maze)
    height = len(maze[0])
    
    wasHere = [[False]*width for _ in range(height)]
    correctPath = [[False]*width for _ in range(height)] #The solution to the maze
    
    
    startX, startY = where_is_robot()
       
    has_maze_been_solved = recursiveSolve(maze, startX, startY);
    if has_maze_been_solved:
        print("Has maze been solved? YES!");
    else:
        print("Has maze been solved? No.");
        
    print("Solved Maze:", end = "")
    print_grid(maze)
    
    print("Correct Path:", end = "")
    print_grid(correctPath);
    
    
def recursiveSolve(maze, x, y):
    
    global width, height
    global wasHere, correctPath
    
    move_robot(x, y)
    
    x,y = where_is_robot()

    # If you reached the end 
    if goal_reached():
        return True

    if (not is_feasible(x,y) or wasHere[x][y]):
        return False
    
    # If you are on a wall or already were here
    wasHere[x][y] = True;
    
    if (recursiveSolve(maze, x-1, y)):  # Recalls method one to the left
        correctPath[x][y] = True; # Sets that path value to true;
        return True;
    


    if (recursiveSolve(maze, x+1, y)):  # Recalls method one to the right
        correctPath[x][y] = True;
        return True;
    

    if (recursiveSolve(maze, x, y-1)): # Recalls method one up
        correctPath[x][y] = True;
        return True;
    

    if (recursiveSolve(maze, x, y+1)): # Recalls method one down
        correctPath[x][y] = True;
        return True;
    
    return False;


# Kicks it all off
solveMaze();



