import sys
from maze_scripts.stack_array import *

def test_array(did_pass):
    """ Print the result of a test_array. """
    line_num = sys._getframe(1).f_lineno # Get the caller’s line number.
           
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else :
        msg = ("Test at line {0} FAILED.".format(line_num))
    print (msg)


def tests_simple_array():
    
    test_stack = current_path()

    print("ARRAY TESTS: ")
    print("Is the stack empty: ", test_stack.is_empty())
    test_array(test_stack.is_empty() == True) 
    print()
    
    test_stack.push("One") 
    test_stack.push("Two") 
    test_stack.push("Three") 
    test_stack.push("Four") 
    test_stack.push("Five") 
    
    print("Is the stack empty after 5 pushes: ", test_stack.is_empty())
    test_array(test_stack.is_empty() == False) 
    print()
    
    print("How big is the stack now: ", test_stack.size())
    test_array(test_stack.size() == 5)
    print()
    
    print("What is in the stack: ", test_stack.show_stack())
    test_array(test_stack.show_stack() == ['One', 'Two', 'Three', 'Four', 'Five'])
    print()
    
    print("What is at the top of the stack: ", test_stack.peek() )
    test_array(test_stack.peek() == "Five")
    print()
     
    print("Pop the stack.")
    test_array(test_stack.pop() == "Five") 
    print()
    
    print("What is in the stack: ", test_stack.show_stack())
    test_array(test_stack.show_stack() == ['One', 'Two', 'Three', 'Four'])
    print()
    
    print("How big is the stack now: ", test_stack.size())
    test_array(test_stack.size() == 4)
    print()
    
    print("What is at the top of the stack: ", test_stack.peek())
    test_array(test_stack.peek() == "Four") 
    print()
    
    print("Testing for popping when the stack is empty.")
    test_array(test_stack.pop() == "Four") 
    test_array(test_stack.pop() == "Three") 
    test_array(test_stack.pop() == "Two") 
    test_array(test_stack.pop() == "One") 
    
    print("What happens to pop when the stack is empty: ", test_stack.pop())
    test_array(test_stack.pop() ==  "Can't pop - this stack is empty") 
 
    
   
tests_simple_array()