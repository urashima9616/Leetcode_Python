# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        length = 0
        pt = head
        while pt:
            length += 1
            pt = pt.next
        
        root = self.slist2bst(head, length)
        return root
    def slist2bst(self, head, length):
        if not head:
            return None
        if length <= 0:
            return None
        count = (length - 1)/2
        idx = 0
        pt = head
        while idx < count:
            idx += 1
            pt = pt.next
        root = TreeNode(pt.val)
        left = self.slist2bst(head, count)
        right = self.slist2bst(pt.next, length-count-1)
        root.left = left
        root.right = right
        return root