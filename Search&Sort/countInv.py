#Python program to count inversions in an array

def countInv(arr, left, right):
    inv_count = 0

    if left < right:

        mid = (left+right)//2

        inv_count += countInv(arr, left, mid)
        inv_count += countInv(arr, mid+1, right)

        inv_count += mergeSort(arr,left,mid,right)
    
    return inv_count     

def mergeSort(arr,left,mid,right):
    i = left
    j = mid+1

    inv_count = 0

    while i <= mid and j <= right :

        if arr[i] <= arr[j]:
            i += 1

        else:
            inv_count += (mid-i+1)
            j += 1

    return inv_count

arr = [1, 20, 6, 4, 5]
result = countInv(arr,0,len(arr)-1)
print(result)