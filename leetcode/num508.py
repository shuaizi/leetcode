__author__ = 'shuai'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_dict = {}
        def tree_sum(node):
            if not node:
                return
            if node.left and node.right:
                ret = node.val + tree_sum(node.left) + tree_sum(node.right)
                val = ret_dict.get(ret, 0)
                ret_dict[ret] = val + 1
                return ret
            elif node.left:
                ret = node.val + tree_sum(node.left)
                val = ret_dict.get(ret, 0)
                ret_dict[ret] = val + 1
                return ret
            elif node.right:
                ret = node.val + tree_sum(node.right)
                val = ret_dict.get(ret, 0)
                ret_dict[ret] = val + 1
                return ret
            else:
                ret = node.val
                val = ret_dict.get(ret, 0)
                ret_dict[ret] = val + 1
                return ret
        if not root:
            return []
        tree_sum(root)
        tmp_dict = {}
        for (k, v) in ret_dict.items():
            tmp_val = tmp_dict.get(v, [])
            tmp_val.append(k)
            tmp_dict[v] = tmp_val
        tmp_keys = tmp_dict.keys()
        tmp_keys.sort()
        print tmp_dict[tmp_keys[-1]]


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
sol = Solution()
sol.findFrequentTreeSum(root)
