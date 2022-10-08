#Python program to implement Binary Tree Level Order Traversal

import collections


def levelOrderTraversal(root):
    res = []
    q = collections.deque()
    if root:
        q.append(root)
    
    while q:
        val = []
        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(val)
    
    return res