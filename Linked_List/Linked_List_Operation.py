class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.lenght = 1
        
    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append_item(self, value):
        new_node = Node(value)
        
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.lenght += 1
        
        return True
    
    def pop_item(self):
        if self.lenght == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1
        
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend_item(self, value):
        new_node = Node(value)
        
        if self.lenght == 0:   
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        
        return True
    
    def pop_first_item(self):
        if self.lenght == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.lenght -= 1
        
        if self.lenght == 0:
            self.tail = None
        return temp
    
    def get_node(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def set_value(self, index, value):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            if temp:
                temp.value = value
                return value
        return False
            
        
        
        
        

my_linked_list = LinkedList(10)
my_linked_list.append_item(20)
my_linked_list.append_item(50)
my_linked_list.append_item(60)
my_linked_list.prepend_item(5)
my_linked_list.pop_first_item()
my_linked_list.pop_item()
my_linked_list.set_value(1, 100)

print(my_linked_list.print_list())
print(my_linked_list.get_node(1))


