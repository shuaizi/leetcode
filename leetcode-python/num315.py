__author__ = 'shuai'

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = []
        ret = [0] * len(nums)
        for i in range(len(nums)):
            count.append({'index': i,
                          'value': nums[i]})
        self.merge_sort(count, 0, len(count) - 1, ret)
        return ret

    def merge(self, nums, start, mid, end, ret):
        tmp = [{}] * (end - start + 1)
        i = start
        j = mid + 1
        k = 0
        jump = 0
        while i <= mid or j <= end:
            if i > mid:
                tmp[k] = nums[j]
                j += 1
                jump += 1
            elif j > end:
                tmp[k] = nums[i]
                ret[tmp[k].get('index')] += jump
                i += 1
            elif nums[i].get('value') <= nums[j].get('value'):
                tmp[k] = nums[i]
                ret[tmp[k].get('index')] += jump
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
                jump += 1
            k += 1

        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1

        while j <= end:
            tmp[k] = nums[j]
            j += 1
            k += 1

        k = 0
        for m in range(start, end + 1):
            nums[m] = tmp[k]
            k += 1

    def merge_sort(self, nums, start, end, ret):
        if start >= end:
            return
        mid = (end + start) / 2
        self.merge_sort(nums, start, mid, ret)
        self.merge_sort(nums, mid+1, end, ret)
        self.merge(nums, start, mid, end, ret)
        print nums


sol = Solution()
print sol.countSmaller([1, 1])
