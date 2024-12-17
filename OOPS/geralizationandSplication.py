class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

class Manager(Employee):  # Specialization
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing the {self.department} department.")

class Intern(Employee):  # Specialization
    def __init__(self, name, salary, mentor):
        super().__init__(name, salary)
        self.mentor = mentor

    def learn(self):
        print(f"{self.name} is learning under {self.mentor}.")

# Generalization and Specialization
manager = Manager("Alice", 90000, "HR")
intern = Intern("Bob", 20000, "Alice")

manager.work()
manager.manage()

intern.work()
intern.learn()