# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.ans = []
        def dfs(curr):
            if not root:
                return None
            if curr.left:
                dfs(curr.left)
            if curr.right:
                dfs(curr.right)
            self.ans.append(curr.val)
        dfs(root)
        return self.ans
            
        