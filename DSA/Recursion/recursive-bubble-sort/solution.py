class Solution:
    def bubbleSort(self, nums):
    
        n = len(nums)

        def sort(n):
            
            if n < 2:

                return nums
            
            def compare(i):

                if i == n-1:
                    return 
                
                if nums[i] > nums[i+1]:

                    nums[i],nums[i+1] = nums[i+1],nums[i]
                
                compare(i+1)
            
            compare(0)
            sort(n-1)
        
        if n > 1:
            sort(n)
        return nums

        