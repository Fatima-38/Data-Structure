class HeapSort:
    # heapify maintains max-heap property for subtree rooted at i
    def heapify(self, arr, n, i):
        largest = i             # assume i is largest
        left = 2 * i + 1        # left child index
        right = 2 * i + 2       # right child index

        # if left child exists and is bigger than current largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # if right child exists and is bigger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # if largest changed, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # main method to heap sort
    def sort(self, arr):
        n = len(arr)

        # Step 1: build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Step 2: extract elements one by one
        for i in range(n - 1, 0, -1):
            # move current max to the end
            arr[i], arr[0] = arr[0], arr[i]
            # heapify the reduced heap
            self.heapify(arr, i, 0)

        return arr

# Example usage
h = HeapSort()
data = [12, 3, 19, 5, 26]
print("Heap Sort Result:", h.sort(data))