#Python program to implement longest substring without repeating characters

def longest(s):
    hashset = set()
    l = res = 0
    for r in range(len(s)):
        while s[r] in hashset:
            hashset.remove(s[l])
            l+=1
        hashset.add(s[r])
        res = max(res,r-l+1)
    return res

print(longest('abcabcbb'))