"""
Reverse a singly linked list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        prev = None
        cur = head
        while cur:
            if not prev:
                prev = cur
                cur = cur.next
            else:
                nextpt = cur.next
                cur.next = prev
                prev = cur
                cur = nextpt
        return prev

Solve = Solution()
head = ListNode(1)
node = ListNode(2)
head.next = node
head = Solve.reverseList(head)
