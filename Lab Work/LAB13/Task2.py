class InsertionSortCounter:
    def __init__(self, arr):
        self.arr = arr
        self.shifts = 0  # TODO: count shifts (moves)

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1

            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                self.shifts += 1  # count the shift
                j -= 1

            self.arr[j + 1] = key

        return self.arr

# Demo
data = [8, 2, 5, 3]
ins = InsertionSortCounter(data)
print("Sorted:", ins.sort())
print("Total shifts:", ins.shifts)