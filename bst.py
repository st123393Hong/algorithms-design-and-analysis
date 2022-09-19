#how do we start here
#create a class called Node
class Node(object):  #object is the primitive class, so I inherit
    pass

    #left``
    #right
    #key
    #when you first create the Node, this guy is the root node
    def __init__(self, key):
        self.left  = None
        self.right = None
        
        self.key = key  #this is actually the root node
        #why you don't write like this
        #self.root = key

    
      
     
        
    #def insert
    def insert(self, key):
        #if we already have a root node,
        if(self.key):
            #then check left and right
            #cond1:  if less than: go left
            if(key < self.key):
                #cond1.1  if the left is NIL, yay! fill it!
                if(self.left == None):
                    self.left = Node(key)
                #cond1.2  if the left is NOT NIL...oh no...
                else:
                    self.left.insert(key)
            
            #cond2:  if greater than: go right
            elif(key >= self.key):
                #cond1.2  if the right is NIL, yay! fill it!
                if(self.right == None):
                    self.right = Node(key)
                #cond1.2  if the right is NOT NIL...consider right as the parent...
                else:
                    self.right.insert(key)
            
            
        #if we don't have the root node
        else:
            #this key is the root node
            self.key = key
    
    #def printTree
    def printT(self):        
        #if left is still available print left
        if (self.left):
            self.left.printT()
        print(self.key)
        if (self.right):
            self.right.printT()
    
    #def delete
    def delete(self,root,key):
        if not root:
            return root
        if root.key>key:
            root.left = self.delete(root.left,key)
        elif root.key<key:
           root.right = self.delete(root.right,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            x = root.right
            
            while x.left:                
                x = x.left            
            root.right = self.delete(root.right,root.key)
            x.right = root.left
            return x
        return root 
    
#try our class
root = Node(10)
root.insert(11)
root.insert(5)
root.insert(3)
root.insert(6)
root.insert(20)
root.insert(1)
#root.printT()
num = 5
root.delete(root,num)
print(f'after deleting the number {num}:')
root.printT()
