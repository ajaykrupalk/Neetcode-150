#Python program to implement Two Sum 2

def twoSum(nums, target):
    l,r =  0, len(nums)-1
    curSum = 0

    while l < r:
        curSum = nums[l] + nums[r]

        if curSum > target:
            r -= 1
        
        elif curSum < target:
            l += 1
        
        else:
            return [l+1, r+1]

print(twoSum([1,3,4,5,7,10,11], 9))