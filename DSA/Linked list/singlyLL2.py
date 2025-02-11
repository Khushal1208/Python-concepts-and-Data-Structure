class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Traverse Linked List
    def traverse_LL(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Search for a value in LL
    def search_LL(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False
    
    # Find the length of LL
    def find_length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length
    
    # Insert at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        # If the list was empty, update tail as well
        if self.tail is None:
            self.tail = new_node

    # Insert at the end (O(1) using tail)
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Insert at a specific position
    def insertAtPos(self, pos, data):
        if pos < 1:
            print('Invalid Position!')
            return
        
        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:  # If list was empty
                self.tail = new_node
            return

        prev = self.head
        count = 1

        while count < pos - 1 and prev is not None:
            prev = prev.next
            count += 1

        if prev is None or prev.next is None and count < pos - 1:
            print('Invalid Position!')
            return

        new_node.next = prev.next
        prev.next = new_node

        # If inserted at last position, update tail
        if new_node.next is None:
            self.tail = new_node

    # Remove first node
    def removeFirstNode(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next

        # If list becomes empty, update tail
        if self.head is None:
            self.tail = None

        temp = None  # Free memory
        return self.head
    
    # Remove last node
    def removeLastNode(self):
        if self.head is None:
            return None

        if self.head.next is None:
            self.head = None
            self.tail = None
            return None

        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next

        # Update tail and remove last node
        second_last.next = None
        self.tail = second_last

        return self.head
    
    # Delete node at a specific position
    def delete_at_position(self, position):
        if self.head is None or position < 1:
            return self.head
        
        if position == 1:
            return self.removeFirstNode()
        
        current = self.head
        prev = None

        for _ in range(1, position):
            prev = current
            if current is None or current.next is None:
                print("Invalid Position!")
                return self.head
            current = current.next

        prev.next = current.next

        # If deleting last node, update tail
        if prev.next is None:
            self.tail = prev

        current = None  # Free memory
        return self.head

# Example Usage
ll = SinglyLL()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtBegin(5)
ll.insertAtPos(2, 15)
ll.traverse_LL()  # Output: 5 -> 15 -> 10 -> 20 -> None

ll.removeFirstNode()
ll.traverse_LL()  # Output: 15 -> 10 -> 20 -> None

ll.removeLastNode()
ll.traverse_LL()  # Output: 15 -> 10 -> None

ll.delete_at_position(2)
ll.traverse_LL()  # Output: 15 -> None
