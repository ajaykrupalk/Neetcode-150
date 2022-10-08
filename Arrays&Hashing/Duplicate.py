#Python program to implement contains duplicate

def findDuplicate(arr, n):
    hashSet = set()
    for i in arr:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

print(findDuplicate([1,2,3,1], 4))