#Python program to implement binary search

'''
Method to implement binary search
Find the mid element of the array and compare with x
If x is less than mid, then search in the left half of the array
Else search in the right half of the array
'''

def bsearch(arr,l,r,x):
    if l<=r:

        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return bsearch(arr,l,mid-1,x)
        
        else:
            return bsearch(arr,mid+1,r,x)
    
    else:
        return -1

print(bsearch([2, 3, 4, 10, 40],0,5,10))