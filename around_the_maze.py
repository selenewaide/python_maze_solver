import os
import pprint
#from maze_scripts_0.find_path import*

grid = None
robot_x,robot_y = 0,0
goal_x,goal_y = 0,0

def create_world(filename):
    
    width = 0
    height = 0
    
    global grid
    global robot_x, robot_y
    global goal_x,goal_y
    
    # Check whether the file exists
    if not os.path.isfile(filename):
        print("File " + filename + " does not exist.")
    else:
    # Open the file for reading
        fh1 = open(filename, "r")
        
        for line in fh1:
            if line[0] == "w":
                coord_x = int(line[2])
                coord_y = int(line[4])
                grid[coord_x][coord_y] = 1
                
            elif line[0] == "r":
                robot_x = int(line[5])
                robot_y = int(line[7])
                
            elif line[0] == "g":
                goal_x = int(line[5])
                goal_y = int(line[7])
                
            else:
                width = int(line[0])
                height = int(line[2])
                grid = [[0]*width for _ in range(height)]
                
    fh1.close()
    return grid
    

def where_is_robot():
    global robot_x, robot_y
    return robot_x, robot_y


def is_feasible(x,y):
    global grid
    
    if x < 0 or y < 0:
        return False
    
    if x >= len(grid) or y >= len(grid[0]):
        return False
    
    return grid[x][y] == 0
        
    

def move_robot(x, y):
    global robot_x, robot_y
    robot_x = x
    robot_y = y
    

def goal_reached():
    global goal_x, goal_y
    global robot_x, robot_y
    
    if robot_x == goal_x and robot_y == goal_y:
        return True
    else:
        return False
    
def print_grid(grid):
    #global grid
    global robot_x, robot_y
    global goal_x,goal_y
    
    print()
    print("MAZE:")
    print("------------------------")
    
    for x in range(0,len(grid)):
        for y in range(0,len(grid)):
            if x == robot_x and y == robot_y:
                print("|R|", end="")
            elif x == goal_x and y == goal_y:
                print("|G|", end="")  
            elif grid[x][y] == 0:
                print("|_|", end="")
            elif grid[x][y] == 1:
                print("|#|", end="") 
            elif grid[x][y] == True:
                print("|r|", end="") # printing the robots path
                  
        print()
    print("------------------------")
    print()
    
