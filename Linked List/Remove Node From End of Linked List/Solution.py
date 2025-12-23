# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        i = length - n
        temp = ListNode()
        temp.next = head
        result = temp
        while i > 0:
            temp = temp.next
            i -= 1
        
        print(f"{temp.val}, {length}")
        if temp.next:
            temp.next = temp.next.next
        
        return result.next