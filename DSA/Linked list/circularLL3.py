class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Only used in Doubly Circular Linked List



# Circular Singly Linked List (CSLL)
class CircularSinglyLL:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")
    
    def insertAtEmpty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = new_node  # Circular link
    
    def insertAtBegin(self, data):
        if not self.head:
            self.insertAtEmpty(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        self.head = new_node
    
    def insertAtEnd(self, data):
        if not self.head:
            self.insertAtEmpty(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    
    def deleteFirst(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
    
    def deleteLast(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head
    
    def search(self, key):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False




# Doubly Circular Linked List (DCLL)
class DoublyCircularLL:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")
    
    def insertAtEmpty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = new_node
        new_node.prev = new_node
    
    def insertAtBegin(self, data):
        if not self.head:
            self.insertAtEmpty(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node
        self.head = new_node
    
    def insertAtEnd(self, data):
        if not self.head:
            self.insertAtEmpty(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node
    
    def deleteFirst(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next
    
    def deleteLast(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
    
    def search(self, key):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False



# Example Usage
csll = CircularSinglyLL()
csll.insertAtEnd(10)
csll.insertAtEnd(20)
csll.insertAtBegin(5)
csll.traverse()  # Output: 5 -> 10 -> 20 -> (Back to Head)

csll.deleteFirst()
csll.traverse()  # Output: 10 -> 20 -> (Back to Head)

csll.deleteLast()
csll.traverse()  # Output: 10 -> (Back to Head)

dcll = DoublyCircularLL()
dcll.insertAtEnd(100)
dcll.insertAtEnd(200)
dcll.insertAtBegin(50)
dcll.traverse()  # Output: 50 <-> 100 <-> 200 <-> (Back to Head)

dcll.deleteFirst()
dcll.traverse()  # Output: 100 <-> 200 <-> (Back to Head)

dcll.deleteLast()
dcll.traverse()  # Output: 100 <-> (Back to Head)
