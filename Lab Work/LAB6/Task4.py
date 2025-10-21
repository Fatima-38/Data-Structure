# ======================================
# Problem 2: Palindrome Checker (Deque)
# ======================================
# We can use the Deque class; for performance, collections.deque would also be great.

class Deque:
    def __init__(self):
        # Internal storage for items; left side = 'front', right side = 'rear'
        self.items = []

    def is_empty(self):
        # True if no elements are stored
        return len(self.items) == 0

    def add_front(self, item):
        # Insert at front (index 0). O(n) because elements shift right.
        self.items.insert(0, item)

    def add_rear(self, item):
        # Append at rear (end of list). Amortized O(1)
        self.items.append(item)

    def remove_front (self):
        # Remove and return front item (index 0) if not empty; else None
        if self.is_empty():
            return None          #Underflow guard
        return self.items.pop(0)  # O(1)

    def remove_rear(self):
        # Remove and return rear item (last element) if not empty; else None
        if self.is_empty():
            return None         # Underflow guard
        return self.items.pop() # O(1)

    def size(self):
        # Current number of elements
        return len(self.items)

def show_state(step_label, dq_obj):
    """
    Prints a labeled snapshot of the deque's content and size.
    This is a helper function to visualize the current state of a Deque object.
    """

    # Print the step description passed by the caller
    # Example: "Step 1 → after adding an element"
    print(step_label)
    
    # Print the current list of items stored inside the deque object
    # dq_obj.items refers to the internal Python list holding deque elements
    print(' items:', dq_obj.items)
    
    
    # Print the size of the deque (number of elements)
    # dq_obj.size() calls the size() method of the Deque class
    print(' size :', dq_obj.size())

    # Print a line of 40 dashes for readability / visual separation
    print('-' * 40)



def is_palindrome(text):
    """
    Returns True if 'text' is a palindrome (ignoring spaces and case),
    using a Deque to compare characters from both ends.
    """

    # 1)Normalize input: lowercase + keep only alphanumeric characters
    normalized = []
    for ch in text:
        if ch.isalnum():             # ignore spaces/punctuations 
            normalized.append(ch.lower())

    # 2) Load into deque (front=left, rear=right)
    dq = Deque()
    for ch in normalized:
        dq.add_rear(ch)              # push characters at the rear (end)

    # 3) Compare front vs rear until deque has 0 or 1 element left
    while dq.size() > 1:
        left = dq.remove_front()    # front character
        right = dq.remove_rear()    # rear character
        if left != right:
            return False            # mismatch -> not a palindrome 
            
    return True                 # all matches -> palindrome
    

# ---------- Quick tests ----------
tests = [
    'Racecar',
    'Never odd or even',
    'Was it a car or a cat I saw?',
    'Hello',
    'A man, a plan, a canal: Panama!'
]
for s in tests:
    print(f"{s!r} ->", is_palindrome(s))