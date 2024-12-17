class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        self.head = new_node
        current.next = self.head

    def insertAfter(self, key, data):
        if self.isEmpty():
            print("List is empty, cannot insert.")
            return
        current = self.head
        while current.data != key:
            current = current.next
            if current == self.head:
                print(f"Node with data {key} not found.")
                return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        if self.isEmpty():
            print("List is empty, cannot delete.")
            return
        current = self.head
        if current.data == key:
            if current.next == self.head:
                self.head = None
                print(f"Deleted the only node with data {key}.")
                return
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            print(f"Deleted head node with data {key}.")
            return
        prev = None
        while current.data != key:
            prev = current
            current = current.next
            if current == self.head:
                print(f"Node with data {key} not found.")
                return
        prev.next = current.next
        print(f"Deleted node with data {key}.")

    def print_linked_list(self):
        if self.isEmpty():
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")



cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

cll.print_linked_list() 

cll.prepend(5)

cll.print_linked_list()  

cll.insertAfter(20, 25)

cll.print_linked_list()  

cll.delete(10)

cll.print_linked_list()  

cll.delete(5)

cll.print_linked_list() 