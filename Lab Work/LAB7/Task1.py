from collections import deque

class BankQueue:
    def __init__(self):
        # Internal queue storage using deque for O(1) append and popleft
        self.queue = deque()

    def arrive(self, customer):
        """A new customer arrives at the rear of the queue."""
        self.queue.append(customer)
        print(f"{customer} joined the line.")

    def serve(self):
        """Serve the next customer (front of the queue)."""
        if self.queue:
            served = self.queue.popleft()
            print(f"{served} is being served.")
            return served
        else:
            print("No customers left!")
            return None

    def show(self):
        """Display the current state of the queue as a list."""
        print("Current Queue:", list(self.queue))


# --- Demo ---
bank = BankQueue()
bank.arrive("Ali")
bank.arrive("Sara")
bank.arrive("Hamza")

bank.show()
bank.serve()
bank.show()


# --- Additional Test Cases ---
bank.arrive("Asifa")
bank.arrive("Ahmad")

bank.show()

bank.serve()
bank.serve()

print("Customers left:", len(bank.queue))