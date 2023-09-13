class CQueue:
    MAXSIZE = 6
    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0  # 인덱스를 가리킨다고 이해하면된가
        self.rear = 0
        print(len(self.container))

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def is_full(self):
        pass

    def enqueue(self, data):
        pass

    def dequeue(self, data):
        pass

    def peek(self):
        pass


cq = CQueue()
print(cq.front)
print(cq.rear)