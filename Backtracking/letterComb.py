#Python program to implement Letter Comvibinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curString):
            if len(curString) == len(digits):
                res.append(curString)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curString + c)
        
        if digits:
            backtrack(0,"")
        return res

obj = Solution()
print(obj.letterCombinations("23"))