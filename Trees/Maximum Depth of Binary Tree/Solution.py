# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # DFS
        stack = []
        stack.append([root, 1])
        maxDepth = 1

        while stack:
            r = stack.pop()
            left, right = r[0].left, r[0].right
            if r[1] > maxDepth:
                maxDepth = r[1]
            if left:
                stack.append([left, r[1] + 1])
            if right:
                stack.append([right, r[1] + 1])
        return maxDepth
    
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # BFS
        level = 0
        q = deque([root])

        while q:
            size = len(q)
            level += 1
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level