class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Traversal - Forward and Backward
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")

    # Search for a value in DLL
    def search_DLL(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    # Find the length of DLL
    def find_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # Insert at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Insert at a specific position
    def insertAtPos(self, pos, data):
        if pos < 1:
            print("Invalid Position!")
            return

        new_node = Node(data)

        if pos == 1:
            self.insertAtBegin(data)
            return

        current = self.head
        for _ in range(pos - 2):
            if current is None:
                print("Invalid Position!")
                return
            current = current.next

        if current is None or current.next is None:
            self.insertAtEnd(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    # Delete the first node
    def removeFirstNode(self):
        if not self.head:
            print("List is empty!")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete the last node
    def removeLastNode(self):
        if not self.head:
            print("List is empty!")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Delete a node at a specific position
    def delete_at_position(self, pos):
        if not self.head or pos < 1:
            print("Invalid Position!")
            return

        if pos == 1:
            self.removeFirstNode()
            return

        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Invalid Position!")
                return
            current = current.next

        if current is None or current.next is None:
            self.removeLastNode()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

# Example Usage
dll = DoublyLL()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtBegin(5)
dll.insertAtPos(2, 15)
dll.traverse_forward()   # Output: 5 ⇄ 15 ⇄ 10 ⇄ 20 ⇄ None
dll.traverse_backward()  # Output: 20 ⇄ 10 ⇄ 15 ⇄ 5 ⇄ None

dll.removeFirstNode()
dll.traverse_forward()   # Output: 15 ⇄ 10 ⇄ 20 ⇄ None

dll.removeLastNode()
dll.traverse_forward()   # Output: 15 ⇄ 10 ⇄ None

dll.delete_at_position(2)
dll.traverse_forward()   # Output: 15 ⇄ None
