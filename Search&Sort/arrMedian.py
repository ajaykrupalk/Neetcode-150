#Python program to find median of two sorted arrays of same size

'''
Method to implement is to swap all smaller numbers to arr1
Sort both the arrays
Get the median of the two arrays by taking 
last element of first array and first element of second array
and divide both by 2
'''

def getMedian(ar1,ar2,n):
    i,j = n-1, 0

    #swap all small elements to ar1
    while ar1[i] > ar2[j] and i > -1 and j < n:
        ar1[i],ar2[j] = ar2[j],ar1[i]
        i -= 1
        j += 1
    
    ar1.sort()
    ar2.sort()

    return (ar1[-1]+ar2[0])//2

ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
  
n1, n2 = len(ar1), len(ar2)
  
if(n1 == n2):
    print('Median is', getMedian(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")