# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def search(curr):
            if not curr.left and curr.val>val:
                curr.left = TreeNode(val)
                return
            if not curr.right and curr.val<val:
                curr.right = TreeNode(val)
                return
            if val>curr.val:
                search(curr.right)
            if val< curr.val:
                search(curr.left)
            

        search(root)
        return root