# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [root]
        dmap = {} # node: depth
        diameter = 0

        while stack:
            node = stack[-1]

            if node.left and node.left not in dmap:
                stack.append(node.left)
                continue
            if node.right and node.right not in dmap:
                stack.append(node.right)
                continue
            node = stack.pop()
            leftDepth = 0 if not node.left else dmap[node.left]
            rightDepth = 0 if not node.right else dmap[node.right]
            diameter = max(diameter, leftDepth + rightDepth)
            dmap[node] = max(leftDepth, rightDepth) + 1
        
        return diameter