class MergeSortCounter:
    def __init__(self):
        self.comparisons = 0  # count comparisons during merge

    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.comparisons += 1  # we compare left[i] and right[j]

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

# Demo
ms = MergeSortCounter()
data = [4, 1, 7, 3, 6]
print("Sorted:", ms.sort(data))
print("Total comparisons:", ms.comparisons)