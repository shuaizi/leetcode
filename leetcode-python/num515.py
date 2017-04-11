__author__ = 'shuai'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import sys
        ret_1 = []
        ret_2 = []
        ret = []
        if not root:
            return ret
        ret_1.append(root)
        while ret_1 or ret_2:
            if ret_1:
                tmp_ret = -sys.maxint - 1
                while ret_1:
                    tmp_node = ret_1.pop()
                    tmp_ret = max(tmp_ret, tmp_node.val)
                    if tmp_node.left:
                        ret_2.append(tmp_node.left)
                    if tmp_node.right:
                        ret_2.append(tmp_node.right)
                ret.append(tmp_ret)
            elif ret_2:
                tmp_ret = -sys.maxint - 1
                while ret_2:
                    tmp_node = ret_2.pop()
                    tmp_ret = max(tmp_ret, tmp_node.val)
                    if tmp_node.left:
                        ret_1.append(tmp_node.left)
                    if tmp_node.right:
                        ret_1.append(tmp_node.right)
                ret.append(tmp_ret)
        return ret

a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(3)
f = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
sol = Solution()
print sol.largestValues(a)

