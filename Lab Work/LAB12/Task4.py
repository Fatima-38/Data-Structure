class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
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
        new_node = Node(key, value)

        # insert at head of linked list
        new_node.next = self.table[index]
        self.table[index] = new_node
        print(f"Inserted '{key}' at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    # deleting first node
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                print(f"Deleted '{key}' from index {index}")
                return
            prev = current
            current = current.next

        print(f"Key '{key}' not found")

    def display(self):
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")

# Testing the HashTableChaining

# Create hash table of size 5
ht = HashTableChaining(5)

# Insert keys
ht.insert("Ali", 1111)
ht.insert("Lia", 2222)
ht.insert("Azeem", 3333)
ht.insert("Omar", 4444)
ht.insert("Usman", 5555)

print("\nHash table after insertions:")
ht.display()

# Search keys
print("\nSearch results:")
print("Ali ->", ht.search("Ali"))
print("Omar ->", ht.search("Omar"))
print("XYZ ->", ht.search("XYZ"))

# Delete a key
ht.delete("Lia")

print("\nHash table after deleting 'Lia':")
ht.display()