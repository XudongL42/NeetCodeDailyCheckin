# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        stack = [root]

        while stack:
            rNode = stack.pop()
            if self.isSameTree(rNode, subRoot):
                return True
            if rNode.left:
                stack.append(rNode.left)
            if rNode.right:
                stack.append(rNode.right)
            
        return False

    def isSameTree(self, rRoot: Optional[TreeNode], sRoot: Optional[TreeNode]) -> bool:
        stack = [(rRoot, sRoot)]

        while stack:
            rNode, sNode = stack.pop()

            if not rNode and not sNode:
                continue
            if not rNode or not sNode or rNode.val != sNode.val:
                return False

            stack.append((rNode.left, sNode.left))
            stack.append((rNode.right, sNode.right))

        return True