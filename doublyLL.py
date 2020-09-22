class Double:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def indexOf(self,data):
        node = self.head
        counter = self.size
        while self.size != 0:
            if node.data == data:
                return self.size - counter
            else:
                counter -= 1
    def insertAtHead(self,data):
        
        if self.size == 0:
            node = Node(data,None,None)
            self.head = node
            self.tail = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node
        self.size += 1
    def insertAtTail(self,data):
        if self.size > 0:
            node = Node(data,None,self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.insertAtHead(data)
    def delHead(self):
        if self.size > 0:
            node = self.head
            self.head = node.next
            del node
            self.size -= 1
        else:
            raise Exception('No head to delete')
    def insertAtIndex(self,index,data):
        if index == 0:
            return self.insertAtHead(data)
        elif index > self.size:
            raise Exception('Index out of range')
        node = self.head
        for _ in range(index):
            
            node = node.next
            
        print(node.data)
        newNode = Node(data,node,node.prev)
        node.prev.next = newNode
        node.prev = newNode
        self.size += 1
    def removeAtIndex(self,index):
        if index > self.size:
            raise Exception('Index out of range')
        node = self.head
        for _ in range(index):
            
            node = node.next
            
        
        
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        self.size += 1
    def findAtIndex(self,index):
        if index > self.size - 1:
            raise Exception('Index out of range')
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data
    def find(self,data):
        node = self.head
        print(self.head.data)
        counter = self.size
        while self.size != 0:
            if not(node == None):
                if node.data == data:
                    return True
                else:
                    counter -= 1
                    node = node.next
            else:
                return False
        
        return False
    def removeAtTail(self):
        if self.size == 0:
            raise Exception('No tail to delete')
        if self.size == 1:
            tail = self.tail
            del tail
            self.tail = None
            self.head = None
            return
            
        tail = self.tail
        self.tail = tail.prev
        
        self.tail.next = None
        del tail
        self.size -= 1
    def state(self):
        node = self.head
        print(node.data)
        for i in range(self.size):
            if hasattr(node,'next'):
                node = node.next
            if hasattr(node,'data'):
                
                print(node.data)
            
            
    
        
class Node:
    def __init__(self,data,nuxt,prev):
        self.data = data
        self.next = nuxt
        self.prev = prev
DLL = Double()
DLL.insertAtHead(2)
DLL.insertAtHead(3)
DLL.insertAtIndex(1,9)
DLL.removeAtTail()
DLL.insertAtTail(1000)
DLL.delHead()


DLL.state()
class Queue:
    def __init__(self):
        self.queue = Double()
        self.length = self.queue.size
        self.front = self.queue.head
        self.back = self.queue.tail
    def enqueue(self,data):
        self.queue.insertAtHead(data)
    def dequeue(self):
        self.queue.removeAtTail()
    def contains(self,data):
        return self.queue.find(data)
    def remove(self,data):
        self.queue.removeAtIndex(self.queue.indexOf(data))
queue = Queue()
queue.enqueue(1)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.queue.state()
        