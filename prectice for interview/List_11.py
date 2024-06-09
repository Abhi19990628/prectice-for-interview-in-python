# How do you implement a basic singly linked list in Python?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()



# How do you reverse a singly linked list in Python?

python
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
reversed_head = reverse_linked_list(head)


#What is a linked list, and how does it differ from an array?

#A linked list is a data structure where each element (node) contains a value and a reference (pointer) to the next node in the sequence. Unlike arrays, linked lists do not have contiguous memory allocation, which allows for efficient insertion and deletion of elements. However, accessing an element by index requires traversal from the head of the list, leading to O(n) time complexity for access.
