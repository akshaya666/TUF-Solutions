class Solution:
    def rearrangeArray(self, nums):

        res = [0]*len(nums)

        p,n = 0,1

        for i in range(0,len(nums)):

            if nums[i] > 0:
                res[p] = nums[i]
                p+=2
            else:
                res[n] = nums[i]
                n+=2
        return res
        