# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def leftMostChild(node):
	current = node
	while current.left != None:
		current = current.left
	return current

def rightMostParent(node):
	current = node
	while current.parent != None and current.parent.right == current:
		current = current.parent
	return current.parent

def findSuccessor(tree, node):
    # Write your code here.
    if node.right != None:
		return leftMostChild(node.right)
	return rightMostParent(node)
