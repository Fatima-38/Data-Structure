class LinearProbingHashTable:
    def __init__(self, size):
        # fixed-size array, initially empty
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: int) -> int:
        return key % self.size

    def insert(self, key: int, value):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]

            if stored_key == key:
                self.table[index] = (key, value)
                print(f"Updated key={key} at index={index}")
                return

            i += 1
            index = (original_index + i) % self.size

            if index == original_index:
                print("Hash table is full, cannot insert.")
                return

        self.table[index] = (key, value)
        print(f"Inserted key = {key}, value = {value} at index = {index}")

    def search(self, key: int):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]
            if stored_key == key:
                return stored_value

            i += 1
            index = (original_index + i) % self.size

            if index == original_index:
                break

        return None

    def display(self):
        print("---- Hash Table State ----")
        for i, item in enumerate(self.table):
            print(i, ":", item)


# ----------------------------------------------------
#               MAIN PROGRAM (FOR VS CODE)
# ----------------------------------------------------
if __name__ == "__main__":
    ht = LinearProbingHashTable(size=10)

    # Insert some keys
    ht.insert(2, "Ayesha")
    ht.insert(4, "Awais")
    ht.insert(6, "Hibah")
    ht.insert(8, "Abdullah")
    ht.insert(10, "Fatima")
    ht.insert(12, "Usman")
    ht.insert(16, "Zara")

    # Display table
    ht.display()

    # Search examples (Task B1)
    print("Search 4:", ht.search(4))
    print("Search 9:", ht.search(9))
    print("Search 35:", ht.search(35)) 
    print("Search 99:", ht.search(99))


keys = [2, 4, 6, 26, 52]

for key in keys:
    result = ht.search(key)
    if result is not None:
        print(f"Key {key}: Found -> {result}")
    else:
        print(f"Key {key}: Not found")
