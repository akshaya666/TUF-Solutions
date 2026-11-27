class Solution:
    def moveZeroes(self, nums):

        idx = -1 

        for i in range(len(nums)):

            if nums[i]==0:
                idx = i
                break
        if idx ==-1:
            return nums
        for i in range(idx+1,len(nums)):
            if nums[i] != 0:

                nums[i],nums[idx]=nums[idx],nums[i]

                idx+=1
    
        return nums

