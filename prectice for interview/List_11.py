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

# What are the different types of linked lists, and how do you implement a doubly linked list in Python?

python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print_list()

# How would you detect a cycle in a linked list?


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head  # Creating a cycle for testing
print(has_cycle(head))  # Should return True

# How do you find the middle element of a linked list in Python?

def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(find_middle(head))  # Should return 3

# How can you merge two sorted linked lists in Python?
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

# Example usage
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)
merged_head = merge_sorted_lists(l1, l2)


# How would you remove duplicates from an unsorted linked list in Python?

def remove_duplicates(head):
    if not head:
        return head
    current = head
    seen = set([current.data])
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return head

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
remove_duplicates(head)
