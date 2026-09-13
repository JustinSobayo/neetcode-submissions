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
        currentDepth = 1
        s = [(root, currentDepth)]
        maxDepth = 0
        while s:
            node, currentDepth = s.pop()
            maxDepth = max(currentDepth, maxDepth)
            if node.right:
                s.append((node.right, currentDepth + 1))
            if node.left:
                s.append((node.left, currentDepth + 1))
        return maxDepth
        