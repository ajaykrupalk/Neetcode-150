# Python program to implement Swim in Rising Water

import heapq
from multiprocessing import heap


def swimInWater(grid):
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]  # (time, r, c)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit.add((0, 0))
    while minH:
        t, r, c = heapq.heappop(minH)

        if r == N-1 and c == N-1:
            return t
        for dr, dc in directions:
            neiR, neiC = r+dr, c+dc
            if (neiR < 0 or neiC < 0 or
                neiR == N or neiC == N or
                (neiR, neiC) in visit):
                continue

            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(t, grid[neiR][neiC]),neiR, neiC])