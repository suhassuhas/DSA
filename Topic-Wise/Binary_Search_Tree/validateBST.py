# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root,float("-inf"),float("inf"))
    
    def isValidBSTHelper(self,root,minValue,maxValue):
        if root == None:
            return True
        if root.left != None and root.val <= root.left.val:
            return False
        if root.right != None and root.val >= root.right.val:
            return False
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self.isValidBSTHelper(root.left,minValue,root.val) and self.isValidBSTHelper(root.right,root.val,maxValue)