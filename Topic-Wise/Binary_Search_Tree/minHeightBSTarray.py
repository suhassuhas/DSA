def minHeightBst(array):
    n = len(array)
	if n == 0:
		return None
	if n == 1:
		return BST(array[0])
	left,right = 0,n-1
	mid = (left+right) //2
	root = BST(array[mid])
	root.left = minHeightBst(array[:mid])
	root.right = minHeightBst(array[mid+1:])
	return root	


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
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
                
############################ Solution 2 ############
def minHeightBst1(array):
    return minHeightBstHelper(array,None,0,len(array)-1)

def minHeightBstHelper(array,bst,l,r):
	if r < l:
		return 
	midIdx = (l+r) // 2
	if bst is None:
		bst = BST(array[midIdx])
	else:
		bst.insert(array[midIdx])
	minHeightBstHelper(array,bst,l,midIdx-1)
	minHeightBstHelper(array,bst,midIdx+1,r)
	return bst
	
# array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
