from collections import deque

class Passenger:
    def __init__(self, name, seat, dest):
        self.name = name
        self.seat = seat
        self.dest = dest
    def __repr__(self):
        return f"{self.name} (Seat {self.seat} -> {self.dest})"

# quick smoke-test
Passenger("Ayesha", "12A", "Lahore")
