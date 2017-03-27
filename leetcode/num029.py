__author__ = 'shuai'

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2**31 - 1
        if dividend == 0:
            return 0
        a = abs(dividend)
        b = abs(divisor)
        ret = 0
        while a >= b:
            c = b
            count = 0
            while a >= c:
                a -= c
                ret += 1 << count
                count += 1
                c <<= 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            ret = 0 - ret
        if ret == 2**31:
            ret -= 1
        return ret

sol = Solution()
print sol.divide(1, 1)
