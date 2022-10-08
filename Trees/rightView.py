#Python program to implement Binary Tree Right Side View

import collections
from turtle import right


def rightSideView(root):
    q = collections.deque([root])
    res = []

    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    
    return res
