class HashTable:
    def __init__(self,size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.table[index].append([key,value])

    def search(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
            
    def display(self):
        for i , j in enumerate(self.table):
            print(f'index{i}:{j}')

    
ht = HashTable(size=5)
ht.insert(10,10)
ht.insert(7,20)
ht.insert(2,20)

print("Hash Table")

ht.display()