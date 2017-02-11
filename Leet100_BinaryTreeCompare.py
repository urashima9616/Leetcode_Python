"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
Total Accepted: 181258
Total Submissions: 399232
Difficulty: Easy
Contributors: Admin
"""
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.IsTwoTreeSame(p, q)
    def IsTwoTreeSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if not root1.left and not root1.right and not root2.left and not root2.right and root1.val == root2.val:
            return True
        if root1.val != root2.val:
            return False
        left = self.IsTwoTreeSame(root1.left, root2.left)
        right = self.IsTwoTreeSame(root1.right, root2.right)
        return left and right