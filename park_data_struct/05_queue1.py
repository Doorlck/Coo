class Queue:
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
        if self.empty():
            return None
        return self.container.pop(0) # 빅오는 O(n)
    
    def peek(self):
        if self.empty():
            return None
        return self.container[0]
    
q = Queue()
print(q.pop())
