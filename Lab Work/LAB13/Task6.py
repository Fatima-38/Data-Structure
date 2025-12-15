class InsertionSort:
    # Constructor: called when we create an object
    def __init__(self, arr):
        # Save input array inside the object
        self.arr = arr

    # Main method to perform insertion sort
    def sort(self):
        # Start from index 1 because index 0 alone is already “sorted”
        for i in range(1, len(self.arr)):
            # key is the value we want to insert correctly
            key = self.arr[i]

            # j will move left inside the sorted part
            j = i - 1

            # Shift bigger elements one step to the right
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]  # shift right
                j -= 1                          # move left

            # Place key at correct position
            self.arr[j + 1] = key

        return self.arr

# Example usage
data = [8, 2, 5, 3]
isort = InsertionSort(data)
print("Insertion Sort Result:", isort.sort())