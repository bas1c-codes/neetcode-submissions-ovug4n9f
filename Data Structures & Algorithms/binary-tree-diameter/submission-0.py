
class Solution:
    def __init__(self):
         self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.hight(root)
        return self.diameter
        
    def hight(self,head):
        if not head:
            return 0
        left = self.hight(head.left)
        right = self.hight(head.right)
        self.diameter = max(self.diameter,right+left)
        return 1+max(left,right)




        