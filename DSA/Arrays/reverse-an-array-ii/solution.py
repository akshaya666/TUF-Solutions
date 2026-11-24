class Solution:
    def reverseArray(self, nums):
        #your code goes here

        self.reversehelper(nums,0,len(nums)-1)
        return nums

    
    def reversehelper(self,nums,left,right):

        if left >= right:
            return 
        
        nums[left], nums[right] = nums[right], nums[left]

        self.reversehelper(nums,left+1,right-1)