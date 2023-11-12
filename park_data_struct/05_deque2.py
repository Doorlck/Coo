class MyDeque:
    def __init__(self):
        self.items = []

    def append_left(self, value):
        self.items.insert(0, value)

    def append_right(self, value):
        self.items.append(value)

    def pop_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def pop_right(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

my_deque = MyDeque()

my_deque.append_left(1)
my_deque.append_left(2)
my_deque.append_right(3)
my_deque.append_right(4)

print("deque:", my_deque.items)  # deque: [2, 1, 3, 4]

left_value = my_deque.pop_left()
right_value = my_deque.pop_right()

print("pop left:", left_value)   # pop Left: 2
print("pop right:", right_value)  # pop Right: 4

print("deque size:", my_deque.size())   # dque Size: 2
print("empty:", my_deque.is_empty())  # empty: False