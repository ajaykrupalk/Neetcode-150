'''
Method to implement Sliding Window Maximum
Initialise a queue and two pointers l and r
l and r are used to keep track of the window
if there is a small element in the window, pop it from the queue
if the window size is greater than k, pop the left element from the queue
and append the max element to the output
'''

import collections


def maxSlidingWindow(nums, k):
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        #pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
            
        q.append(r)

        # remove left val from window since we move the window
        # Note: we are storing the indices of the max in window
        if l > q[0]:
            print('here',nums[r],l,q[0])
            q.popleft()
        
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output

print(maxSlidingWindow([8,7,6,9], 2))