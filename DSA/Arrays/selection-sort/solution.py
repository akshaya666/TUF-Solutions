class Solution:
    def selectionSort(self, nums):
        
        n = len(nums)

        for i in range(n-1):

            idx = i

            for j in range(i+1,n):

                if nums[j] < nums[idx]:
                    idx = j
            if idx != i:
                nums[idx],nums[i] = nums[i],nums[idx]
        return nums