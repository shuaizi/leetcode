__author__ = 'shuai'

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mark = {}
        i = 0
        while i < len(s):
            if len(s) - i < len(mark):
                return len(mark)
            sub = {}
            for ch in s[i:]:
                if ch not in sub:
                    sub[ch] = ch
                else:
                    break
            if len(sub) > len(mark):
                    mark = sub.copy()
            i += 1
        if i >= len(s):
            return len(mark)


sol = Solution()
print sol.lengthOfLongestSubstring("dvdf")