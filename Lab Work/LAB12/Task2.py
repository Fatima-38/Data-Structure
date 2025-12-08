class HashTableBasic:
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
        # no collision handling yet
        self.table[index] = value
        print(f"Inserted '{key}' at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]


# Testing
ht = HashTableBasic(10)
ht.insert("Ali", 1111)
ht.insert("Azeem", 2222)

print("Ali ->", ht.search("Ali"))
print("Azeem ->", ht.search("Azeem"))