#Python program to implement TwoSum algorithm

def TwoSum(arr, target):
    prevMap = {}
    for i,n in enumerate(arr):
        if target-n in prevMap:
            return [prevMap[target-n], i]
        prevMap[n] = i
    return False

print(TwoSum([3,2,4], 6))