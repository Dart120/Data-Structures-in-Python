class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def addHead(self,data):
        node = Node(data,self.head)
        self.head = node
    @staticmethod
    def raiser(exception):
        raise Exception(exception)
    def insertAtHead(self,data):
        node = Node(data,self.head)
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1
    def insertAtTail(self,data):
        if self.size == 0:
            self.insertAtHead(data)
            
        else:
            node = self.tail
            node.next = Node(data,None)
            self.size += 1
            
    def delHead(self):
        if self.size > 0:
            
            node = self.head
            self.head = node.next
            del node
            self.size -= 1
        else:
            raise Exception('No head to delete')
    def insertAtIndex(self,index,data):
        if index > self.size -1:
            raise Exception('Index out of range')
        if index == 0:
            self.insertAtHead(data)
        else:
            node = self.head
            node2 = self.head
            for _ in range(index):
                node = node.next
            for _ in range(index-1):
                node2 = node2.next
            node3 = Node(data,node)
            node2.next = node3
            self.size += 1
    def findAtIndex(self,index,data):
        if index > self.size - 1:
            raise Exception('Index out of range')
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data
    def find(self,data):
        node = self.head
        found = True if node.data == data else False
        for _ in range(self.size):
            node = node.next
            found = True if node.data == data else False  
        return found
    def removeAtTail(self):
        if self.size == 0:
            raise Exception('No tail to delete')
        node = self.head
        tail = self.tail
        for i in range(self.size -1):
            node = node.next
        node.next = None
        del tail
        self.tail = node
        self.size -= 1
            
class Node:
    def __init__(self,data,node):
        self.data = data
        self.next = node
thing = LinkedList()
thing.insertAtHead(0)
thing.removeAtTail()