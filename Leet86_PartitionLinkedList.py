"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
Total Accepted: 88423
Total Submissions: 279365
Difficulty: Medium
Contributors: Admin
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            if head.val == x:
                return head
            else:
                return head
        #Locate the node
        fast_pt = slow_pt = head
        anchor_pt = head
        flag = 0
        while fast_pt:
        #handle the cast fast_pt == slow_pt
            if fast_pt == slow_pt:
                if fast_pt.val == x and flag == 0:
                    anchor_pt = fast_pt
                    head = fast_pt.next
                    slow_pt = head
                    flag = 1
                fast_pt = fast_pt.next
                continue
            else:
                if fast_pt.val == x and flag ==0 :
                    anchor_pt = fast_pt
                    slow_pt.next = fast_pt.next # cut it off
                    fast_pt = fast_pt.next
                    flag = 1
                else: # move both forward
                    fast_pt = fast_pt.next
                    slow_pt = slow_pt.next
        #Swap it to the tail of the list
        if flag == 0:
            return head
        tail_pt = slow_pt
        tail_pt.next = anchor_pt
        tail_pt = anchor_pt 
        tail_pt.next = None
        fast_pt = slow_pt = head
        while fast_pt!= anchor_pt:
            if fast_pt == slow_pt:
                if fast_pt.val > x:
                    head = fast_pt.next
                    tail_pt.next = fast_pt
                    tail_pt = fast_pt
                fast_pt = fast_pt.next
                tail_pt.next = None
            else:
                if fast_pt.val > x:
                    slow_pt.next = fast_pt.next
                    tail_pt.next = fast_pt
                    tail_pt = fast_pt
                    fast_pt = fast_pt.next
                    tail_pt.next = None
                else:
                    fast_pt = fast_pt.next
                    slow_pt = slow_pt.next
        return head
if __name__ == '__main__':
    Solve = Solution()
    head = ListNode(1)
    node = head
    node.next = ListNode(2)
    node = node.next
    node.next =ListNode(2)
    node = node.next
    node.next =ListNode(4)
    node = node.next
    node.next =ListNode(5)
    node = node.next
    node.next =ListNode(6)
    head = Solve.partition(head, 2)
    print head