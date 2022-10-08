#Python program to implement kth largest element in an array

def findKthLargest(self, nums, k):
    k = len(nums) - k

    def quickSelect(l,r):
        pivot,p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:#if k is less than p
            return quickSelect(l,p-1)
        elif p < k:#if k is greater than p
            return quickSelect(p+1,r)
        else:
            return nums[p]