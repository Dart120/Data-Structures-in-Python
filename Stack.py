class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def raiser(self,exception):
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
        for _ in range(self.size -1):
            node = node.next
        node.next = None
        del tail
        self.tail = node
        self.size -= 1
            
class Node:
    def __init__(self,data,node):
        self.data = data
        self.next = node
        
class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.size = self.stack.size
        self.capacity = 10
    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size == 0
    def pop(self):
        if self.isEmpty():
            raise Exception('Nothing to pop')
        self.peek()
        self.stack.delHead()
        self.size -= 1
    def push(self, data):
        if self.isFull():
            raise Exception('Stack is full')
        self.stack.insertAtHead(data)
        self.size += 1
    def peek(self):
        return self.stack.head.data if not stack.isEmpty() else 'stack is Empty'
    
    
stack = Stack()

print(stack.peek())
        
        
            
        
