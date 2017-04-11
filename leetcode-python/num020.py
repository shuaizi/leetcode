__author__ = 'shuai'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) % 2:
            return False

        def _comapare(left, right):
            if left == "(" and right == ")":
                return True
            elif left == "[" and right == "]":
                return True
            elif left == "{" and right == "}":
                return True
            else:
                return False

        stack = []
        list_s = list(s)
        stack.append(list_s[0])
        pos = 1
        length = len(list_s) - 1

        while stack:
            if pos > length:
                break
            mark = stack[-1]
            if _comapare(mark, list_s[pos]):
                stack.pop()
            else:
                stack.append(list_s[pos])
            pos += 1

        if not stack:
            return True
        return False

sol = Solution()
print sol.isValid("(((}]))")
