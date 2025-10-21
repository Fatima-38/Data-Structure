# ================================
# Problem 1: Doorway Traffic Sim
# ================================
# We will use the Deque class defined earlier (teaching version).


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



def doorway_simulation():
    dq = Deque()  # Start with an empty deque (front=left, rear=right)
    show_state('Start -> Empty doorway line', dq)

    # Step 1: normal students arrive at the rear (they join the end of the line)
    dq.add_rear('Student-1')
    dq.add_rear('Student-2')
    dq.add_rear('Student-3')
    show_state('After Step 1 -> 3 normal arrivals at REAR', dq)

    # Step 2: a VIP arrives and gets access at the FRONT
    dq.add_front('VIP-1')
    show_state('After Step 2 -> VIP-1 enters at FRONT', dq)

    # Step 3: emergency exit at the FRONT (e.g., closest to the door leaves)
    left_front = dq.remove_front() # likely removes VIP-1
    print('Emergency exit (FRONT):', left_front)
    show_state('After Step 3 -> one exit from FRONT', dq)
    
    # Step 4: more arrivals (rear) and a second VIP (front)
    dq.add_rear('Student-4')
    dq.add_rear('Student-5')
    dq.add_front('VIP-2')
    show_state('After Step 4 -> two more normals (REAR) + VIP-2 (FRONT)', dq)
    
    # Step 5: one person exits from REAR (last to join leaves)
    left_rear = dq.remove_rear()
    print('Exit (REAR):', left_rear)
    show_state('After Step 5 -> one exit from REAR', dq)
    
    # Step 6: final report
    print('Final remaining people:', dq.items)
    print('Final size:', dq.size())
    
# Run the simulation
doorway_simulation()