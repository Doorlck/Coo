class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class HashTable:
    # 해시 테이블 구현
    def __init__(self, length):
        self.length = length
        self.table = list([None for _ in range(self.length)])

    # 해시 함수
    def hash_function(self, key):
       hash_key = sum([ord(i) for i in str(key)]) 
       return hash_key % self.length

    # 추가
    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] == None:
            self.table[index] = Node(key,value) # 데이터가 아닌 주소가 삽입되는 형태
        
        else: # 헤드에다 집어넣으면 계산이 더 빨라지나
            current = self.table[index]
            while current:
                current.next = current
            current = Node(key,value)

    # 탐색
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    # 삭제
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        if current and current.key == key:
            self.table[index] = current.next
            return
        while current and current.key != key:
            current.prev = current
            current = current.next
        if current:
            current.prev.next = current.next

hash_table = HashTable(length=10)

hash_table.add("red", 5)
hash_table.add("green", 7)
hash_table.add("blue", 3)

print(hash_table.search("red"))  # 5
print(hash_table.search("green")) # 7

hash_table.delete("green")
print(hash_table.search("green")) # None

print(hash_table.table)