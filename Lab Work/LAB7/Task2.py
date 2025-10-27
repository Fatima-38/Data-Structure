import heapq

class PriorityQueue:
    def __init__(self):
        # Each entry is a tuple (priority, task)
        self.queue = []

    def add_task(self, priority, task):
        """Insert a task with a numeric priority (smaller = higher priority)."""
        heapq.heappush(self.queue, (priority, task))
        print(f"Added '{task}' with priority {priority}")

    def serve_task(self):
        """Pop the highest-priority task (lowest number)."""
        if self.queue:
            priority, task = heapq.heappop(self.queue)
            print(f"Serving '{task}' (priority {priority})")
            return task
        else:
            print("No tasks left!")
            return None

    def show(self):
        """Display the raw heap (priority, task) pairs."""
        print("Current tasks:", self.queue)


# --- Demo ---
pq = PriorityQueue()
pq.add_task(3, "Normal Customer")
pq.add_task(1, "VIP Customer")
pq.add_task(2, "Senior Citizen")

pq.show()
pq.serve_task()
pq.show()


# --- Additional Test Cases ---
pq.add_task(5, "Regular Customer")
pq.add_task(0, "Emergency Case")
pq.add_task(4, "Online Appointment")

pq.show()

while pq.queue:
    pq.serve_task()

pq.show()