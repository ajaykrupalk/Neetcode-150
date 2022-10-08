#Python program to implement Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))