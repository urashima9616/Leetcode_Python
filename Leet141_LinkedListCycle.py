# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Two runner solutions

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow, fast = head, head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
            if fast is slow:
                return True
        return False