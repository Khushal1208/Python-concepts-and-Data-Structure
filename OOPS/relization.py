from abc import ABC,abstractmethod
#method are not defined and can be used by child classes 
# it is similar to interfaces in java 
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    

class Dog(Animal):
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Run"
    
dog=Dog()
print(dog.sound())
print(dog.move())