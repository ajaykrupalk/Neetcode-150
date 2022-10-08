#Python program to implement Min Cost to Connect Components

import heapq


def minCost(points):
    N = len(points)

    adj = {i:[] for i in range(N)}#i: list of [cost, node]
    for i in range(N):
        x1,y1 = points[i]
        for j in range(i+1,N):
            x2,y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    #Prim's Algorithm
    res = 0
    visit = set()
    minHeap =[[0,0]] #[cost, point]
    while len(visit) < N:
        cost,i = heapq.heapop(minHeap)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost,nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minHeap, [neiCost, nei])
    return res
