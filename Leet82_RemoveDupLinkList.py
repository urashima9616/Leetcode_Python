"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_pt = head
        fast_pt = head
        anchor_pt = head
        flag = 0
        while fast_pt is not None:
            if fast_pt == slow_pt: # the initial step
                fast_pt = fast_pt.next
                continue
            if fast_pt.val == slow_pt.val: # dups, remove it 
                slow_pt.next = fast_pt.next
                flag = 1
                del fast_pt
                fast_pt = slow_pt.next
                continue
            if fast_pt.val != slow_pt.val: # different element, advance slow pt
                if flag == 1:
                    if slow_pt == head:
                        head = fast_pt
                        del slow_pt
                        slow_pt = head
                        anchor_pt = head
                    else:
                        anchor_pt.next = fast_pt
                        del slow_pt
                        slow_pt = fast_pt
                else:
                    if slow_pt == anchor_pt:
                        slow_pt = fast_pt
                    else:
                        anchor_pt = slow_pt 
                        slow_pt = fast_pt
                fast_pt = fast_pt.next
                flag = 0
        if flag == 1:
            if anchor_pt == slow_pt:
                return None
            anchor_pt.next = None
        return head