class Employee:
    emp_no = 0
    emp_name = None
    emp_desig = None
    emp_salary = 0

    details = {}

    def add(self ,emp_no , emp_name , emp_desig , emp_salary):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_desig = emp_desig
        self.emp_salary = emp_salary
    
    def get_emp_details(self,emp_no):
        print()

emp1 = Employee()

emp_no = int(input("Enter employeeID: "))
emp_name = input("Enter employee name: ")
emp_desig = input("Enter Designation: ")
emp_salary = int(input("Enter salary: ")) 

emp1.add(emp_no,emp_name,emp_name,emp_desig,emp_salary)

emp1.get_emp_details(emp_no)
