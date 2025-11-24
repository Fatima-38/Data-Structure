# -------- Task 1: Implementation sequential search (OOP) ---------

class SequentialSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index in range(len(self.data)):
            if self.data[index] == target:
                return index
        return -1
    
arr = [15, 8, 23, 42, 4, 33]
obj = SequentialSearch(arr)

print(obj.search(23))
print(obj.search(4))
print(obj.search(15))      # element at index 0
print(obj.search(33))      # element at last index
print(obj.search(42))
print(obj.search(8))


print(obj.search(99))     # Not found case
print(obj.search(12))     # Not found case