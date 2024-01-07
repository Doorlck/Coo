## chat gpt 버전
class HashTable:
    def __init__(self):
        self.size = 10  # 해시 테이블의 크기를 10으로 설정
        self.table = [None] * self.size

    def hash_func(self, key):
        return hash(key) % self.size  # 간단한 해시 함수: key의 해시값을 테이블 크기로 나눈 나머지를 반환

    def insert(self, key, value):
        index = self.hash_func(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]  # 새로운 키와 값을 삽입
        else:
            for pair in self.table[index]:
                if pair[0] == key:  # 이미 존재하는 키라면 값을 업데이트
                    pair = (key, value)
                    return
            self.table[index].append((key, value))  # 존재하지 않는 키라면 새로운 키와 값을 추가

    def search(self, key):
        index = self.hash_func(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]  # 해당 키에 대한 값 반환
        return None  # 키를 찾지 못했을 때 None 반환

    def delete(self, key):
        index = self.hash_func(key)
        if self.table[index] is None:
            return False  # 키를 찾지 못했을 때 False 반환
        else:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]  # 해당 키를 삭제
                    return True
        return False  # 키를 찾지 못했을 때 False 반환

# 해시 테이블 생성
my_hash_table = HashTable()

# 데이터 삽입
my_hash_table.insert('apple', 10)
my_hash_table.insert('orange', 20)
my_hash_table.insert('banana', 30)

# 데이터 검색
print(my_hash_table.search('apple'))  # 'apple'에 해당하는 값 출력

# 데이터 삭제
my_hash_table.delete('orange')

# 테이블 확인
print(my_hash_table.table)