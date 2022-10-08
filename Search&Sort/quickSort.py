#Python program to implement Quick Sort
'''
Method to implement Quick Sort is:
1. Pick an element as pivot (preferably the last element)
2. Keep track of the smaller element and greater element
3. Swap the smaller element with the pivot
4. Recursively sort the left and right of the pivot
'''

def partition(arr,low,high):
    #assigning the pivot of the array to the last element
    pivot = arr[high]

    #keeping track of the greater element
    i = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            #if element smaller than pivot is found
            #swap it with greater element pointed by i
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    
    #in the end move the pivot the correct position
    arr[i+1],arr[high] = arr[high],arr[i+1]

    #Return the position of the partition
    return i+1

#funcion to perform quicksort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        #Recursive call to sort the left of pivot
        quickSort(arr,low,pi-1)
        #Recursive call to sort the right of pivot
        quickSort(arr,pi+1,high)

arr = [ 10, 7, 8, 9, 1, 5]
quickSort(arr,0,len(arr)-1)
print(arr)