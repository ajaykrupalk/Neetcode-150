#Python program to find the duplicate number

from asyncio import FastChildWatcher


def findDuplicate(nums):
    slow, fast = 0,0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow