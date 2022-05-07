# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self,isBalanced,height):
		self.isBalanced = isBalanced
		self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.
    ans = getTreeInfo(tree)
	return ans.isBalanced

def getTreeInfo(node):
	if node == None:
		return TreeInfo(True,-1)
	
	leftSubtreeinfo = getTreeInfo(node.left)
	rightSubtreeinfo = getTreeInfo(node.right)
	
	isBalanced = (
		leftSubtreeinfo.isBalanced and rightSubtreeinfo.isBalanced and
		abs(leftSubtreeinfo.height - rightSubtreeinfo.height) <= 1
	)
	height = 1+max(leftSubtreeinfo.height,rightSubtreeinfo.height)
	return TreeInfo(isBalanced,height)
	