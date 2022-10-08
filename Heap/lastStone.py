#Python program to implement Last Stone Weight

import heapq

class Solution():
    def lastStoneWeight(self, stones):
       stones = [-s for s in stones]
       heapq.heapify(stones)
       
       while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            print(first,second)
            if second > first:
                heapq.heappush(stones, first - second)
                #first - second since values in heap are 
                #negated to make it a max heap
        
       stones.append(0)
       return abs(stones[0])

obj = Solution()
ans = obj.lastStoneWeight([2,7,4,1,8,1])
print(ans)