#Python program to implement Palindromic Substrings

def countSubstrings(s):
    res = 0

    for i in range(len(s)):
        res += countPalind(s, i, i)
        res += countPalind(s, i, i+1)

def countPalind(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    
    return res