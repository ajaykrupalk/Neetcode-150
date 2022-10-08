#Python program to implement Binary Search

def bSearch(arr,l,r,x):
    if l<=r:

        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return bSearch(arr,l,mid-1,x)
        
        else:
            return bSearch(arr,mid+1,r,x)
    
    else:
        return -1

print(bSearch([-1,0,3,5,9,12],0,6,9))