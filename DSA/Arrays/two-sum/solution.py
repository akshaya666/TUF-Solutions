class Solution:
    def twoSum(self, nums, target):

        tmp = []

        for i in range(0,len(nums)):

            tmp.append([nums[i],i])
        
        tmp.sort()

        left = 0

        right = len(nums) - 1

        while left < right:

            summ = tmp[left][0] + tmp[right][0] 

            if summ == target:

                return [tmp[left][1],tmp[right][1]]

            elif summ < target:

                left+=1
            else:
                right-=1
    
        