# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pque = deque()
        pque.append(p)
        qque = deque()
        qque.append(q)

        while pque and qque:
            pnode = pque.popleft()
            qnode = qque.popleft()

            if not pnode and not qnode:
                continue
            
            if not pnode or not qnode:
                return False

            if pnode.val != qnode.val:
                return False
            
            pque.append(pnode.left)
            pque.append(pnode.right)
            qque.append(qnode.left)
            qque.append(qnode.right)
        
        if pque or qque:
            return False
        
        return True