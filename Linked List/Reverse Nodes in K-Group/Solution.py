# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        pre_head = dummy

        stack = []
        while cur:
            l = len(stack)
            if l < k:
                stack.append(cur)
                cur = cur.next
            elif l == k:
                while stack:
                    temp = stack.pop()
                    print(f"{l}, {temp.val}")
                    pre_head.next = temp
                    pre_head = pre_head.next
                pre_head.next = cur
        if len(stack) == k:
            while stack:
                temp = stack.pop()
                print(f"{l}, {temp.val}")
                pre_head.next = temp
                pre_head = pre_head.next
            pre_head.next = cur
        
        return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            cur = groupPrev
            for i in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
                print(f"{groupPrev.val}, {cur.val}")
            
            # otherwise counter == k, k nodes to reverse
            groupHead = newGroupHead = groupPrev.next
            groupEnd = cur
            while groupHead != groupEnd:
                temp = groupHead.next
                groupPrev.next = temp
                groupHead.next = groupEnd.next
                groupEnd.next = groupHead
                groupHead = temp
            groupPrev = newGroupHead
        return dummy.next