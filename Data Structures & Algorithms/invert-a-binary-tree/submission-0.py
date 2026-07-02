# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root

        def preorder(head):
            if not head:
                return
            left = head.left
            right = head.right
            head.left =right
            head.right = left
            preorder(head.left)
            preorder(head.right)
        preorder(head)
        return head
        