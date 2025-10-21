# =========================
# Deque (Teaching Version)
# =========================
# Implementation uses a Python list to keep concepts visible.
# Note: insert/remove at index 0 are O(n) due to shifting.
# For production, use collections.deque (see earlier section)

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
# ---------- Mini demo (you can run this cell to preview behavior) ----------

if __name__ == '__main__':
    dq = Deque()
    show_state('Step 0 -> created empty deque', dq)
    
    dq.add_rear('Ali')
    show_state("After add_rear('Ali')", dq)
    
    dq.add_front('Sara')
    dq.add_rear('Hamza')
    show_state('After 2 inserts (front+rear)', dq)
    
    out1 = dq.remove_rear()
    out2 = dq.remove_front()
    print('Removed (rear):', out1)
    print('Removed (front):', out2)
    show_state('After 2 removals', dq)
