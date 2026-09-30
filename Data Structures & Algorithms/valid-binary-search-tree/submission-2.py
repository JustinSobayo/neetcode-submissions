# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr, lower_bound, upper_bound):
            if not curr:
                return True
            if not lower_bound<curr.val<upper_bound:
                return False
            return(valid(curr.left, lower_bound, curr.val) and valid(curr.right, curr.val, upper_bound))
        return valid(root, float('-inf'), float('inf'))