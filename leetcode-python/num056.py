__author__ = 'shuai'

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + "-" + str(self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def _compare(a, b):
            if a.start < b.start:
                return True
            elif a.start > b.start:
                return False
            return a.end < b.end
        if not intervals or len(intervals) <= 1:
            return intervals
        sorted(intervals, _compare)
        ret = []
        ret.append(intervals[0])
        for i in range(1, len(intervals)):
            tmp = ret[-1]
            if tmp.end < intervals[i].start:
                ret.append(intervals[i])
            else:
                if tmp.end <= intervals[i].end:
                    tmp.end = intervals[i].end
        return ret

a = Interval(1, 4)
b = Interval(0, 4)
sol = Solution()
sss = sol.merge([a, b])
for i in range(len(sss)):
    print sss[i]
