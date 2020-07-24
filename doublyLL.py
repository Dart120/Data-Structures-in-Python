class Double:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
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