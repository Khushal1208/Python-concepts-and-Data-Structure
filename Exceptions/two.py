a = int(input())
b = int(input())
try:
    c = a / b
    print(c)
except ZeroDivisionError as ze:
    print("Denomination should not be zero")
except TypeError as te:
    print("You have to provide only integer values")

try: 
    li = [1, 2, 3]
    result = li[5]
except IndexError as ie:
    print("Index is not reachable")

try:
    d = {"name": "Khushal", "roll": 20}
    result = d["subject"]
except KeyError as ke:
    print("Mapping key not found")

try:
    file = open("example.txt", 'r')
except FileNotFoundError as fnfe:
    print("File not found")

# Example of handling ImportError and AttributeError
try:
    # You can add an import statement here that causes ImportError if the module does not exist
    import nonexistentmodule
except ImportError as ie:
    print("Importing module which is absent")

# Example of handling AttributeError
try:
    x = 5
    result = x.non_existent_method()  # This will raise an AttributeError
except AttributeError as ae:
    print("Attribute error")

try: 
    a = [0] * (10**20)
    print(a)
except OverflowError as ofe:
    print("Result too large to be represented")

try: 
    # Uncomment to raise MemoryError by allocating too much memory
    a = [0] * (10**9)
    print(a)
except MemoryError as me:
    print("Out of memory")

try:
    value = int('string')  # This will raise a ValueError
except ValueError as ve:
    print("Inappropriate argument value (of correct type)")
