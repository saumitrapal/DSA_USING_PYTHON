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
        return temp
    
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
            
    def insert_value(self, index, value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0:
            return self.prepend_item(value)
        if index == self.lenght:
            return self.append_item(value)

        new_node = Node(value)
        temp = self.get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True
    
    def remove_item(self, index):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first_item()
        if index == self.lenght - 1:
            return self.pop_item()
        
        prev = self.get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.lenght -= 1
        return temp
    
    def reverse(self):
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            

my_linked_list = LinkedList(10)
my_linked_list.append_item(20)
my_linked_list.append_item(50)
my_linked_list.append_item(60)
my_linked_list.prepend_item(5)
my_linked_list.pop_first_item()
my_linked_list.pop_item()
my_linked_list.set_value(1, 100)
my_linked_list.insert_value(2, 200)
my_linked_list.remove_item(1)
my_linked_list.reverse()

print(my_linked_list.print_list())
# print(my_linked_list.get_node(1))
