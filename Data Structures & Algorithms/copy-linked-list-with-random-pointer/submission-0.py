"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        new_head=None
        dic={}
        prev = 0
        while head:
            if not prev:
                prev = Node(head.val)
                new_head = prev
                dic[head] = prev
            else:
                tmp = Node(head.val)
                prev.next = tmp
                prev = tmp
                dic[head] = tmp
            head = head.next
        head = dummy
        while head:
            if head.random in dic:
                tmp = dic[head.random]
                dic[head].random = tmp
            head = head.next
        return new_head
                
            
        