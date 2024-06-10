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


# 3. Evaluate a Postfix Expression
# Question: Evaluate a given postfix expression.

def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(int(operand1 / operand2))  # integer division
    return stack.pop()


#4. Implement a Stack with O(1) Time Complexity for get_min
# Question: Implement a stack that supports push, pop, and get_min operations, all in O(1) time complexity.


# Example usage:
# print(evaluate_postfix("231*+9-"))  # Output: -4

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]

# Example usage:
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.get_min())  # Output: 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.get_min())  # Output: 1
min_stack.pop()
print(min_stack.get_min())  # Output: 2


