__author__ = 'shuai'

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                tmp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = tmp
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                tmp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = tmp
                high -= 1
        return nums

sol = Solution()
print sol.sortColors([1, 0])
