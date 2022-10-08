#Python program to implement House Robber

def rob(nums):
    rob1, rob2 = 0,0

    #[rob1,rob2,n,n+1]
    for n in nums:
        temp = max(n+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    
    return rob2