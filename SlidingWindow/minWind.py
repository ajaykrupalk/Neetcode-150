#Python program to implement minimum window substring

def minWind(s,t):
    if t == "": return -1

    countT, window = {}, {}
    for c in t:
        countT[c] = 1+countT.get(c,0)
    
    l = 0
    res, resLen = [-1,-1], float("infinity")
    have, need = 0, len(countT)

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c,0)

        if c in countT and window[c] == countT[c]:
            have += 1
        
        while have == need:
            if (r-l+1) < resLen:
                res = [l,r]
                resLen = (r-l+1)
            
            window[s[l]] -= 1

            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
            
    l,r = res
    return s[l:r+1] if resLen != float("infinity") else ""

print(minWind('ADOBECODEBANC','ABC'))