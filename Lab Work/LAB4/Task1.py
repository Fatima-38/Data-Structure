# Name: Fatima Javaid
# Roll no: 2024-csr-010
# Section: B

# Task-1: Stack Class (array-backed)

class Stack:
    def __init__(self):
        """Initialize internal storage for the stack using a Python list.
        Top of the stack will be at the *end* of the list for O(1) amortized push and pop.
        """
        self._data = []  # internal list to hold items

    def push(self, item):
        """Place a new item on the top of the stack."""
        self._data.append(item)  # append adds at end (the top)

    def pop(self):
        """Remove and return the top item from the stack.
        Raises:
            IndexError: if the stack is empty (underflow).
        """
        if self.is_empty():  # guard against removing from empty stack
            raise IndexError("Stack underflow")
        return self._data.pop()  # remove and return last element

    def peek(self):
        """Return the top item without removing it.
        Raises:
            IndexError: if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Empty stack")
        return self._data[-1]  # last element is the top

    def is_empty(self):
        """Return True if the stack has no elements; otherwise False."""
        return len(self._data) == 0

    def size(self):
        """Return the current number of elements in the stack."""
        return len(self._data)
    
    
# --- Quick tests for Task-1 ---
s = Stack()                  # create a stack
assert s.is_empty()         # new stack should be empty
s.push(10)                  # push first element
s.push(20)                  # push second element
assert s.peek() == 20       # top should be 20
assert s.pop() == 20        # pop returns 20
assert s.pop() == 10        # then 10
try:
    s.pop()                 # popping now should fail
    assert False, "Expected IndexError for underflow"
except IndexError:
    pass                   # correct path

print("Task-1: Stack OK")