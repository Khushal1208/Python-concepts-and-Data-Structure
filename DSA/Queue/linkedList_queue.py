class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front.next is None:
            print("Popped element is: ",self.front.data)
            self.front = None
        
        else:
            temp = self.front
            print("Popped element is: ",self.front.data)
            self.front = temp.next
        
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("\nElements of queue are : ")
            current = self.front
            while current:
                print(current.data,end = " ")
                current = current.next
            print("\nfront of queue is : ",self.front.data)
            print("Rear of queue is : ",self.rear.data)
            print()

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

q.dequeue()
q.dequeue()

q.display()