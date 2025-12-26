# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        height = {} # TreeNode:height(int)

        while stack:
            node = stack[-1]

            if node.left and node.left not in height:
                stack.append(node.left)
                continue
            if node.right and node.right not in height:
                stack.append(node.right)
                continue
            
            hleft = 0 if not node.left else height[node.left]
            hright = 0 if not node.right else height[node.right]

            if abs(hleft - hright) > 1:
                return False
            
            height[node] = max(hleft, hright) + 1
            stack.pop()
        
        return True