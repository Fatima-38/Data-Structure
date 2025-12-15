class SelectionSortCounter:
    def __init__(self, arr):
        self.arr = arr
        self.comparisons = 0  # TODO: keep track of comparisons

    def sort(self):
        n = len(self.arr)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                # We are comparing arr[j] with arr[min_index]
                self.comparisons += 1  # count the comparison

                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr

# Demo
data = [12, 7, 3, 14, 9]
s = SelectionSortCounter(data)
print("Sorted:", s.sort())
print("Total comparisons:", s.comparisons)