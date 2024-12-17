class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size

    def push(self,item):
        if(len(self.stack) <= self.max_size):
            self.stack.append(item)
            print(f"the {item} pushed!")

        else:
            print("stack overflow!")

    def isEmpty(self):
        return len(self.stack) == 0
    
    def POP(self):
        if not self.isEmpty():
            item = self.stack.pop()
            print(f"{item} popped!")
        print("stack underflow!")
        return None
    
    def peek(self):
        if not self.isEmpty():
            print("top element is:",self.stack[-1]) # negative indexing for last element
            return self.stack[-1]
        print("no element to show")
        return None
    
    def display(self):
        return self.stack


s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print(s.display)

s.peek()
s.POP()

print(s.display())
