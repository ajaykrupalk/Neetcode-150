#Python program to implement Palindrome Partitioning

class Palind:
    def partition(self,s):
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                print(f"i,j: {i,j}")
                if self.isPalind(s,i,j):
                    part.append(s[i:j+1])
                    print(f"append: {part}")
                    dfs(j+1)
                    part.pop()
                    print(f"pop: {part}")
        
        dfs(0)
        return res
    
    def isPalind(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1, r-1
        return True

obj = Palind()
print(obj.partition('aab'))