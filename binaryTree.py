from queue import Queue
from collections import deque
class Node:
    def __init__(self,data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
        
        
        self.stack = ['N','R','L']
class BinaryTree:
    def __init__(self,root):
        self.root = root
    def height(self,node):
        if node==None:
            return 0
        else:
            return 1+ max(self.height(node.left),self.height(node.right))
    def size(self,node):
        if node==None:
            return 0
        else:
            return 1+ self.size(node.left)+ self.size(node.right)

        
        
    def bfs(self):
        q = Queue()
        
        q.put(self.root)
        while not q.empty():
            node = q.get()
            if node.left != None:
                q.put(node.left) 
            if node.right != None:
                q.put(node.right)
            print (node.data)
    # def dfs(self):
    #     node = self.root
    #     Stack = []
    #     Stack.append(node)
    #     while len(Stack) > 0:
    #         if len(node.stack) == 0:
              
    #             node = Stack.pop()
                
    #         else:
    #             action = node.stack.pop()
    #         if action == 'N':
    #             print(node.data)
    #             Stack.append(node)
    #         elif action == 'L':
    #             if node.left != None:
    #                 node = node.left
    #                 Stack.append(node)
    #         elif action == 'R':
    #             if node.right != None:
    #                 node = node.right
    #                 Stack.append(node)
    def dfs(self):
        node = self.root
        Stack = []
        Stack.append(node)
        while len(Stack) != 0:
            if len(node.stack) == 0:
                node = Stack.pop()
            else:
                action = node.stack.pop()
                if action == 'N':
                    print(node.data)
                elif action == 'L':
                    if node.left != None:
                        node = node.left
                        Stack.append(node)
                elif action == 'R':
                    if node.right != None:
                        node = node.right
                        Stack.append(node)
                    
            
            
            
        
        
        

        
        
        
        
        
        
            
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
j = Node('j')
k = Node('k')
Tree = BinaryTree(a)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = h
e.left = i
e.right = j
c.left = f
c.right = g
g.right = k



#print(Tree.bfs(Tree.root,q))
print(Tree.dfs())
