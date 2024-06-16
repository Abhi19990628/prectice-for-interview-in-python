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
