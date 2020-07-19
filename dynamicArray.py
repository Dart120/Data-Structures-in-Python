class dynamicArray:
    def __init__(self):
        self.arr = []
        self.len = 0
        self._capacity = 0
        self.startArray()
        
    def startArray(self):
        self.arr.extend([None]*16)
        print(self.arr)
        self.len = 0
        self.capacity = 16
    @property
    def capacity(self):
        return self._capacity
    
        
    @capacity.setter
    def capacity(self,number):
        if number < 0:
            raise Exception("Capacity cannot be lower than 0")
        self._capacity = number
    def size(self):
        return self.len
    def isEmpty(self):
        return self.len == 0
    def __getitem__(self,index):
        return self.arr[index]
    def __setitem__(self,index,data):
        self.arr[index] = data
    def clear(self):
        self.arr = [None for i in self.arr]
    def append(self, elem):
        if self.len + 1 >= self._capacity:
            if self._capacity == 0:
                self._capacity = 1
            else:
                
                self._capacity = self._capacity * 2
                newArr = [None] * self._capacity
                print(hex(int(id(self.arr))),hex(int(id(newArr))))
                for i,data in enumerate(self.arr):
                    newArr[i] = data
                self.arr = newArr
        
        
        self.len +=1
        self.arr[self.len-1] = elem
    def removeAt(self,index):
        if index > self.len - 1:
            raise Exception('Index out of array')
        newArr = [None for i in range(self.capacity)]
        counter = 0
        for i,data in enumerate(self.arr):
            if i != index:
                newArr[counter] = data
                counter += 1
        self.arr = newArr
        self.len -= 1
        self.capacity -= 1
        
    def __iter__(self):
        for i in self.arr:
            if i == None:
                
                return 
            yield i
    def remove(self,item):
        if item in self.arr:
            index =  self.arr.index(item)
            self.removeAt(index)
        else:
            raise Exception('Item not in Array')
    def indexOf(self,item):
        if item in self.arr:
            index =  self.arr.index(item)
            return index
        else:
            raise Exception('Item not in Array')
        
    def contains(self,item):
        if item in self.arr:
            return True
        return False
        
    

    
        



       
    
    
        
            
        
    