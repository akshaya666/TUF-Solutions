
class Solution:
    def mergeSort(self, nums):

        if len(nums) < 2:
            return nums

        self.merge_sort_helper(nums, 0, len(nums) - 1)

        return nums

    def merge_sort_helper(self, nums, left, right):

        if left >= right:
            return

        mid = left + (right - left) // 2

        self.merge_sort_helper(nums, left, mid)

        self.merge_sort_helper(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):

        left_arr = nums[left:mid + 1]
        right_arr = nums[mid + 1:right + 1]

        l = 0
        r = 0
        i = left

        while l < len(left_arr) and r < len(right_arr):

            if left_arr[l] <= right_arr[r]:
                nums[i] = left_arr[l]
                l += 1
            else:
                nums[i] = right_arr[r]
                r += 1

            i += 1

        while l < len(left_arr):
            nums[i] = left_arr[l]
            l += 1
            i += 1

        while r < len(right_arr):
            nums[i] = right_arr[r]
            r += 1
            i += 1
