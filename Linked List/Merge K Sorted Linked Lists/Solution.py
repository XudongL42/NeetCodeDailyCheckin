# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        hasNodes = True
        while hasNodes:
            hasNodes = False
            minNode = None
            for i in range(len(lists)):
                if lists[i]:
                    minNode = lists[i] if not minNode or lists[i].val < minNode.val else minNode
            
            if minNode:
                for i in range(len(lists)):
                    temp = lists[i]
                    if temp and temp.val == minNode.val:
                        cur.next = temp
                        lists[i] = temp.next
                        cur = cur.next
                        hasNodes = True
                        break
        
        return dummy.next