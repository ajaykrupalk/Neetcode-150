#Python program to check if two strings are anagrams

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i], 0)
        countT[t[i]] = 1+countT.get(t[i], 0)

    for key in countS:
        if countS.get(key) != countT.get(key, 0):
            return False
    return True

print(is_anagram('rat', 'car'))
# print(is_anagram('anagram', 'nagaram'))