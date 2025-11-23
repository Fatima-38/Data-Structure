from collections import deque

class Passenger:
    def __init__(self, name, seat, dest):
        self.name = name
        self.seat = seat
        self.dest = dest
    def __repr__(self):
        return f"{self.name} (Seat {self.seat} -> {self.dest})"


class TicketSystem:
    def __init__(self):
        self.waiting_queue = deque()
        self.served_passengers = []

    def add_passenger(self, name, seat, dest):
        self.waiting_queue.append(Passenger(name, seat, dest))
        return f"Added {name} to the waiting queue."

    def serve_passenger(self):
        if not self.waiting_queue:
                return "No passengers waiting."
        passenger = self.waiting_queue.popleft()   # FIFO
        self.served_passengers.append(passenger)   # keep history
        return f"Served passenger: {passenger}"

    def show_waiting(self):
        if not self.waiting_queue:
            return "Queue is empty."
        return "Waiting Queue:\n" + "\n".join("  -> " + str(p) for p in list(self.waiting_queue))

    def show_served(self):
        if not self.served_passengers:
            return "Served History: (empty)"
        return "Served History:\n" + "\n".join("  " + str(p) for p in self.served_passengers)


# quick scenario
sys_demo = TicketSystem()
print(sys_demo.add_passenger("Ali", "1", "Pattoki"))
print(sys_demo.add_passenger("Sara", "2B", "Lahore"))
print(sys_demo.show_waiting())
print(sys_demo.serve_passenger())
print(sys_demo.show_waiting())
print(sys_demo.show_served())