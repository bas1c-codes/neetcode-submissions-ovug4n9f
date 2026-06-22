# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            temp = ListNode()
            if list1.val<list2.val:
                temp.val =list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            cur.next = temp
            cur = cur.next
        while list1:
            temp = ListNode(list1.val)
            cur.next = temp
            cur = cur.next
            list1 = list1.next

        while list2:
            temp = ListNode(list2.val)
            cur.next = temp
            cur = cur.next
            list2 = list2.next

        return dummy.next
