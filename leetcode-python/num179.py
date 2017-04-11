__author__ = 'shuai'


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        ret = ""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                str_i = str(nums[i])
                str_j = str(nums[j])
                if str_i + str_j < str_j + str_i:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
            # to check if max equals 0 ,return '0'
            if i == 0 and nums[i] == 0:
                return '0'
            ret += str(nums[i])
        return ret

sol = Solution()
print sol.largestNumber([3, 30, 34, 5, 9])
