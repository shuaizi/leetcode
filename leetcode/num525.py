__author__ = 'shuai'


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            nums[i] = -1 if nums[i] == 0 else 1
        length = len(nums)
        ret = 0
        sum = 0
        for i in xrange(length):
            sum += nums[i]
        for i in xrange(length):
            if i > 0:
                sum = sum - nums[i - 1]
            tmp_sum = sum
            for j in xrange(length - 1, i,  -1):
                if j < length - 1:
                    tmp_sum = tmp_sum - nums[j]
                if tmp_sum == 0 and ret < j - i:
                    ret = j - i + 1
                    break
            if ret >= length - i:
                return ret
        return ret

sol = Solution()
print sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1])
