class HeapSortCounter:
    def __init__(self):
        self.comparisons = 0  # count comparisons in heapify

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1  # compare arr[left] with arr[largest]
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1  # compare arr[right] with arr[largest]
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        return arr

# Demo
hs = HeapSortCounter()
data = [12, 3, 19, 5]
print("Sorted:", hs.sort(data))
print("Total comparisons:", hs.comparisons)