#singly linekd list as stacks
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_Node = Node(data)

        if self.top is None:
            self.top = new_Node
            self.top.next = None

        else:
            new_Node.next = self.top
            self.top = new_Node

    def pop(self):
        if self.top is None:
            print("Strack is Empty")

        elif self.top.next is None:
            print("Popped element is :", self.top.data)
            self.top = None
        else:
            temp = self.top
            print("Popped element is :", self.top.data)
            self.top = temp.next
            temp = None
    
    def display(self):
        if self.top is None:
            print("Stack is empty")

        else:
            print("Elements of the Stack are: ")
            current = self.top

            while current:
                print(current.data)
                current = current.next
            
            print("Top of the stack is: ",self.top.data)

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()

s.pop()
s.pop()

s.display()