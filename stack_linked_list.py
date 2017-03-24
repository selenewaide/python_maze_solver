
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
   
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
  
    def set_data(self, new_data):
        self.data = new_data
       
    def set_next(self, new_next):
        self.next = new_next

class linked_list_stack_adt:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def pop(self):
        if linked_list_stack_adt.is_empty(self) == True:
            msg = "Can't pop - this stack is empty"
            return msg
        else:
            current = self.head
            self.head = current.get_next()
            return current.get_data()
    
    def peek(self):
        current = self.head
        return current.get_data()
        
    def show_stack(self):
        current = self.head
        list_str = ""
        while current != None:
            list_str += current.get_data() + " "
            current = current.get_next()
        return list_str    
        
        
        
        
        
        
        
        
        
        