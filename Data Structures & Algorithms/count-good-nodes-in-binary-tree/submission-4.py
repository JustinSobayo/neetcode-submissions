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

        q = collections.deque()
        q.append((root, root.val))

        ans = 0

        while q:
            node, path_max = q.popleft()

            if node.val >= path_max:
                ans += 1

            new_max = max(path_max, node.val)

            if node.left:
                q.append((node.left, new_max))

            if node.right:
                q.append((node.right, new_max))

        return ans