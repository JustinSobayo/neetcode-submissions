# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def good(curr, maxVal):
            if not curr:
                return 0
            res = 1 if curr.val >= maxVal else 0
            maxVal = max(maxVal, curr.val)
            res +=good(curr.left, maxVal)
            res +=good(curr.right, maxVal)
            return res
        return good(root, root.val)