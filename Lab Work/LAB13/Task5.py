class SelectionSort:
    # Constructor: runs when we create an object of this class
    def __init__(self, arr):
        # Store the array inside the object so other methods can use it
        self.arr = arr

    # Main method to perform selection sort
    def sort(self):
        # Find the length of the array
        n = len(self.arr)

        # Outer loop: select a position where we will place the smallest element
        for i in range(n):
            # Assume current i is the smallest in the unsorted part
            min_index = i

            # Inner loop: find the true smallest element in remaining part
            for j in range(i + 1, n):
                # Compare current element with current minimum
                if self.arr[j] < self.arr[min_index]:
                    # Update min_index if we found a smaller value
                    min_index = j

            # Swap: put smallest element at position i
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        # Return the sorted array
        return self.arr

# Example usage
data = [25, 10, 35, 5]
ss = SelectionSort(data)
print("Selection Sort Result:", ss.sort())