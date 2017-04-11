__author__ = 'shuai'

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def _compare(a, b):
            if len(a) < len(b):
                return 1
            elif len(a) == len(b):
                return 0
            return -1

        d = sorted(d, _compare)
        str_len = len(s)
        ret = []
        mark = False
        for i in range(len(d)):
            length = len(d[i])
            j = 0
            k = 0
            while j < str_len and k < length:
                if s[j] == d[i][k]:
                    k += 1
                j += 1
            if k >= length:
                if ret and len(ret[-1]) > length:
                    mark = True
                else:
                    ret.append(d[i])
            if mark:
                break
        if not ret:
            return ""
        ret = sorted(ret)
        return ret[0]


sol = Solution()
print sol.findLongestWord("abpcplea", ["a", "b", "c"])

