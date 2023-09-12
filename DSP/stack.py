class Stack:
    def __init__(self):
        self.data = list()

    def add(self, x):
        self.data.append(x)

    def show(self):
        if (len(self.data) != 0):
            for i in self.data:
                print(i)

# if __name__ == "__main__":
#     print(12424)