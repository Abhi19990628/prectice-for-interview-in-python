# 1. Implement a Stack using a List
# Question: Implement a stack using a list with the following operations: push, pop, peek, and is_empty.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1
print(stack.is_empty())  # Output: False
print(stack.size())  # Output: 1



# 2. Check for Balanced Parentheses
# Question: Write a function to check if a given string containing only parentheses is balanced.


def is_balanced(parentheses):
    stack = Stack()
    for char in parentheses:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Example usage:
print(is_balanced("()"))  # Output: True
print(is_balanced("(()"))  # Output: False
print(is_balanced("(())"))  # Output: True
print(is_balanced("())("))  # Output: False


