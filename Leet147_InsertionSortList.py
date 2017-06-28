# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        next_pt = head.next
        tail = head
        current_pt = head
        prev_pt = None
        while next_pt:
            current_pt = head
            prev_pt = None
            while current_pt is not next_pt:
                if current_pt.val >= next_pt.val:
                    if prev_pt:
                        tail.next = next_pt.next
                        prev_pt.next = next_pt
                        next_pt.next = current_pt
                        next_pt = tail.next
                        break
                    else: # head
                        tail.next = next_pt.next
                        next_pt.next = current_pt
                        head = next_pt
                        next_pt = tail.next
                        break
                else:
                    prev_pt = current_pt
                    current_pt = current_pt.next
            else:
                tail = next_pt
                next_pt = next_pt.next
        return head