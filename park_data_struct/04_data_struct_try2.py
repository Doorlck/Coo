##1##
# 이중더미연결리스트 시험본



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data_size = 0

    def add_first(self, data):
        new_node = Node(data)
        
        new_node.next = self.head.next
        new_node.prev = self.head 
        
        self.head.next.prev = new_node
        self.head.next = new_node

        self.data_size += 1


if __name__=="__main__":

    dlist = DoubleLinkedList()
    dlist.add_first(1)
    cur2 = dlist.head.next
    dlist.add_first(2)
    dlist.add_first(3)
    dlist.add_first(5)
    while cur2 != dlist.tail:  # tail은 None으로 값이 다름
        print(cur2.data, end = " ")
        cur2 = cur2.next
    print()
    print(dlist.data_size)