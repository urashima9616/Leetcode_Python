class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        prev = None
        cur1 = l1
        cur2 = l2
        head = None
        while cur1 and cur2:
            if cur2.val < cur1.val:
                if not prev:
                    prev = cur2
                    head = prev
                else:
                    prev.next = cur2
                cur2 = cur2.next
            else:
                if not prev:
                    prev = cur1
                    head = prev
                else:
                    prev.next = cur1
                cur1 = cur1.next
        if not cur1:
            prev.next = cur2
        if not cur2:
            prev.next = cur1
        return head
Solve = Solution()
l1 = ListNode(3)
l1.next = ListNode(5)
l1.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(8)

Solve.mergeTwoLists(l1, l2)
