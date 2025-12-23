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
        if not head:
            return None
        
        # Add a duplicate to the next of each node
        cur = head
        while cur:
            dupNode = Node(cur.val, cur.next)
            cur.next = dupNode
            cur = dupNode.next
        
        cur = head
        curDup = head.next
        while cur:
            curDup.random = cur.random.next if cur.random else cur.random
            cur = curDup.next
            curDup = cur.next if cur else cur
        
        cur = head
        curDup = head.next
        copied = curDup
        while cur:
            cur_next = curDup.next
            curDup_next = cur_next.next if cur_next else cur_next
            cur.next = cur_next
            curDup.next = curDup_next
            cur = cur_next
            curDup = curDup_next
        
        return copied