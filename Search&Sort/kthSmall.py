#Python program to implement the kth smallest element in an array

'''Implementing kth largest which is similar to kth smallest'''

'''Using Quick Select which is a variation of Quick Sort'''

def kthLargest(nums, k):
    #since we are finding the kth largest element
    #we need to find the (len(nums) - k)th smallest element
    k = len(nums) - k

    def quickSelect(l,r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p],nums[i] = nums[i],nums[p]
                p += 1
        nums[p],nums[r] = nums[r],nums[p]

        if p > k:
            return quickSelect(l,p-1)
        elif k > p:
            return quickSelect(p+1,r)
        else:
            return nums[p]
    
    return quickSelect(0,len(nums)-1)

print(kthLargest([3,2,1,5,6,4],2))