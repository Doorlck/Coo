from queue import Queue

class Stack:
    def __init__(self):
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()
    
    def peek(self):
        if self.empty():
            return None
        return self.container[-1]

class TreeNode:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

    def __del__(self):
        print("deleted")

    def data(self, data):
        self.data=data
        return self.data

    def left(self, left):
        self.left=left
        return self.left

    def right(self, right):
        self.right=right
        return self.right

## 전위 순회
def preorder(cur):
    if not cur:
        return

    print(cur.data, end='  ')
    preorder(cur.left)
    preorder(cur.right)

## 중위순회
def inorder(cur):
    if not cur:
        return

    inorder(cur.left)
    print(cur.data, end='  ')
    inorder(cur.right)

## 후위순회
def postorder(cur):
    if not cur:
        return

    postorder(cur.left)
    postorder(cur.right)
    print(cur.data, end='  ')

def iter_preorder(cur):
    s=Stack()
    while True:
        while cur:
            print(cur.data, end='  ')
            s.push(cur)
            cur=cur.left

        cur=s.pop()
        if not cur:
            break

        cur=cur.right

def iter_inorder(cur):
    s=Stack()
    while True:
        while cur:
            s.push(cur)
            cur=cur.left
        cur=s.pop()
        if not cur:
            break
        
        print(cur.data, end='  ')
        cur=cur.right

## 레벨순서조회(levelorder traversal)   
             
def levelorder(cur):
    q=Queue()

    q.put(cur)
    while not q.empty():
        cur=q.get()
        print(cur.data, end='  ')

        if cur.left:
            q.put(cur.left)

        if cur.right:
            q.put(cur.right)

if __name__=="__main__":
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    n7=TreeNode(7)

    n1.left=n2; n1.right=n3
    n2.left=n4; n2.right=n5
    n3.left=n6; n3.right=n7

    preorder(n1)
    iter_preorder(n1)
    print()

    inorder(n1)
    iter_inorder(n1)
    print()

    postorder(n1)
    print()

    levelorder(n1)
    print()