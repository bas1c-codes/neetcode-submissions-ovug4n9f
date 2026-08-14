# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val == n2.val:
                #print("Found match",n1.val,n2.val)
                x = sameTree(n1.left,n2.left)
                y =sameTree(n1.right,n2.right)
                return x and y
            else:
                return False
        def inorder(node):
            x= None
            if not node:
                return False
            if node.val == subRoot.val:
                if sameTree(node,subRoot):
                    return True
            return inorder(node.left) or inorder(node.right)
        return inorder(root)
        