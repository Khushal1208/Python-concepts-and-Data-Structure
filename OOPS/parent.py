class Parent:
    def __init__(self, name, age):
        self.parent_name = name
        self.parent_age = age

    def display(self):
        print(f"Parent Name: {self.parent_name}\nParent Age: {self.parent_age}")

class Child(Parent):
    def __init__(self,name,age):
        super().__init__("khushal", 20)

c = Child("Narsimha",28)
c.display()
