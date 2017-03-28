__author__ = 'shuai'

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_val = nums[0]
        max_val = nums[0]
        for i in range(len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
            if nums[i] > max_val:
                max_val = nums[i]

        if min_val == max_val:
            return 0
        if len(nums) == 2:
            return max_val - min_val

        bucket_min = []
        bucket_max = []
        for i in range(len(nums)):
            bucket_max.append(min_val)
            bucket_min.append(max_val)
        gap = (max_val - min_val)/(len(nums) - 1)
        if (max_val - min_val) % (len(nums) - 1):
            gap += 1
        for i in range(len(nums)):
            pos = (nums[i] - min_val)/gap
            if nums[i] > bucket_max[pos]:
                bucket_max[pos] = nums[i]
            if nums[i] < bucket_min[pos]:
                bucket_min[pos] = nums[i]

        ret = 0
        pre = bucket_max[0]
        for i in range(1, len(nums)):
            if bucket_max[i] == min_val and bucket_min[i] == max_val:
                continue
            ret = max(ret, bucket_min[i] - pre)
            pre = bucket_max[i]

        return ret

sol = Solution()
print sol.maximumGap([3, 6, 9, 1])
