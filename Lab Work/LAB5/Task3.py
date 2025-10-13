# Task 3: Fixed-Size Array Queue — See the Waste

# ---- Fixed-size Array Queue ----

class ArrayQueue:
   def __init__(self, size):
     self.size = size # total capacity
     self.a = [None] * size # fixed-size storage
     self.front = 0 # index of current front
     self.rear = -1 # index of last filled position
     self.count = 0 # number of current elements
 
   def is_empty(self):
     return self.count == 0
 
   def is_full(self):
    return self.count == self.size

   def enqueue(self, x):
     if self.is_full():
       print("Overflow")
       return False
     self.rear += 1 # move right
     self.a[self.rear] = x # place new element
     self.count += 1
     return True
 
   def dequeue(self):
     if self.is_empty():
       print("Underflow")
       return None
     val = self.a[self.front] # read front
     self.front += 1 # move right
     self.count -= 1
     return val
   
   def front_val(self):
     if self.is_empty():
       return None
     return self.a[self.front]

# demo: show wasteb
aq = ArrayQueue(5)
aq.enqueue(10); aq.enqueue(20); aq.enqueue(30)
print('dequeue ->', aq.dequeue()) # remove 10
print('dequeue ->', aq.dequeue()) # remove 20
print('front ->', aq.front_val()) # expect 30
print('state ->', 'count=', aq.count, 'front=', aq.front, 'rear=', aq.rear)
print('active ->', aq.a[aq.front:aq.rear+1]) # logical active window