# Task 1: FIFO Warm‑Up (List)

# Show results after each step for the user's FIFO warm-up

q = [] # start empty
print("Start:", q)

q.append('A') # enqueue A
print("After enqueue A:", q)

q.append('B') # enqueue B
print("After enqueue B:", q)

q.append('C') # enqueue C
print("After enqueue C:", q)

out1 = q.pop(0) # dequeue -> 'A'
print("After dequeue ->", out1, "| Queue:", q)

out2 = q.pop(0) # dequeue -> 'B'
print("After dequeue ->", out2, "| Queue:", q)

out3 = q.pop(0) # dequeue -> 'C'
print("After dequeue ->", out3, "| Queue:", q)

print('Removed order:', out1, out2, out3)