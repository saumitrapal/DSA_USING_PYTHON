# Create a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create LinkedList class with __init__() constructor.
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

my_linked_list = LinkedList(30)

#print linke list value
print(my_linked_list.head.value)