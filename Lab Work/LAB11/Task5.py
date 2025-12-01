class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = ("DELETED", None)  # special marker for deleted slots

    def hash_function(self, key: int) -> int:
        return key % self.size

    def insert(self, key: int, value):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None and self.table[index] != self.DELETED:
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

    def delete(self, key: int):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]
            if stored_key == key:
                self.table[index] = self.DELETED
                print(f"Deleted key={key} from index={index}")
                return

            i += 1
            index = (original_index + i) % self.size
            if index == original_index:
                break

        print(f"Key={key} not found, cannot delete.")

    def display(self):
        print("---- Hash Table State ----")
        for i, item in enumerate(self.table):
            print(i, ":", item)
        print("\n")


if __name__ == "__main__":
    ht = LinearProbingHashTable(size=10)

    # Insert some keys
    ht.insert(2, "Ayesha")
    ht.insert(4, "Awais")
    ht.insert(6, "Hibah")
    ht.display()

    # Delete a key
    ht.delete(4)
    ht.display()

    # Try searching deleted key
    print("Search 4:", ht.search(4))  # should return None

    # Insert into deleted slot
    ht.insert(14, "Fatima")  # h(14)=4 → slot was deleted, should reuse
    ht.display()
