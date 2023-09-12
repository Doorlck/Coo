##1##
# 이중더미연결리스트
class Node: 
    def __init__(self, data=None):
        self.__data = data

        self.__prev = None
        self.__next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.data = data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next
    
    @next.setter  
    def next(self, n):
        self.__next = n

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node() # 더미노드: 실제 데이터를 저장하지 않는 노드
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d_size = 0

    def add_first(self, data):
        new_node = Node(data)
        
        new_node.next = self.head.next
        new_node.prev = self.head 
        
        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        new_node = Node(data)

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        self.d_size += 1
    


if __name__=="__main__":

    dlist = DoubleLinkedList()
    dlist.add_first(1)
    cur2 = dlist.head.next
    dlist.add_first(2)
    dlist.add_first(3)
    dlist.add_first(5)
    while cur2 is not dlist.tail:
        print(cur2.data, end = " ")
        cur2 = cur2.next
    print()
    print(dlist.d_size)