from collections import deque

dq = deque()
dq.append('Ali')          #add to rear
dq.append('Sara')         #add to front
dq.append('Hamza')        #add to rear

print('Deque now:', list(dq))    #['Sara', 'Ali', 'Hamza']

print('Removed from rear:', dq.pop())        #'Hamza'
print('Removed from front:', dq.popleft())   #'Sara'
print('Deque after removals:', list(dq))     #['Ali']