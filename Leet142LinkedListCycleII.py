"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Key idea:

send another slow pointer when the other slow, fast pair meets

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast, slow = head, head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
            if fast is slow:
                break
        else:
            return None
        while not (head is slow):
            head = head.next
            slow = slow.next
        return head