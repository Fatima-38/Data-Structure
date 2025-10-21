# Name: Fatima Javaid
# Roll no: 2024-csr-010
# Section: B

# Task-3: Infix→Postfix Converter

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


class InfixToPostfix:
    def __init__(self):
        """Initialize precedence and the internal operator stack."""
        self._prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # precedence map
        self._right_assoc = {'^'}                             # right-associative
        self._stack = Stack()                                   # operator stack

    def _is_operand(self, ch):
        """Return True if ch is an operand (letter or digit)."""
        return ch.isalnum()

    def convert(self, infix: str) -> str:
        """Convert an infix expression (single-char tokens) to postfix (RPN)."""
        out = []               # output token list
        self._stack = Stack()  # reset operator stack

        # remove spaces so we can scan char by char
        for ch in infix.replace(" ", ""):
            if self._is_operand(ch):
                out.append(ch)  # operands go straight to output
            elif ch == '(':
                self._stack.push(ch)  # push opening parenthesis
            elif ch == ')':
                # pop operators until '(' is found
                while not self._stack.is_empty() and self._stack.peek() != '(':
                    out.append(self._stack.pop())
                if self._stack.is_empty():
                    raise ValueError("Mismatched parentheses")  # no matching '('
                self._stack.pop()  # discard '('
            else:
                # operator case; pop while stack top has higher precedence
                # or same precedence for left-associative operators
                while (not self._stack.is_empty() 
                       and self._stack.peek() != '(' 
                       and (self._prec[self._stack.peek()] > self._prec[ch]
                            or (self._prec[self._stack.peek()] == self._prec[ch] 
                                and ch not in self._right_assoc))):
                    out.append(self._stack.pop())
                self._stack.push(ch)  # finally push current operator

        # flush remaining operators
        while not self._stack.is_empty():
            top = self._stack.pop()
            if top == '(':
                raise ValueError("Mismatched parentheses")  # stray '('
            out.append(top)

        return "".join(out)  # join tokens to make postfix string


# --- Quick tests for Task-3 with printing ---

conv = InfixToPostfix()

expr1 = "A+B*C"
result1 = conv.convert(expr1)
print(f"{expr1} → {result1}")

expr2 = "(A+B)*C"
result2 = conv.convert(expr2)
print(f"{expr2} → {result2}")

expr3 = "A^B^C"
result3 = conv.convert(expr3)
print(f"{expr3} → {result3}")

expr4 = "A*(B+C*D)"
result4 = conv.convert(expr4)
print(f"{expr4} → {result4}")

print("Task-3: InfixToPostfix tests done")