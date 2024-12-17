class Vehicle:
    def __init__(self, brand ,speed):
        self.brand =brand
        self.speed = speed
    
    def drive(self):
        print(f"The {self.brand} vehicle drives at {self.speed} km/h.")
    
class Car(Vehicle):
    def __init__(self,brand,speed,seats):
        super().__init__(brand,speed)
        self.seats = seats
    
    def drive(self):
        print(f"the {self.brand} car with {self.seats} seats drives at {self.speed} km/h. ")


vehicle = Vehicle("geneic",100)
car = Car("toyota",150,5)

vehicle.drive()
car.drive()