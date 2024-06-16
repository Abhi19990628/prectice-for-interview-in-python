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
