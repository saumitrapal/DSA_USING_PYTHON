class Node():   #class
    def __init__(self, value):  #constructor
        self.value = value  #attribute
        self.next = None    #attribute
        
class LinkedList():     #class
    def __init__(self, value):  #constructor
        new_node = Node(value)
        self.head = new_node    #attribute 
        self.tail = new_node    #attribute
        self.length = 1         #attribute
        
    def print_list(self):   #method
        temp = self.head    #attribute
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0   
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return next
        
my_linked_list = LinkedList(4)  #instance or object of LinkedList class
my_linked_list.empty()
my_linked_list.append(5)
my_linked_list.append(6)


print(my_linked_list.print_list())

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print('Head and tail are the same node:', my_linked_list.head is my_linked_list.tail)
        

