# Task: Circular Queue — Wrap‑Around with %

# ---- Circular Queue with modulo wrap-around ----

class CircularQueue:
  def __init__(self, size):
    self.size = size
    self.a = [None] * size
    self.front = 0
    self.rear = -1
    self.count = 0
 
  def is_empty(self):
    return self.count == 0
 
  def is_full(self):
    return self.count == self.size
 
  def enqueue(self, x):
    if self.is_full():
      print("Overflow")
      return False
    self.rear = (self.rear + 1) % self.size
    self.a[self.rear] = x
    self.count += 1
    return True
 
  def dequeue(self):
    if self.is_empty():
      print("Underflow")
      return None
    val = self.a[self.front]
    self.front = (self.front + 1) % self.size
    self.count -= 1
    return val
  
  def front_val(self):
    if self.is_empty():
      return None
    return self.a[self.front]
 
  def to_list(self):
    # return logical order of elements from front, length = count
    res = []
    idx = self.front
    for _ in range(self.count):
      res.append(self.a[idx])
      idx = (idx + 1) % self.size
      return res
    
# demo: wrap-around behavior In [9]:
cq = CircularQueue(5)
for x in [10, 20, 30, 40]:
  cq.enqueue(x)
print('start ->', cq.to_list()) # [10,20,30,40]

print('dequeue ->', cq.dequeue()) # remove 10
print('dequeue ->', cq.dequeue()) # remove 20
print('mid ->', cq.to_list()) # [30,40]

cq.enqueue(50); cq.enqueue(60) # should wrap when needed
print('after ->', cq.to_list()) # [30,40,50,60]
print('front ->', cq.front_val())
print('state ->', 'front=', cq.front, 'rear=', cq.rear, 'count=', cq.count)