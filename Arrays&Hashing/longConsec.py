#Python program to find longest consecutive sequence

def consecSeq(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numSet:
            length = 1
            while (n+length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

print(consecSeq([100,4,200,1,3,2]))