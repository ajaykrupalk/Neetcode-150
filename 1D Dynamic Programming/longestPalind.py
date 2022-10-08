#Python program to implement Longest Palindromic String

def longestPalindrome(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        #odd length palindromes
        l,r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l-=1
            r+=1
        
        #even length palindrome
        l,r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l-=1
            r+=1
    
    return res
