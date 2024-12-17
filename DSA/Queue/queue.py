class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = self.rear = -1

    def enqueue(self,item):
        if(self.rear+1) % self.size == self.front:
            print(f'Queue is full')
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = item
            print(f"{item} is inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty") 
            return 
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = self.front+1 %self.size
            print(f'{item} is deleted from Queue')
            return 
        
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print(f"Queue elements are: ")

            i = self.front 
            while(True):

                print(self.queue[i] , end = " ")

                if i == self.rear:
                    break
                i = (i+1)%self.size

            print()


# Test Code
s = Queue(5)
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(80)
s.enqueue(90)
print("Queue:", s.display())
s.enqueue(100)  # Should show overflow message

s.front_rear()  # Display front and rear elements
s.dequeue()  # Remove the first element
print("Queue after dequeue:", s.display())

s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()  # Now the queue should be empty
s.dequeue()  # Should show underflow message
