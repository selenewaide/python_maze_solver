'''
@author: selenewaide
'''

# ADT stack using python list
class current_path:
    def __init__(self):
        self.items = []
     
    # is the stack empty - returns a boolean   
    def is_empty(self):
        return self.items == []
     
    # to add an item
    def push(self, item):
        self.items.append(item)
        return self
     
    # to remove an item and return it  
    def pop(self):
        if current_path.is_empty(self) == True:
            msg = "Can't pop - this stack is empty"
            return msg
        else:
            return self.items.pop()
     
    # to view the last element, i.e. top of the stack
    def peek(self):
        if not self.items:
            return ''
        return self.items[len(self.items)-1]
     
    # returns the size of the list
    def size(self):
        return len(self.items)
    
    # show the list of items in the stack
    def show_stack(self):
        return self.items
     
     
    

