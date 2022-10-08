#Python program to implement Subtree of another tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        if not t:
            return True
        if not s:
            return False
        
        if self.isSame(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
    def isSame(self,p,q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSame(p.left,q.left) and
        self.isSame(p.right,q.right))