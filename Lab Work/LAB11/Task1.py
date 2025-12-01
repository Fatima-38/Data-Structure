class LinearProbingHashTable:
    def __init__(self, size):
        # fixed size array, intially empty
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: int) -> int:
        """
        Simple modulo-based hash function.
        Returns an index between 0 and size-1.
        """
        return key % self.size

    def insert(self, key: int, value):
        """
        Insert (key, value) using linear probing.
        If collision occurs, move forward one-by-one.
        """
        index = self.hash_function(key)
        original_index = index
        i = 0

        # probe until we find an empty slot
        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]
            # if same key already exists, update its value
            if stored_key == key:
                self.table[index] = (key, value)
                print(f"Updated key = {key} at index = {index}")
                return

                i =+ 1
                index = (original_index + i) % self.size

                #safety check if table is full
                if index == original_index:
                    print("Hash table is full, cannot insert.")
                    return

        self.table[index] = (key, value)
        print(f"Inserted key = {key}, value = {value} at index = {index}")

    def search(self, key: int):
        """
        Search for a key using the same probing sequence.
        Returns the value if found, otherwise None.
        """
        index = self.hash_function(key)
        original_index = index
        i = 0

        # probe until we find an empty slot (or full circle)
        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]
            if stored_key == key:
                return stored_value

            i += 1
            index = (original_index + i) % self.size

            if index == original_index:
                break  # we checked entire table

        return None

    def display(self):
        """
        Print the complete hash table.
        """
        print("---- Hash Table State ----")
        for i, item in enumerate(self.table):
            print(i, ":", item)

# quick demo (you can modify these values)
if __name__ == "__main__":
    ht = LinearProbingHashTable(size=10)

    # Insert some keys
    ht.insert(25, "Alice")
    ht.insert(35, "Bob")
    ht.insert(45, "Charlie")
    ht.insert(15, "David")

    # Display table
    ht.display()

    # Search examples
    print("Search 35:", ht.search(35))
    print("Search 99:", ht.search(99))