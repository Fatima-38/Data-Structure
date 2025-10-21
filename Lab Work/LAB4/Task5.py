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
     
        
#--- Quick tests for Task-5 ---
ls = LinearSearch([10, 30, 20, 50])
assert ls.find(20) == 2     # expected index
assert ls.find(99) == -1    # missing
print("Task-5: LinearSearch OK")