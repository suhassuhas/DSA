# Given preorder traversal of a binary search tree, construct the BST.

# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be the root of the following tree.

#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	n = len(preOrderTraversalValues)
	if n == 0:
		return None 
	rightIdx = n
	for i in range(1,n):
		if preOrderTraversalValues[0] <= preOrderTraversalValues[i]:
			rightIdx = i
			break
	leftpotv = reconstructBst(preOrderTraversalValues[1:rightIdx])
	rightpotv = reconstructBst(preOrderTraversalValues[rightIdx:])
	return BST(preOrderTraversalValues[0],leftpotv,rightpotv)


			
	
class TreeInfo:
	def __init__(self,rootIdx):
		self.rootIdx = rootIdx

def reconstructBst1(preOrderTraversalValues):
    # Write your code here.
	treeInfo = TreeInfo(0)
	return reconstructBstRange(float("-inf"),float("inf"),preOrderTraversalValues,treeInfo)

def reconstructBstRange(lowerBound,upperBound,preOrderTraversalValues,currentSubtreeInfo):
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	
	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	currentSubtreeInfo.rootIdx += 1
	leftSubtree = reconstructBstRange(lowerBound,rootValue,preOrderTraversalValues,currentSubtreeInfo)
	rightSubtree = reconstructBstRange(rootValue,upperBound,preOrderTraversalValues,currentSubtreeInfo)
	return BST(rootValue,leftSubtree,rightSubtree)