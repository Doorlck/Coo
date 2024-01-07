class CQueue:
    def __init__(self, max_size):
        self.max_size=max_size
        self.container=[None]*max_size
        self.front=self.rear=0
    

    def is_empty(self):
        if self.front==self.rear:
            return True
        return False
    
    def is_full(self):
        if self.__step_forward(self.rear)==self.front:
            return True
        return False

    def __step_forward(self, x):
        x+=1
        if x>=self.max_size:
            x=0
        return x

    def enqueue(self, data):
        if self.is_full():
            #raise Exception("---------The queue is Full---------")
            print("FULL")
            return

        self.container[self.rear]=data
        self.rear=self.__step_forward(self.rear)

    def dequeue(self):
        if self.is_empty():
            #raise Exception("---------The queue is Empty---------")
            print("EMPTY")
            return
        
        temp=self.front
        self.front=self.__step_forward(self.front)
        return self.container[temp]
    
    def peek(self):
        if self.is_empty():
            #raise Exception("---------The queue is Empty---------")
            print("EMPTY")
            return
        
        return self.container[self.front]
    
if __name__=="__main__":
    cq=CQueue(5)

    for i in range(3):
        cq.enqueue(i)
    
    print(cq.container)

    cq.dequeue()
    cq.dequeue()
    print(f"front: {cq.front}, rear: {cq.rear}")
    
    for i in range(3,6):
        cq.enqueue(i)

    print(cq.container)
    print(f"front: {cq.front}, rear: {cq.rear}")

    


