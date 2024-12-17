class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)

        if self.isEmpty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        
        self.head = new_node

    
    def insertAfter(self,prev_data,data):
        current = self.head
        
        while current and current.data != prev_data:
            current = current.next

        if not current:
            print(f'node with the data {prev_data} not found')
            return
        
        new_node = Node(data)
        new_node.prev = current
        new_node.next = current.next

        if current.next:
            current.next.prev = new_node
        
        current.next = new_node

    def delete(self,key):
        current = self.head

        # case 1: if node is head
        if current and current == key :
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        
        # case 2: traverse to find node to delete

        while current and current.data != key:
            current = current.next

        # if the node is not found
        if not current:
            print(f'node with the data {key} not found')
            return
        
        # case 3: delete the node
        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data , end = "-> ")
            current = current.next
        print("None")



dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.print_linked_list()  

dll.prepend(5)
dll.print_linked_list()  

dll.insertAfter(20, 25)
dll.print_linked_list() 

dll.delete(10)
dll.print_linked_list() 
