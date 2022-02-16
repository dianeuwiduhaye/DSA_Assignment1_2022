class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
        
class UndoableList:
   def __init__(self):
      self.head=None
      self.commands = [] #Storing commands done
      self.redo_commands = [] #storing commands that are undone.


def undo(self):
    last_command=self.commands.pop()
    self.redo_commands.append(last_command) #storing last commands for redo purpose.
    name_of_command, node_value = last_command
    if name_of_command == "insert":
        self.delete(node_value)
    elif name_of_command =="delete":
        self.insert(node_value)
        
        
def redo(self):
    redo_command= self.redo_commands.pop() #popping the last command from the list of redo commands.
    name_of_command, node_value = redo_command
    if name_of_command == "insert":
        self.insert(node_value)
    elif name_of_command == "delete":
        self.delete(node_value)
        

#Inserting function
def insert(self,value):
    self.commands.append(["insert",value])
    new_node=Node(value) #creating the Node
    #when the head is empty
    if self.head is None:
        self.head=new_node
        return
    #when the value of the new node is less than the value of the head
    temp=self.head
    if temp.value > value:
            new_node.next = temp
            self.head = new_node
            return
    #when the value of the new node is greater than the value of the head
    while temp.next:
        if temp.next.value > value:
            break  
        temp = temp.next  
        
    new_node.next = temp.next  #pointer to the value of temp
    temp.next = new_node #Insert the new node after the temp
    
    
    # the deleting fuction
def delete(self, node):
    self.commands.append(["delete",node])
    #when the node to be deleted is the head
    if self.head.value == node:
        temp = self.head.next
        self.head = temp
        return
    # when the node to be deleted is in the middle.
    current = self.head
    while current.next:
        if current.next.value == node:
            break 
        current = current.next
    current.next = current.next.next
    
# the find function
def find(self, node):
    current = self.head
    while current:
        if current.value == node:
            return True
        else:
            current = current.next
    return False
#function to print a list
def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
            
 #function to undo  
def __init__(self):
        self.commands = {}
            
