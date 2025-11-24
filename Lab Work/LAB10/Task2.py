# -------- Task 2: Implement binary search (OOP) --------

class BinarySearch:
    def __init__(self, data):
        self.data = sorted(data)

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
    
arr = [15, 8, 23, 42, 4, 33]
obj = BinarySearch(arr)

print(obj.search(23))
print(obj.search(15))
print(obj.search(8))
print(obj.search(42))
print(obj.search(4))
print(obj.search(33))


print(obj.search(99))   # Not found case
print(obj.search(12))   # Not found case