# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h = self.bal(root)
        if h ==-1:
            return False
        return True
    def bal(self,node):
        if not node:
            return 0
        left = self.bal(node.left)
        if left == -1:
            return -1
        right = self.bal(node.right)
        if right ==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
        