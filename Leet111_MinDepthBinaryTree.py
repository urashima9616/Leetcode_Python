# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 1000000000
        depth = self.DFSearchMin(root, 0, res)
        return depth + 1
    def DFSearchMin(self, root, k, res):
        if not root:
            return res
        if not root.left and not root.right:
            if k < res:
                res = k
                return k
        if k >= res:
            return res
        left = self.DFSearchMin(root.left, k+1, res)
        right = self.DFSearchMin(root.right, k+1, left)
        return min(left, right)