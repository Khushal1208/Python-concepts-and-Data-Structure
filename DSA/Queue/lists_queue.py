def enqueue():
    n = int(input("enter the element to be inserted into queue: "))
    queue.append(n)

def dequeue():
    if len(queue) == 0 :
        print("\nQueue is empty")
        print()

    else: 
        print(queue[0]," is the element deleted from queue")
        # queue[0].pop()
        del queue[0]
        print()

def display():
    if len(queue) == 0 :
        print("\nQueue is empty")
        print()

    else:
        print("\nQueue elements are: ")
        for i in queue:
            print(i ,end = " ")
        print("\nfront of the queue is ",queue[0])
        print("Rear of the queue is ", queue[-1])

queue = list()

while(1):
    print("\nEnter the option from below: \n1-enqueue\n2-dequeue\n3-display\n4-exit")
    option = int(input())
    if option == 1:
        print("\nEnqueue operation")
        enqueue()
    elif option == 2:
        print("\nDequue Operation")
        dequeue()
    elif option == 3:
        print("\nDisplay")
        display()

    else: 
        break