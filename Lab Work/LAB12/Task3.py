class HashTableLinear:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start = index

        # find empty slot
        while self.table[index] is not None:
            # if same key, update value (optional)
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size
            if index == start:
                print("Hash table is full")
                return

        self.table[index] = (key, value)
        print(f"Inserted '{key}' at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None
    
# Testing

ht = HashTableLinear(7)

ht.insert("Ali", 1111)
ht.insert("Lia", 2222)
ht.insert("Azeem", 3333)
ht.insert("Omar", 4444)
ht.insert("Usman", 5555)

print(ht.table)