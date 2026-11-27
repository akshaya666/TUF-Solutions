class Solution:
    def secondLargestElement(self, nums):

        max_1 , max_2 = nums[0],None
        for i in range(1,len(nums)):

            if nums[i] > max_1:

                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] < max_1:
                if max_2 is None or nums[i] > max_2:
                    max_2 = nums[i]
        if max_2 is None:
            return -1
        return max_2
        