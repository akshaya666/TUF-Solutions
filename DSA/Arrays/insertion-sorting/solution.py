class Solution:
    def insertionSort(self, nums):

        n = len(nums)

        for i in range(1,n):
            
            key = nums[i]
            pos = i-1

            while pos >=0 and nums[pos] > key:

                nums[pos+1] = nums[pos]
                pos-=1
            nums[pos+1] = key
        
        return nums
