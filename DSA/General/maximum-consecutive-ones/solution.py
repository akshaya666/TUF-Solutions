class Solution:
    def findMaxConsecutiveOnes(self, nums):

        count = 0

        ans = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                count+=1
            else:
                 if count > ans:
                    ans = count
                 count = 0
        if count > ans:
            ans = count
        return ans
            


            
        