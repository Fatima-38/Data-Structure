import heapq

class SignPriorityQueue:
    def __init__(self):
        # Internal min_heap storing tuples (priority_number, task)
        self.queue = []

    def add_task(self, task, sign):
        """Add a task where sign is '+' (urgent) or '-' (normal)."""
        priority = 1 if sign == '+' else 2
        heapq.heappush(self.queue, (priority, task))
        print(f"Added task '{task}' with sign '{sign}' (mapped priority={priority})")

    def serve_task(self):
        """Serve the next task based on sign-derived priority."""
        if self.queue:
            priority, task = heapq.heappop(self.queue)
            sign = '+' if priority == 1 else '-'
            print(f"Serving '{task}' with sign '{sign}' (mapped priority={priority})")

    def serve_task(self):
        """Serve the next task based on sign-derived priority."""
        if self.queue:
            priority, task = heapq.heappop(self.queue)
            sign = '+' if priority == 1 else '-'
            print(f"Serving '{task}' (priority sign {sign})")
            return task, sign
        else:
            print("No tasks left!")
            return None

    def show(self):
        """Display the heap state."""
        print("Queue Status:", self.queue)


# --- Demo ---
spq = SignPriorityQueue()
spq.add_task("VIP Client", "+")
spq.add_task("Normal Client", "-")
spq.add_task("Emergency Case", "+")
spq.add_task("Student Inquiry", "-")

spq.show()
spq.serve_task()
spq.show()


# --- Additional Test Cases ---
while True:
    action = input("Enter 'add' to add a task, 'serve' to serve a task, 'quit' to exit: ").strip().lower()
    
    if action == 'add':
        task = input("Enter task name: ").strip()
        sign = input("Enter sign (+ or -): ").strip()
        if sign not in ['+', '-']:
            print("Invalid sign! Please enter '+' or '-'.")
            continue
        spq.add_task(task, sign)
        spq.show()
    
    elif action == 'serve':
        spq.serve_task()
        spq.show()
    
    elif action == 'quit':
        print("Exiting the code.")
        break
    
    else:
        print("Invalid action! Please enter 'add', 'serve', or 'quit'.")