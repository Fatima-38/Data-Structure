class LinearProbingHashTable:
    def __init__(self, size):
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
        print("\n")  # extra newline for readability


# ----------------------------------------------------
#               MAIN PROGRAM (VS CODE)
# ----------------------------------------------------
if __name__ == "__main__":
    ht = LinearProbingHashTable(size=10)

    # Insert keys one by one, display after each insertion
    print("Inserting 2 -> Ayesha")
    ht.insert(2, "Ayesha")
    ht.display()

    print("Inserting 4 -> Awais")
    ht.insert(4, "Awais")
    ht.display()

    print("Inserting 6 -> Hibah")
    ht.insert(6, "Hibah")
    ht.display()

    print("Inserting 8 -> Abdullah")
    ht.insert(8, "Abdullah")
    ht.display()

    print("Inserting 10 -> Fatima (collision at index 0)")
    ht.insert(10, "Fatima")  # h(10)=0, but 0 is free in this case? if 0 occupied, moves
    ht.display()

    print("Inserting 12 -> Usman")
    ht.insert(12, "Usman")
    ht.display()

    print("Inserting 16 -> Zara")
    ht.insert(16, "Zara")    # collision example
    ht.display()

    # Example of linear probing moving keys:
    print("Example: key 10 was expected at h(10)=0, but moved to next free slot due to collision.")
