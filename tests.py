import sys
from maze_scripts.around_the_maze import *

def test_array(did_pass):
    """ Print the result of a test_array. """
    line_num = sys._getframe(1).f_lineno # Get the caller’s line number.
           
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else :
        msg = ("Test at line {0} FAILED.".format(line_num))
    print (msg)

def tests_simple_array():
    # Create the world
    grid = create_world("world1.dat") # basic tests
    
    print("Initial position.", end="")
    print_grid(grid) 
    
    
    print("TESTS: ")
    test_array(where_is_robot() == (7, 0)) 
    test_array(is_feasible(1, 0) == True) 
    test_array(is_feasible(6, 0) == True) 
    test_array(is_feasible(0, -1) == False) 
    test_array(is_feasible(-1, 0) == False) 
    test_array(is_feasible(-1, -1) == False) 
    move_robot (6 , 0)
    move_robot (5 , 0)
    test_array(where_is_robot() == (5, 0))

    # move the robot to the goal and test_array whether it is detected
    move_robot(4,0)
    move_robot(3,0)
    move_robot(2, 0)
    move_robot(1,0) 
    move_robot(0, 0) 
    move_robot(0, 1)
    move_robot(0, 2) 
    move_robot(0, 3)
    test_array(where_is_robot() == (0, 3)) 
    test_array(goal_reached () == False )

    move_robot(0,4)
    move_robot(0,5)
    move_robot(0,6)
    move_robot(0,7)
    test_array(where_is_robot() == (0, 7)) 
    test_array (goal_reached () == True)
   
    print()
    print("Final position, robot at goal", end="")
    print_grid(grid) 
   
tests_simple_array()