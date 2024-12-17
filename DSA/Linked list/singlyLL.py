class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None

    def append(self,data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self,prev_data,data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        
        if not current:
            print(f'node with the data {prev_data} not found')
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self,key): #key is element
        current = self.head

        if current and current.data == key:
            self.head = current.next 
            current = None
            return 
        prev = None
        
        while current and  current.data != key :
            prev = current 
            current = current.next
        
        if not current:
            print(f'node with the data {key} is not found')
            return
        
        prev.next = current.next
        current = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data , end = "-> ")
            current = current.next
        print("None")


sl = SingleLinkedList()
sl.append(10)
sl.append(20)
sl.append(30)
print("intial list")
sl.prepend(5)

print("after inserting 5")
sl.print_linked_list()

sl.insert_after(2,15)

print("after inserting 15")
sl.print_linked_list()

sl.delete(5)
print("after deleting 5 key")
sl.print_linked_list()



