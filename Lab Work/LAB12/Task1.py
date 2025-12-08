def simple_hash(key, size):
    total = 0
    for ch in key:
        total += ord(ch) # convert into ASCII  and sum the values
    return total % size

# Test your function
size = 10
print(simple_hash("Ali", size))
print(simple_hash("Azeem", size))
print(simple_hash("Lia", size))
print(simple_hash("Omar", size))