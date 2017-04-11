__author__ = 'shuai'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = [0]
        def _process(root, sum):
           if not root:
               return
           _process(root.right, sum)
           print("before sum: %d", sum[0])
           root.val += sum[0]
           sum[0] = root.val
           print("after sum: %d", sum[0])
           _process(root.left, sum)

        _process(root, sum)
        return root

    def convertBST_2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = 0
        ret = []
        tmp_root = root
        while ret or tmp_root:
            while tmp_root:
                ret.append(tmp_root)
                tmp_root = tmp_root.right
            if ret:
                tmp_root = ret.pop()
                tmp_root.val += sum
                sum = tmp_root.val
                tmp_root = tmp_root.left
        return root


a = TreeNode(2)
b = TreeNode(5)
c = TreeNode(13)
b.left = a
b.right = c
sol = Solution()
#ret = sol.convertBST(b)
ret = sol.convertBST_2(b)
print ret
