class Node:
    def __init__(self,data,nuxt):
        self.next = nuxt
        self.data = data
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def isEmpty(self):
        return self.head == None
    def size(self):
        return self.length
    def sizeI(self):
        node = self.head
        counter = 1
        if node == None:
            return 0
        else:
            while node.next != None:
                node = node.next
                counter += 1
        return counter
    def valueAt(self, index):
        if index > self.size()-1 or index < 0:
            return 'out of range'
        node = self.head
        while index != 0:
            
            node = node.next
            index-= 1
        return node.data
    def push_front(self, value):
        node = self.head
        newHead = Node(value,node)
        self.head = newHead
        self.length += 1
    def pop_front(self):
        if self.isEmpty():
            return 'nothing to delete'
        node = self.head
        newHead = self.head.next
        self.head = newHead
        value = node.data
        del node
        self.length -= 1
        return value
    def push_back(self,value):
        node = self.head
        newTail = Node(value,None)
        if self.isEmpty():
            self.head = newTail
        else:
            counter = self.length - 1
            while counter != 0:
                node = node.next
            node.next = newTail
        self.length += 1
    def __str__(self):
        node = self.head
        ll = ''
        while node != None:
            ll += str(node.data) + '-->'
            node = node.next
        end = 'Null'
        return ll + end
    def pop_back(self):
        node = self.head
        if self.isEmpty():
            return 'nothing to delete'
        elif node.next == None:
            data = node.data
            self.head = None
            del node
            self.length -= 1
        else:
            for i in range(self.length - 1):
                node = node.next
            tail = node
            node = self.head
            for i in range(self.length - 2):
                node = node.next
            pu = node
            pu.next = None
            data = tail.data
            del tail
            self.length -= 1 
        return data
    def front(self):
        if self.isEmpty():
            print('Nothing to show you')
        else:
            return self.head.data
    def back(self):
        node = self.head
        if self.isEmpty():
            print('Nothing to show you')
        else:
            for i in range(self.length - 1):
                node = node.next
            return node.data
    def insert(self,index,value):
        load = self.head
        node = Node(value,None)
        if index > self.length - 1:
            print('index does not exist')
        
        elif index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            for i in range(index - 1):
                load = load.next
            prev = load
            load = self.head
            for i in range(index):
                load = load.next
            nuxt = load
            prev.next = node
            node.next = nuxt
            self.length += 1
        print(self)
    def erase(self,index):
        load = self.head
        if index > self.length - 1:
            print('index does not exist')
        
        elif index == 0:
            load.next = self.head
            self.head = load.next
            self.length += 1
        else:
            for i in range(index - 1):
                load = load.next
            prev = load
            load = self.head
            for i in range(index):
                load = load.next
            nuxt = load
            prev.next = load
            load.next = nuxt
            self.length += 1
        print(self)
    def n_from_end(self,n):
        return self.valueAt(self.length - n)
    def reverse(self):
        prev = None
        current = self.head 
        while current is not None: 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

            
                
        
        
        
            
        
            
        
            
        
                
List = LinkedList()



List.push_front(4)
List.push_front(4)
List.push_front(4)
List.push_front(2)
List.push_front(4)
print(List)
List.reverse()
print(List)

        