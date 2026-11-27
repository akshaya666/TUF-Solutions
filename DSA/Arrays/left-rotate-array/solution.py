class Solution:
    def rotateArray(self, nums, k: int) -> None:
        
        n = len(nums)

        k = k%n
        def reverse_helper(nums,left,right):

            while left < right:

                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        
        reverse_helper(nums,0,k-1)
        reverse_helper(nums,k,n-1)
        reverse_helper(nums,0,n-1)

        return nums
        
    
