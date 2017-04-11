__author__ = 'shuai'

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        minus = 0
        for i in range(len(str)):
            if str[i].isdigit():
                break
            else:
                length -= 1
                if str[i] == '-':
                    minus += 1
        if length == 0:
            return 0
        if length == 1:
            if minus % 2 == 0:
                return int(str[len(str) - 1])
            else:
                return 0 - int(str[len(str) - 1])
        ret = 0
        for i in range(length):
            if not str[len(str)-i-1].isdigit():
                continue
            ret += (int(str[len(str)-i-1]) * (10**i))
        if len(str) != length and minus % 2 == 1:
            ret = 0 - ret
        return ret


sol = Solution()
print sol.myAtoi("+-1")
