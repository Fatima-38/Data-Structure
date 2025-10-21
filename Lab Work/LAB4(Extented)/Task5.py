# Name: Fatima Javaid
# Roll no: 2024-csr-010
# Section: B

# Task-5: LinearSearch

class LinearSearch:
    def __init__(self, data):
        """Store a copy of the data to avoid external mutation side-effects."""
        self.data = list(data)

    def find(self, target):
        """Return index of first occurrence of target; -1 if not found."""
        for i, x in enumerate(self.data):  # scan left to right
            if x == target:                # match?
                return i                   # return index of first match
        return -1                          # not found
     
        
# --- Quick tests for Task-5 with printing ---

ls = LinearSearch([10, 30, 20, 50])

# Search for an existing element
target1 = 20
res1 = ls.find(target1)
print(f"Searching for {target1} → Index: {res1}")    # expected 2

# Search for a missing element
target2 = 99
res2 = ls.find(target2)
print(f"Searching for {target2} → Index: {res2}")    # expected -1

print("Task-5: LinearSearch tests done")