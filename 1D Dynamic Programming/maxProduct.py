#Python program to implement Maximum Product Subarray

def maxProduct(nums):
    res = nums[0]
    curMin, curMax = 1,1

    for n in nums:
        temp = curMax * n
        curMax = max(curMax * n, curMin * n, n)
        curMin = min(temp, curMin * n, n)
        res = max(res, curMax)
    
    return res