import sys
from maze_scripts.stack_linked_list import *

def test_linked_list(did_pass):
    """ Print the result of a test_linked_list. """
    line_num = sys._getframe(1).f_lineno # Get the caller’s line number.
           
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else :
        msg = ("Test at line {0} FAILED.".format(line_num))
    print (msg)


def tests_simple_linked_list():
    
    test_linked_list_stack = linked_list_stack_adt()

    print("LINKED LISTS TESTS: ")
    print("Is the stack empty: ", test_linked_list_stack.is_empty())
    test_linked_list(test_linked_list_stack.is_empty() == True) 
    print()
    
    test_linked_list_stack.push("One") 
    test_linked_list_stack.push("Two") 
    test_linked_list_stack.push("Three") 
    test_linked_list_stack.push("Four") 
    test_linked_list_stack.push("Five") 
    
    print("Is the stack empty after 5 pushes: ", test_linked_list_stack.is_empty())
    test_linked_list(test_linked_list_stack.is_empty() == False) 
    print()
    
    print("How big is the stack now: ", test_linked_list_stack.size())
    test_linked_list(test_linked_list_stack.size() == 5)
    print()
    
    print("What is in the stack: ", test_linked_list_stack.show_stack())
    test_linked_list(test_linked_list_stack.show_stack() == "Five Four Three Two One ")
    print()
    
    print("What is at the top of the stack: ", test_linked_list_stack.peek() )
    test_linked_list(test_linked_list_stack.peek() == "Five")
    print()
     
    print("Pop the stack.")
    test_linked_list(test_linked_list_stack.pop() == "Five") 
    print()
    
    print("What is in the stack: ", test_linked_list_stack.show_stack())
    test_linked_list(test_linked_list_stack.show_stack() == "Four Three Two One ")
    print()
    
    print("How big is the stack now: ", test_linked_list_stack.size())
    test_linked_list(test_linked_list_stack.size() == 4)
    print()
    
    print("What is at the top of the stack: ", test_linked_list_stack.peek())
    test_linked_list(test_linked_list_stack.peek() == "Four") 
    print()
    
    print("Testing for popping when the stack is empty.")
    test_linked_list(test_linked_list_stack.pop() == "Four") 
    test_linked_list(test_linked_list_stack.pop() == "Three") 
    test_linked_list(test_linked_list_stack.pop() == "Two") 
    test_linked_list(test_linked_list_stack.pop() == "One") 
    
    print("What happens to pop when the stack is empty: ", test_linked_list_stack.pop())
    test_linked_list(test_linked_list_stack.pop() == "Can't pop - this stack is empty") 
 
tests_simple_linked_list()