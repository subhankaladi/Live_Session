# Question No: 1
# Correct syntax to define a function:
# Correct Answer: C) def myFunc()

def myFunc():
    print("Hello, this is myFunc!")

myFunc()  # Output: Hello, this is myFunc!


# Question No: 2
# 'return' is used to send a value back from a function
# Correct Answer: B) return

def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5


# Question No: 3
# print() is a built-in function
# Correct Answer: C) print()

print("This is a built-in function!")  # Output: This is a built-in function!


# Question No: 4
# len() returns the length of an object (like list or string)
# Correct Answer: C) The length of an object like list or string

my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4


# Question No: 5
# range() creates a sequence of numbers
# Correct Answer: B) To create a list of numbers in a sequence

for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4


# Question No: 6
# Functions created by users are called user-defined functions
# Correct Answer: C) User defined functions

def greet():
    print("Hello User!")

greet()  # Output: Hello User!


# Question No: 7
# If you call a function without required parameters, it gives an error
# Correct Answer: B) Gives an error

def greet(name):
    print(f"Hello {name}")

# greet()  # Uncommenting this will cause an error: missing 1 required positional argument


# Question No: 8
# Default return type without return statement is None
# Correct Answer: C) None

def hello():
    print("Hi")

result = hello()  # Output: Hi
print(result)     # Output: None


# Question No: 9
# A default parameter means a parameter with a predefined value
# Correct Answer: B) A parameter with a predefined value

def greet(name="Guest"):
    print(f"Hello {name}")

greet()           # Output: Hello Guest
greet("Subhan")   # Output: Hello Subhan


# Question No: 10
# Function with default parameter
# Correct Answer: B) def func(a, b=10):

def func(a, b=10):
    print(a + b)

func(5)  # Output: 15


# Question No: 11
# Function that returns the square of a number
# Correct Answer: A) def square(x): return x ** 2

def square(x):
    return x ** 2

print(square(4))  # Output: 16


# Question No: 12
# Correct lambda function for multiplying two numbers
# Correct Answer: A) lambda x, y: x * y

multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12


# Question No: 13
# loop() is not a valid built-in function
# Correct Answer: D) loop()

# type(), len(), range() are valid built-in functions.


# Question No: 14
# Any data type can be passed as a parameter to a function
# Correct Answer: C) Any data type

def show(x):
    print(x)

show(5)       # Integer
show("Hello") # String
show([1,2,3]) # List


# Question No: 15
# Function with no return statement returns None
# Correct Answer: C) None

def greet():
    print("Hello")

result = greet()
print(result)  # Output: Hello \n None


# Question No: 16
# Correct function call
# Correct Answer: C) greet("Subhan")

def greet(name):
    print(f"Hello {name}")

greet("Subhan")  # Output: Hello Subhan


# Question No: 17
# WAF stands for Write a Function
# Correct Answer: B) Write a Function


# Question No: 18
# len() of [1,2,3,4] is 4
# Correct Answer: B) 4

print(len([1,2,3,4]))  # Output: 4


# Question No: 19
# Function with default parameters
# Correct Answer: A) def sum(a, b=5):

def sum(a, b=5):
    return a + b

print(sum(3))  # Output: 8


# Question No: 20
# 'def' keyword is used to define a function
# Correct Answer: C) def

def myFunc():
    pass


# Question No: 21
# 'return' exits the function and sends a value back
# Correct Answer: D) Exits the function and optionally sends a value back

def add(a, b):
    return a + b

result = add(5, 5)
print(result)  # Output: 10


# Question No: 22
# Functions can take input and return output
# Correct Answer: C) Functions can take input and return output


# Question No: 23
# Correct syntax to call a function with keyword arguments
# Correct Answer: B) myfunc(a=10, b=20)

def myfunc(a, b):
    print(a, b)

myfunc(a=10, b=20)  # Output: 10 20


# Question No: 24
# To print all elements of a list in one line
# Correct Answer: D) Both A and C

my_list = [1, 2, 3, 4]

print(my_list)  # Method A

for i in my_list:  # Method C
    print(i, end=" ")  # Output: 1 2 3 4


# Question No: 25
# Anonymous function to subtract two numbers
# Correct Answer: A) lambda x, y: x - y

subtract = lambda x, y: x - y
print(subtract(10, 3))  # Output: 7
