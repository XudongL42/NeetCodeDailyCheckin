# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # BFS
        q = deque()
        q.append(root)
        while q:
            r = q.popleft()
            left, right = r.left, r.right
            r.left = right
            r.right = left
            if left:
                q.append(left)
            if right:
                q.append(right)
            
        return root

class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # DFS
        stack = []
        stack.append(root)

        while stack:
            r = stack.pop()
            left, right = r.left, r.right
            r.right = left
            r.left = right
            if left:
                stack.append(left)
            if right:
                stack.append(right)
        return root