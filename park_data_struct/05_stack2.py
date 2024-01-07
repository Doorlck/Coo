class Stack:
    def __init__(self):
        self.container=list()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if not self.container:
            return None
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
if __name__=="__main__":
    s=Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.container)

    print(s.peek())

    print(s.pop())

    print(s.container)
