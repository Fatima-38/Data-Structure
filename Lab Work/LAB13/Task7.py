class MergeSort:
    # Public method to start merge sort
    def sort(self, arr):
        # Base case: 0 or 1 item is already sorted
        if len(arr) <= 1:
            return arr

        # Split array into two halves
        mid = len(arr) // 2
        left_half = self.sort(arr[:mid])   # recursively sort left
        right_half = self.sort(arr[mid:])  # recursively sort right

        # Merge the two sorted halves
        return self.merge(left_half, right_half)

    # Helper method: merge two sorted arrays into one sorted array
    def merge(self, left, right):
        result = []   # final merged list
        i = 0         # pointer for left
        j = 0         # pointer for right

        # Compare elements and take smaller one first
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add any remaining elements (only one side may have leftover)
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# Example usage
m = MergeSort()
data = [4, 1, 7, 3, 6]
print("Merge Sort Result:", m.sort(data))