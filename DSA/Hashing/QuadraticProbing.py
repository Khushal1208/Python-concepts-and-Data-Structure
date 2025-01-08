class Quadratic_probing:
    def __init__(self,size=10):
        self.size = size
        self.table = [None]*size

    def _hash(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self._hash(key)
        i = 0
        start_index = index
        while self.table[(index+i*i)%self.size] is not None:
            if self.table[(index+i*i)%self.size][0] == key:
                self.table[(index+i*i)%self.size] = (key,value)
                return
            i += 1
            if(i==self.size):
                raise Exception("Table is Full")
            
        self.table[(index+i*i)%self.size] = (key,value)

    def search(self,key):
        index =  self.hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            
            index = (index+1)%self.size
            if index == start_index:
                break
            return None 
    def delete(self,key):
        index = self.hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                next_index = (index+1)%self.size
                while self.table[next_index] is not None:
                    rehash_key,rehash_value = self.table[next_index]
                    self.table[next_index] = None
                    self.insert(rehash_key,rehash_value)
                    next_index = (next_index+1)%self.size
                return
        
            index = (index+1)%self.size
            if index == start_index:
                break

    def display(self):
        for i,pair in enumerate(self.table):
            print(f"Index {i}: {pair}")

qp = Quadratic_probing(5)
qp.insert(10,10)
qp.insert(7,20)
qp.insert(22,20)

qp.display()