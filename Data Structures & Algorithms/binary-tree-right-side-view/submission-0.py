# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = collections.deque()
        q.append(root)
        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                ans.append(levels[-1])
            else: continue
            print(ans)
        return ans
            
            


            
