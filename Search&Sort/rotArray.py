#Python program to search an element in a sorted and rotated array

def search(arr,target):
    dict = {}
    if target not in arr:
        return -1

    for i in range(len(arr)):
        dict[arr[i]] = i

    return dict[target]

print(search([5, 6, 7, 8, 9, 10, 1, 2, 3],3))