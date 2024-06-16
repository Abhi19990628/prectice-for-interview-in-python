# 1. Basic Syntax and Data Types
# Variables and Data Types: Integers, floats, strings, booleans.
# Comments: Use # for single-line comments and triple quotes """ """ for multi-line comments.
# Indentation: Python uses indentation to define the scope of loops, functions, and classes.

x = 10        # Integer
y = 3.14      # Float
name = "Alice" # String
is_active = True  # Boolean

# 2. Control Flow
# Conditional Statements: if, elif, else

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Arguments and Return Values:
def add(a, b=5):  # Default parameter
    return a + b

print(add(10, 20))
print(add(10))  # Uses default value for b


# Data Structures
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# Tuples:

# Ordered: The elements in a tuple have a defined order, and this order will not change.
# Immutable: Once a tuple is created, its elements cannot be changed, added, or removed.
# Heterogeneous: Tuples can contain elements of different data types.
# Indexable: Elements in a tuple can be accessed by their index, starting from 0


tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "apple", 3.5)

print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: banana
print(tuple3[2])  # Output: 3.5

# Dictionaries:
# Unordered: The elements (key-value pairs) in a dictionary are not stored in any particular order. Starting from Python 3.7, dictionaries maintain insertion order as an implementation detail, but it is not a feature to rely on for program correctness.
# Mutable: You can change, add, or remove key-value pairs after the dictionary has been created.
# Indexed by keys: Values are accessed using their keys, not by an index position.
# Unique keys: Each key in a dictionary must be unique. If you try to use a duplicate key, the previous value associated with that key will be overwritten.


dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(dict1["name"])  # Output: Alice
print(dict1["age"])   # Output: 25



# Set.



# Unordered: The elements in a set do not have a specific order.
# Unique elements: Each element in a set must be unique. If duplicates are added, they are automatically removed.
# Mutable: Sets can be changed after their creation; you can add or remove elements.
# Non-indexable: Elements in a set cannot be accessed by index, because sets do not maintain order.'

set1 = {1, 2, 3, 4}
set2 = {"apple", "banana", "cherry"}
empty_set = set()
set1.add(5)
print(set1)  # Output: {1, 2, 3, 4, 5}



# 6. File I/O
# Reading and Writing Files:


# File I/O (Input/Output) in Python involves reading from and writing to files. This is a fundamental operation that allows programs to persist data, read data from external sources, and interact with users through files.

# Reading Files
# Reading files means accessing the contents of a file and loading them into the program for processing.

