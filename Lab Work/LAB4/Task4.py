# Name: Fatima Javaid
# Roll no: 2024-csr-010
# Section: B

# Task-4: PostfixEvaluator

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


class PostfixEvaluator:
    def __init__(self):
        """Initialize with an internal stack of numbers."""
        self._stack = Stack()

    def _apply(self, op, b, a):
        """Apply binary operator 'op' to operands a (left) and b (right)."""
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        if op == '^': return a ** b
        raise ValueError(f"Unknown operator {op}")

    def evaluate(self, postfix: str) -> float:
        """Evaluate a postfix string containing single-digit operands."""
        self._stack = Stack()  # reset per call
        for ch in postfix.replace(" ", ""):
            if ch.isdigit():
                self._stack.push(float(ch))  # push numeric value
            elif ch in "+-*/^":
                if self._stack.size() < 2:
                    raise ValueError("Malformed expression: insufficient operands")
                b = self._stack.pop()  # right operand
                a = self._stack.pop()  # left operand
                self._stack.push(self._apply(ch, b, a))
            else:
                raise ValueError(f"Bad token {ch}")  # reject unknown tokens
        if self._stack.size() != 1:
            raise ValueError("Malformed expression: leftover values")
        return self._stack.pop()  # final result
        

# --- Quick tests for Task-4 ---
ev = PostfixEvaluator()
assert ev.evaluate("432+*") == 20.0        # (4*(3+2)) = 20
assert ev.evaluate("23+5*") == 25.0        # (2+3)*5 = 25
assert ev.evaluate("82/3-") == 1.0         # (8/2)-3 = 1
print("Task-4: PostfixEvaluator OK")