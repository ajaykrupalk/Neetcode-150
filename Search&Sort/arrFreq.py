#Python program to sort elements by frequency

def arrFreq(arr):
    freq = {}
    
    for i in arr:
        freq[i] = 1 + freq.get(i, 0)
    
    arr.sort(key=lambda x: (-freq[x], x))
    return arr

print(arrFreq([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))