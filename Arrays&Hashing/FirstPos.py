#Python program to find the first positive missing number
#using constant extra space 

'''
Since constant extra space we use the method of in-place hashing
'''

def findPost(arr, n):
    #if there is a negative number in the array
    #then make that number as 0
    for i in range(n):
        if arr[i] < 0:
            arr[i] = 0
    
    #marking if an element exists in the array
    #using in-place hashing
    for i in range(n):
        val = abs(arr[i])
        if 1 <= val <= n:
            #checking if an element is already marked as negative
            if arr[val - 1] > 0:
                arr[val-1] = -arr[val-1]
            #if an element is already marked as zero
            elif arr[val-1] == 0:
                arr[val-1] = -(n+1)
    
    #finding the first positive missing number
    for i in range(1,n+1):
        if arr[i-1] >= 0:
            return i
    return n+1

print(findPost([1,-1,6,3],3))
            