# Open a file for reading
with open('example.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    print(content)

# Open a file for reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes trailing newline characters
Writing files means creating or modifying a file by outputting data to it.

Example:
python
Copy code
# Open a file for writing (this will create a new file or overwrite an existing file)
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a second line.\n')

# Open a file for appending (this will add to the end of the file without deleting existing content)
with open('example.txt', 'a') as file:
    file.write('This is an appended line.\n')



File I/O (Input/Output) in Python involves reading from and writing to files. This is a fundamental operation that allows programs to persist data, read data from external sources, and interact with users through files.

Reading Files
Reading files means accessing the contents of a file and loading them into the program for processing.

When opening a file, you specify the mode:

'r' - Read (default mode). Opens the file for reading.
'w' - Write. Opens the file for writing (creates a new file or truncates an existing file).
'a' - Append. Opens the file for appending at the end of the file.
'r+' - Read and Write. Opens the file for both reading and writing.
'b' - Binary mode. Used with any of the above modes to open the file in binary mode (e.g., 'rb', 'wb').




# Exception Handling in Python
# Exception handling in Python is the process of responding to the occurrence of exceptions—unexpected events or errors that can happen during the execution of a program. Exception handling helps to ensure that a program can handle errors gracefully and continue running or terminate properly.

# Basic Syntax of Exception Handling
# The basic syntax for handling exceptions in Python involves using the try, except, else, and finally blocks

def read_file(filename):
    """Reads the content of a file and returns it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")
        return None

def write_file(filename, content):
    """Writes the given content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error: An error occurred while writing to the file '{filename}'.")

# Example usage
file_content = read_file('example.txt')
if file_content is not None:
    print("File content:")
    print(file_content)

new_content = "This is some new content for the file."
write_file('example.txt', new_content)


# Classes and Objects in Python
# Classes and objects are fundamental concepts of object-oriented programming (OOP) in Python. They help in creating and organizing code in a way that models real-world entities and relationships.

# Definitions
# Class: A blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.
# Object: An instance of a class. It is a specific realization of the class with actual values and functionalities.
# Creating a Class
# To define a class in Python, use the class keyword followed by the class name and a colon. Class names are usually written in CamelCase.

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Creating an instance of the Dog class
my_dog = Dog("Buddy", 5)

# Accessing instance attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5

# Accessing class attribute
print(my_dog.species)  # Output: Canis familiaris

# Calling instance methods
print(my_dog.description())  # Output: Buddy is 5 years old
print(my_dog.speak("Woof!")) # Output: Buddy says Woof!



# Libraries and Frameworks
# Libraries and Frameworks in Software Development
# Libraries and frameworks are essential components in software development that provide pre-written functionality to facilitate common tasks. They help developers save time, enhance productivity, and ensure code reliability by leveraging reusable code and established patterns.

# Libraries
# A library in programming refers to a collection of precompiled routines or functions that can be used in your code to perform specific tasks without rewriting them from scratch. Libraries typically focus on specific tasks or domains and are designed to be reusable across different projects.

# Example: math Library in Python
# The math library in Python provides various mathematical functions, constants, and utilities for numerical computations.

import math

# Using functions from the math library
print(math.sqrt(16))     # Output: 4.0 (square root)
print(math.pi)           # Output: 3.141592653589793 (constant)
print(math.sin(math.pi)) # Output: 1.2246467991473532e-16 (sine of pi)






# Virtual Environments in Python




# A virtual environment in Python is a self-contained directory that contains a specific Python interpreter and any number of additional packages. Virtual environments allow you to isolate project dependencies and manage them separately from the system-wide Python interpreter and other projects.

# Definition
# Virtual environments are used to:

# Isolate Dependencies: Each project can have its own set of dependencies (libraries and packages), which may differ in version requirements from other projects.

# Avoid Dependency Conflicts: Different projects may require different versions of the same package. Virtual environments ensure that each project gets the version it needs without conflicts.

# Maintain Clean Development Environment: Virtual environments keep your system-wide Python environment clean and prevent accidental modifications or installations.

# Uses
# Development: Create a virtual environment for each project to manage dependencies and ensure reproducibility across different environments.

# Testing: Test your project in different Python environments or with different package versions without affecting other projects.

# Deployment: Deploy your project with its specific dependencies, ensuring compatibility and consistency across different deployment environments


# Creating a Virtual Environment:
pip install virtualenv
virtualenv name of your env for example (my_env)

# Activating the Virtual Environment:

# Navigate to the directory where your virtual environment is located. Then, depending on your Command Prompt shell (CMD or PowerShell):
cd my_env
myenv/scripts/./activate

# Deactivating the Virtual Environment:
# To deactivate the virtual environment and return to the system's global Python environment:

deactivate




# 12. Advanced Topics



# Decorators in Python
# Decorators are a powerful and advanced feature in Python that allow you to modify the behavior of functions or methods without changing their actual code. They provide a convenient syntax to wrap functions or methods with other functions, enabling you to add functionality, modify arguments, or perform actions before or after the original function call.

# Definition
# In Python, a decorator is a design pattern that allows you to dynamically alter the functionality of a function, method, or class without permanently modifying its code. Decorators are defined using the @decorator_name syntax before the function definition.

# Example
# Let's explore a simple example to illustrate how decorators work:

# Decorator function definition
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function definition with decorator
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()







Generators in Python


# Generators in Python are special functions that enable you to iterate over a sequence of items lazily, one at a time, instead of computing and storing all items at once like a regular function. They are used to create iterators, providing a more memory-efficient way to process large datasets or infinite sequences.

# Definition
# A generator in Python is defined using a function with one or more yield statements. When called, a generator function returns a generator object that can be iterated over using a for loop or by calling the next() function on it. Each time the yield statement is encountered, the generator function pauses its execution and returns the yielded value.

# Example
# Let's create a simple generator that generates squares of numbers up to a specified limit:


def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

# Using the generator
my_generator = square_generator(5)

# Iterating over the generator using a for loop
for num in my_generator:
    print(num)


# Generator Function (square_generator):

# square_generator is a generator function that uses a for loop to yield squares of numbers from 1 to n.
# Using the Generator:

# my_generator = square_generator(5) creates a generator object my_generator that yields squares of numbers up to 5.
# Iterating Over the Generator:

# The for loop iterates over my_generator, calling the generator function each time next() is called implicitly.
# Each iteration computes and yields the next square of the number.


Output:
1
4
9
16
25
