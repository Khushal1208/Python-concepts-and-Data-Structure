class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = []

    def enqueue(self,item):
        if(len(self.queue) < self.size):
            self.queue.append(item)
            print(f'{item} is inserted')
        else:
            print(f'Queue is full')

    def dequeue(self):
        if(self.queue):
            item = self.queue.pop(0)
            print(f"popped item is {item}")
            return  # if you don't write return then no issue
        else:
            print(f"Queue is empty")
            return 
        
    def display(self):
        print("The element are in the queue are: ")
        print(*self.queue)  
        # it is used print the list like 10 20 30 instead of [10,20,30]


size = 5
q = Queue(size)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)

q.display()

q.dequeue()
q.display()

