# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        nextn=None
        while cur:
            n=ListNode()
            n.val=cur.val
            n.next=nextn
            nextn=n
            cur=cur.next
        return nextn
        