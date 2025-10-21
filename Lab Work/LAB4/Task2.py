# Name: Fatima Javaid
# Roll no: 2024-csr-010
# Section: B

# Task-2: BracketChecker (Balanced Parentheses)

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

class BracketChecker:
    def __init__(self):
        """Create a new bracket checker that uses an internal Stack instance."""
        self._stack = Stack()  # composition: use a Stack inside

    def _is_open(self, ch):
        """Return True if character is an opening bracket."""
        return ch in "([{"

    def _matches(self, open_br, close_br):
        """Return True if open_br correctly matches close_br."""
        pairs = {')': '(', ']': '[', '}': '{'}  # mapping closing -> opening
        return pairs.get(close_br) == open_br

    def is_balanced(self, expr: str) -> bool:
        """Return True if expr has balanced (), [], {}; False otherwise.
        Ignores non-bracket characters.
        """
        self._stack = Stack()  # reset stack per call
        for ch in expr:
            if self._is_open(ch):
                self._stack.push(ch)  # push openings
            elif ch in ")]}":
                if self._stack.is_empty():  # unmatched closing bracket
                    return False
                top = self._stack.pop()  # get last opening
                if not self._matches(top, ch):  # mismatch pair
                    return False
            # ignore other characters
        return self._stack.is_empty()  # balanced only if nothing left


# --- Quick tests for Task-2 ---
bc = BracketChecker()
assert bc.is_balanced("{[()]}") is True     # perfectly nested
assert bc.is_balanced("([)]") is False      # crossing pairs
assert bc.is_balanced("(((())))") is True   # deep nesting
assert bc.is_balanced(")(") is False        # close before open
print("Task-2: BracketChecker OK")