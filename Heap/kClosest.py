#Python program to implement K closest points to origin

import heapq


class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for x,y in points:
            dist = (x ** 2) + (y**2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)#sorts it in ascending order
        res = []
        while k > 0:
            dist,x,y = heapq.heapop(minHeap)
            res.append([x,y])
            k-=1

        return res
