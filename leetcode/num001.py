__author__ = 'shuai'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]

    def twoSum2(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            dic[nums[i]] = i

sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)
