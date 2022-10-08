#Python program to implement Count Good Nodes in Binary Tree

def countGood(root):
    def dfs(node, maxVal):
        if not node:
            return 0
        
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)
        return res
    
    return dfs(root, root.val)
