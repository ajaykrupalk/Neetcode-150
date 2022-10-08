#Python program to allocate minimum number of pages

#https://takeuforward.org/data-structure/allocate-minimum-number-of-pages/

'''
Method to implement is to use binary search to find the minimum number of pages
'''

def isPossible(arr, n, m, curr_min):
    student = sumAllocated = 0
    for i in range(n):
        if (sumAllocated+arr[i] > curr_min):
            student += 1
            sumAllocated = arr[i]
            if sumAllocated > curr_min:
                return False
        else:
            sumAllocated += arr[i]
    
    return True if student < m else False

def findPages(arr, n, m):
    sum = 0

    if n < m:
        return -1

    for i in range(n):
        sum += arr[i]

    start = 0
    end = sum
    result = -1

    while start <= end:
        mid = (start+end)//2
        if isPossible(arr, n, m, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

arr = [12, 34, 67, 90]
n = len(arr)
m = 2
print("Minimum number of pages = ", findPages(arr, n, m))