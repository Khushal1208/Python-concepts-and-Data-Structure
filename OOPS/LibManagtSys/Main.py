class User:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__role = ""
        self.__id = ""
        self.__dept = ""
        self.__email_id = ""

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_id(self, user_id):
        self.__id = user_id

    def get_id(self):
        return self.__id

    def set_dept(self, dept):
        self.__dept = dept

    def get_dept(self):
        return self.__dept

    def set_email_id(self, email_id):
        self.__email_id = email_id

    def get_email_id(self):
        return self.__email_id


class Student(User):
    def __init__(self):
        super().__init__()
        self.set_role("Student")


class Librarian(User):
    def __init__(self):
        super().__init__()
        self.set_role("Librarian")


class Library:
    def __init__(self):
         # below are all groups(dictionaries) of data about library number of books , issued books , students , staff members . 
        # it is like a database of library 
        self.books = {}
        self.issued_books = {}
        self.students = {}
        self.librarians = {}

    def add_student(self):
        student = Student()
        student.set_id(input("Enter student ID: "))
        student.set_username(input("Enter student username: "))
        student.set_dept(input("Enter student department: "))
        student.set_email_id(input("Enter student email: "))
        student.set_password(input("Enter student password: "))
        if student.get_id() in self.students:
            print("Students already exist!")
        else:
            self.students[student.get_id()] = student
            print(f"Student {student.get_username()} added successfully!")

        def view_students(self):
            print("List of Students:")
            for student_id, student in self.students.items():
                print(f"ID: {student_id}, Username: {student.get_username()}, Dept: {student.get_dept()}, Email: {student.get_email_id()}")
 

    def add_librarian(self):
        librarian = Librarian()
        librarian.set_id(input("Enter librarian ID: "))
        librarian.set_username(input("Enter librarian username: "))
        librarian.set_dept(input("Enter librarian department: "))
        librarian.set_email_id(input("Enter librarian email: "))
        librarian.set_password(input("Enter librarian password: "))
        if librarian.get_id() in self.librarians:
            print("Students already exist!")
        else:
            self.librarians[librarian.get_id()] = librarian
            print(f"Librarian {librarian.get_username()} added successfully!")
    

    
