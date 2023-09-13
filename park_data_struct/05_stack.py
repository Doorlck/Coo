class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else: 
            return False
    
    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        if self.empty(): # 빈 리스트에서 pop하면 IndexError가 남.
            return None
        return self.container.pop()
    
    def peek(self):
        if self.empty():
            return None
        return self.container[-1]
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.container)
print(s.pop())
print(s.container)
print(f"{s.peek()} will be pop: {s.pop()}")