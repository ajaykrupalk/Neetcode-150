#Python program to implement container with most water

def isMost(heights):
    l, r = 0, len(heights)-1
    maxArea = 0

    while l < r:
        dist = r - l
        minVal = min(heights[l], heights[r])
        area = dist * minVal
        maxArea = max(maxArea, area)

        if heights[l] < heights[r]:
            l += 1
        
        else:
            r -= 1
    
    return maxArea

print(isMost([1,8,6,2,5,4,8,3,7]))