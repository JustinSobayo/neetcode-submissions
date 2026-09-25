# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(curr):
            if not curr:
                return True, 0
            leftBalanced, leftHeight = dfs(curr.left)
            rightBalanced, rightHeight = dfs(curr.right)
            if abs(leftHeight - rightHeight) <= 1 and leftBalanced and rightBalanced:
                self.balanced = True
            else:
                self.balanced = False
            return self.balanced, 1 + max(leftHeight, rightHeight)
        dfs(root)
        return self.balanced
        