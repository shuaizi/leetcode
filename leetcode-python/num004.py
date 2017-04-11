__author__ = 'shuai'

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ret = []
        len1 = len(nums1)
        len2 = len(nums2)
        dst = (len1 + len2)/2
        pos1 = 0
        pos2 = 0
        while pos1 < len1 and pos2 < len2:
            if nums1[pos1] >= nums2[pos2]:
                ret.append(nums2[pos2])
                pos2 += 1
            else:
                ret.append(nums1[pos1])
                pos1 += 1
            if pos1 + pos2 == dst + 1:
                if (len1 + len2) % 2 == 0:
                    return float(ret[dst - 1] + ret[dst])/2
                else:
                    return float(ret[dst])

        while pos1 < len1:
            ret.append(nums1[pos1])
            pos1 += 1
            if pos1 + pos2 == dst + 1:
                if (len1 + len2) % 2 == 0:
                    return float(ret[dst - 1] + ret[dst])/2
                else:
                    return float(ret[dst])
        while pos2 < len2:
            ret.append(nums2[pos2])
            pos2 += 1
            if pos1 + pos2 == dst + 1:
                if (len1 + len2) % 2 == 0:
                    return float(ret[dst - 1] + ret[dst])/2
                else:
                    return float(ret[dst])


sol = Solution()
print sol.findMedianSortedArrays([1, 3], [2])
