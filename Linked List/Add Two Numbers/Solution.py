# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        lead = ListNode()
        cur = lead
        while l1 or l2:
            cur_value = carry
            if l1:
                cur_value += l1.val
            if l2:
                cur_value += l2.val
            
            carry = cur_value // 10
            cur.next = ListNode(cur_value % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry == 1:
            cur.next = ListNode(1)
        
        return lead.next