__author__ = 'shuai'

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        tmp = 0
        tmpNode = ret
        while l1 or l2:
            if not l1:
                sum = l2.val
                l2 = l2.next
            elif not l2:
                sum = l1.val
                l1 = l1.next
            else:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            tmpN = ListNode((sum + tmp) % 10)
            tmp = (sum + tmp) / 10
            tmpNode.next = tmpN
            tmpNode = tmpNode.next
        if tmp != 0:
            tmpN = ListNode(tmp)
            tmpNode.next = tmpN
        return ret.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
sol.addTwoNumbers(l1, l2)