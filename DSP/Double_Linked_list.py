#더미 이중 연결리스트
#보통 연결 리스트라고 하면 더미 이중 연결리스트를 의미한다. 

#노드를 정의한 클래스
class Node:
    def __init__(self,data=None):
        self.__data=data
        self.__prev=None
        self.__next=None

    def __def__(self):
        print(f"Data of {self.data} is deleted")

    
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self,p):
        self.__prev = p

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,n):
        self.__next = n


#더미 이중 연결리스트클래스 구현
#ADT:
# 1.empty()
# 2.size()
# 3.add_first()
# 4.add_last()
# 5.insert_after()
# 6.search.forward()
# 7.delete_first()
# 8.delete_last()

class DoubleLinkedList:
    def __init__(self):
        #더미 노드
        #실제 데이터를 저장하지 X
        self.head = Node() #리스트의 처음
        self.tail = Node() #리스트의 끝

        self.head.next=self.tail
        self.tail.prev=self.head

        self.d_size = 0

        def empty(self):
            if self.d_size == 0:
                return True
            return False
        
        def size(self):
            return self.d_size
        
        def add_fist(self,data):
            new_node= Node(data)

            new_node.next = self.head.next
            new_node.prev= self.head

            self.head.next.prev = new_node
            self.head.next = new_node

            self.d_size += 1

        def add_last(self,data):
            new_node= Node(data)

            new_node.next= self.tail
            new_node.prev= self.tail.prev

            self.tail.prev.next= new_node
            self.tail.prev= new_node
            
            self.d_size += 1


        def inset_after(self,data,node):
            new_node= Node(data)

            new_node.next= node.next
            new_node.prev= node

            node.next.prev= new_node
            node.next= new_node
            
            self.d_size += 1

        def search_forward(self,target):
            cur = self.head.next

            while cur is not self.tail :
                if cur.data == target:
                    return cur
                cur= cur.next

            return None
        
        def delete_first(self):
            if self.empty():
                return 
            
            self.head.next= self.head.next.next
            self.head.next.prev= self.head

            self.d_size -= 1

        def delete_last(self):
            if self.empty():
                return
            self.tail.prev= self.tail.prev.prev
            self.tail.prev.next= self.tail

            self.d_size -= 1














            





