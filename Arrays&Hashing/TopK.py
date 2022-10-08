#Python program to find top k frequent elements

#Method to implement is bucket sort

def findTopK(arr,k):
    count = {}
    freq = [[] for i in range(len(arr)+1)]

    for i in arr:
        count[i] = 1+count.get(i,0)
    
    for key, val in count.items():
        freq[val].append(key)
    
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(findTopK([1,1,1,2,2,100],2))