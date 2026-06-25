# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        c=0
        while c!=n:
            c+=1
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        nxt = slow.next
        slow.next = nxt.next
        return head
        