class Solution:
    def missingNumber(self, nums):
        
        n = len(nums)

        summ = n * (n+1) // 2

        return summ - sum(nums)
