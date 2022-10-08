def isPossible(arr,n,m,cur_min):
	student = sumAllocated = 0
	for i in range(n):
		if sumAllocated+arr[i] > cur_min:
			student += 1
			sumAllocated = arr[i]
			if sumAllocated > cur_min:
				return False
		else:
			sumAllocated += arr[i]
	return True if student < m else False
	

def findPages(arr,n,m):
	if n < m:
		return -1
	
	Totalsum = sum(arr)
	start = 0
	end = Totalsum
	result = -1

	while start <= end:
		mid = (start+end)//2
		if isPossible(arr,n,m,mid):
			result = mid
			end = mid-1
		else:
			start = mid+1
	return result

arr = [12, 34, 67, 90]
n = len(arr)
m = 2
print("Minimum number of pages = ", findPages(arr, n, m))