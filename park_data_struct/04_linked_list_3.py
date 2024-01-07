## 노드
class Node:
    def __init__(self, data=None):
        self.data=data
        self.prev=None
        self.next=None
    
    def data(self, data):
        return self.data

    def next(self, data):
        self.next=data
        return self.next
    
    def prev(self, data):
        self.prev=data
        return self.prev

## 이중연결리스트 
class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()

        self.head.next=self.tail
        self.tail.prev=self.head

        self.node_size=0

    # 데이터를 head 다음에 삽임
    def add_first(self, data):
        new_node=Node()
        new_node.data=data

        new_node.next=self.head.next
        new_node.prev=self.head
        self.head.next.prev=new_node
        self.head.next=new_node

        self.node_size+=1

    # 데이터를 tail 이전에 삽임
    def add_last(self, data):
        new_node=Node()
        new_node.data=data

        new_node.next=self.tail
        new_node.prev=self.tail.prev
        self.tail.prev.next=new_node
        self.tail.prev=new_node
        
        self.node_size+=1

    # 데이터를 노드 다음에 삽임
    def insert(self, data, node):
        new_node=Node()
        new_node.data=data

        new_node.next=node.next
        new_node.prev=node
        node.next.prev=new_node
        node.next=new_node

        self.node_size+=1

    # target의 주소를 첫번째 데이터부터 탐색
    def search(self, data):
        
        node=self.head.next

        while node.data:
            if node.data==data:
                return node
            else: 
                node=node.next
        return None
    
    # 노드 삭제
    def delete(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

        self.node_size-=1

## 메인부
if __name__=="__main__":
    dlist=DoubleLinkedList()

    dlist.add_last(1)
    dlist.add_last(2)
    dlist.add_last(3)
    dlist.add_last(4)

    cur=dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur=cur.next

    print(f"search 7: {dlist.search(7)}")
    print(f"search 3: {dlist.search(3)}")

    dlist.delete(dlist.search(3))

    cur=dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur=cur.next
