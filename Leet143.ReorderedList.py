"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Key idea:
Use fast and slow pointer to find the mid of the link list
reverse the right hand side
combine the two linked list
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        #reverse right hand side
        right_head = slow.next
        slow.next = None
        if not right_head:
            return
        new_head = self.reverseList(right_head)
        head = self.combineList(head, new_head)
        
    def reverseList(self, head):
        if head == None:
            return head
        prev, current, post = None, head, head.next
        while current:
            current.next = prev
            prev = current
            current = post
            if post:
                post = post.next
        return prev

    def combineList(self, head1, head2):
        pt_1, pt_2 = head1.next, head2.next
        new_head = head1
        new_head.next = head2
        new_tail = head2
        while pt_1 and pt_2:
            post_1 = pt_1.next
            post_2 = pt_2.next
            new_tail.next = pt_1
            new_tail.next.next = pt_2
            new_tail = pt_2
            pt_1 = post_1
            pt_2 = post_2
        if pt_1 and pt_2 == None:
            new_tail.next = pt_1
        elif pt_1 == None and pt_2:
            new_tail.next = pt_2
        return new_head

head = ListNode(0)
pt = head
for i in xrange(1):
    pt.next = ListNode(i+1)
    pt = pt.next

Solve = Solution()
new_head = Solve.reorderList(head)

