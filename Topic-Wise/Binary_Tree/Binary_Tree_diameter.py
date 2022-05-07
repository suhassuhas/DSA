# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(tree):
	if tree == None:
		return 0
	return 1+max(height(tree.left),height(tree.right))
	

def binaryTreeDiameter(tree):
    # Write your code here.
    if tree == None:
		return 0
	
	leftHeight = height(tree.left)
	rightHeight = height(tree.right)
	print(leftHeight,rightHeight)
	leftBTDia = binaryTreeDiameter(tree.left)
	rightBTDia = binaryTreeDiameter(tree.right)
	
	return max(leftHeight+rightHeight,leftBTDia,rightBTDia)
