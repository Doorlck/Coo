class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, length):
        self.length = length
        self.table = [None] * length

    def hash_function(self, key):
        return hash(key) % self.length

    def add(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        if self.table[index] == None:
            self.table[index] = Node(key, value)
        elif current.key == key: 
            current.value = value
        else:
            while current:
                current.next = current
            current = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key != key:
                current = current.next
            elif current.key == key:
                current = current.next
                self.table[index] = current


hash_table = HashTable(length=10)

hash_table.add("red", 5)
hash_table.add("green", 7)
hash_table.add("blue", 3)

print(hash_table.search("red"))  # 출력: 5
print(hash_table.search("green")) # 출력: 7

hash_table.delete("green")
print(hash_table.search("green")) # None