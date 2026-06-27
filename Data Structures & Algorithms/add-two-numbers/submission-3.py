# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cu=l1
        cur=l2
        c=0
        n=None
        d=None
        head=None
        while cu or cur:
            x=None
            y=None
            if not cu:
                x=0
            else:
                x=cu.val
                cu=cu.next
            if not cur:
                y=0
            else:
                y=cur.val
                cur=cur.next
            r=0
            if len(str(x+c+y))>1 :
                r=int(str(x+y+c)[-1])
                c=int(str(x+y+c)[0])
            else:
                r=x+y+c
                c=0
            if n is None:
                n=ListNode(r)
                head=n
            else:
                d=ListNode(r)
                n.next=d
                n=d
        if c!=0:
            t=ListNode(c)
            n.next =t
        return head