#Python program to implement Permutations

class Solution:
    def permutations(self,nums):
        result = []
        
        if(len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutations(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

