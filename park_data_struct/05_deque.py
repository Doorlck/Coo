from collections import deque

print("*"*20 + "STACK" + "*"*20)

stack = deque()

for i in range(1, 6):
    stack.append(i)
    print(stack)

for i in range(5):
    stack.pop()

print("*"*20 + "Queue" + "*"*20)

queue = deque()

for i in range(1, 6):
    queue.append(i)
    print(queue)

for i in range(5):
    queue.popleft()

if stack == queue:
    print(f"stack is {stack} and queue is {queue}")