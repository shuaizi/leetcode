__author__ = 'shuai'

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        alphabet_line_1 = "qwertyuiopQWERTYUIOP"
        alphabet_line_2 = "asdfghjklASDFGHJKL"
        alphabet_line_3 = "zxcvbnmZXCVBNM"
        key_dict = {}
        for key in alphabet_line_1:
            key_dict[key] = 1
        for key in alphabet_line_2:
            key_dict[key] = 2
        for key in alphabet_line_3:
            key_dict[key] = 3
        ret = []
        for word in words:
            mark = key_dict[word[0]]
            to_add = True
            for letter in word[1:]:
                if key_dict[letter] != mark:
                    to_add = False
                    break
            if to_add:
                ret.append(word)

        return ret


sol = Solution()
print sol.findWords(["Hello", "Alaska", "Dad", "Peace"])

