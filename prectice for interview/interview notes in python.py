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
