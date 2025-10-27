from collections import deque
import heapq

class MixedServiceDesk:
    def __init__(self):
        self.normal = deque()   # FIFO for '-' customers
        self.urgent = []        # heap for '+' customers as (priority_number, name)

    def arrive(self, name, sign='-'):
        """Customer arrives. '+' -> urgent heap, '-' -> normal deque."""
        if sign == '+':
            heapq.heappush(self.urgent, (1, name))
            print(f"{name} arrived as URGENT (+).")
        else:
            self.normal.append(name)
            print(f"{name} arrived as NORMAL (-).")

    def serve(self):
        """Serve urgent (+) if present, else serve from normal queue."""
        if self.urgent:
            _, name = heapq.heappop(self.urgent)
            print(f"Serving URGENT (+): {name}")
            return name, '+'
        elif self.normal:
            name = self.normal.popleft()
            print(f"Serving NORMAL (-): {name}")
            return name, '-'
        else:
            print("No customers to serve!")
            return None
        
    def show(self):
        print("Urgent (+) heap:", self.urgent)
        print("Normal (-) queue:", list(self.normal))


# ---Demo ---
desk = MixedServiceDesk()
desk.arrive("Ali", "-")
desk.arrive("Sara", "-")
desk.arrive("Hamza", "+")
desk.arrive("Noor", "-")
desk.arrive("Zoya", "+")

desk.show()
desk.serve()   #serves urgent first
desk.serve()
desk.show()


# --- Additional Test Cases ---
desk.arrive("Tariq", "-")
desk.arrive("Maya", "+")
desk.arrive("Bilal", "-")
desk.arrive("Iqra", "+")
desk.arrive("Omar", "-")

desk.show()

service_order = []
while True:
    served = desk.serve()
    if not served:
        break
    service_order.append(served)

print("""
Why this hybrid approach is practical:
Banks and hospitals often face both regular and emergency cases.
A mixed system ensures that urgent ('+') cases get served immediately
while normal ('-') customers are still handled fairly in order (FIFO).
""")