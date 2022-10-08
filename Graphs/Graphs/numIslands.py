#Python program to implement number of islands

import collections


def numIslands(self, grid):
    if grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0


    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                if ((r+dr) in range(rows) and 
                (c+dc) in range(cols) and 
                grid[r+dr][c+dc] == "1" and 
                (r+dr, c+dc) not in visited):
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r.c) not in visited:
                bfs(r,c)
                islands += 1
    return islands
