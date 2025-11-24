import random

# create a sorted list
data = list(range(1, 100001))

# search a random target using binary search
target = random.randint(1, 100001)
class BinarySearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.data[mid] == target:
                return mid
            elif target > self.data[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
obj = BinarySearch(data)
print(f"Searching for {target} in the sorted list.")

result = obj.search(target)
if result != -1:
    print(f"Element {target} found at index {result}.") 


# search a random target using sequential search
class SequentialSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index in range(len(self.data)):
            if self.data[index] == target:
                return index
        return -1
    
obj_seq = SequentialSearch(data)
print(f"Searching for {target} in the list using sequential search.")

result_seq = obj_seq.search(target)
if result_seq != -1:
    print(f"Element {target} found at index {result_seq}.")