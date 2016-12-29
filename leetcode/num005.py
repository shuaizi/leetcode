__author__ = 'shuai'

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        ret = []
        for i in range(len(s)):
            if length >= len(s) - i:
                return ret
            for j in range(len(s)-1, i, -1):
                m = i
                n = j
                while s[m] == s[n] and m < n:
                    m += 1
                    n -= 1
                if m >= n and j - i + 1 > length:
                    ret = s[i:j+1]
                    length = j - i + 1
        if not ret:
            return s[0]
        return ret

sol = Solution()
print sol.longestPalindrome("babab")


