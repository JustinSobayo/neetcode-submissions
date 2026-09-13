# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        qstack = [(q, q.val)]
        pstack = [(p, p.val)]

        while pstack and qstack:
            pnode, pv = pstack.pop()
            qnode, qv = qstack.pop()
            #check vs
            if pv != qv:
                return False
            # add nodes
            if pnode.right and not qnode.right or pnode.left and not qnode.left or qnode.left and not pnode.left or qnode.right and not pnode.right:
                return False

            if pnode.right:
                pstack.append((pnode.right, pnode.right.val))
            if qnode.right:
                qstack.append((qnode.right, qnode.right.val))
            if pnode.left:
                pstack.append((pnode.left, pnode.left.val))
            if qnode.left:
                qstack.append((qnode.left, qnode.left.val))
    
        if len(pstack) != len(qstack):
            return False
        else:
            return True