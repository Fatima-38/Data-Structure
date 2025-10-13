# Task 2: Teaching Queue (list-backed)

# Teaching Queue (list-backed) with step-by-step outputs
class Queue:
   def __init__(self):
     self.items = [] # internal list to hold elements
     print("Init ->", self.items)

   def is_empty(self):
     return len(self.items) == 0 # empty if length == 0

   def enqueue(self, x):
     self.items.append(x) # append at end (rear)
     print(f"enqueue({x}) ->", self.items)
 
   def dequeue(self):
     if self.is_empty():
       print("dequeue() -> Underflow (None) |", self.items)
       return None # signal underflow
     val = self.items.pop(0) # remove & return element at index 0 (fr
     print(f"dequeue() -> {val} |", self.items)
     return val
   
   def front(self):
     if self.is_empty():
       print("front() -> None |", self.items)
       return None
     print("front() ->", self.items[0], "|", self.items)
     return self.items[0] # peek front without removing

# quick test with step-by-step tracing
q = Queue()
q.enqueue(10)
q.enqueue(20)
_ = q.dequeue() # expect 10
_ = q.front() # expect 20
print('is_empty ->', q.is_empty()) # expect False