class Solution:
    def insertionSort(self, nums):
        
        n = len(nums)
        def sort(i):

            if i == n:
                return 
            
            insert(i)

            sort(i+1)
        
        def insert(i):

            if i==0:
                return
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
            
            insert(i-1)
        if n < 2:
            return nums
        sort(0)

        return nums