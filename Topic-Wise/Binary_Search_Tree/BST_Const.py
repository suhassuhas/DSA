class BST:
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
    
    def contains(self,value):
        if self == None:
            return False
        if self.value == value :
            return True
        if value < self.value:
            return self.left.contains(value) if self.left != None else False
        else:
            return self.right.contains(value) if self.right != None else False
    
    def delete(self,value,parent=None):
        if self == None:
            return 
        if value < self.value:
            if self.left != None:
                self.left.delete(value,self)
        elif value > self.value:
            if self.right != None:
                self.right.delete(value,self)
        else:
            if self.left != None and self.right != None:
                self.value = self.right.getMinVal()
                print(self.value,'i')
                self.right.delete(self.value,self)
            elif parent == None:
                if self.left != None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right != None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                parent.left = self.left if self.left != None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left != None else self.right
        return self
    
    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.remove(value,self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value,self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinVal()   
                self.right.remove(self.value,self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
				
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self
    
    def getMinVal(self):
        if self.left == None:
	        return self.value
        return self.left.getMinValue()


    def print_tree(self):
        if self is None:
            return
        if self.left != None:
            self.left.print_tree()
        print(self.value)
        if self.right != None:
            self.right.print_tree()
        
B = BST(10)
B.insert(4)
B.insert(12)
B.insert(1)
B.insert(6)
B.insert(14)
B.print_tree()
print("---")
B.delete(10)
B.print_tree()