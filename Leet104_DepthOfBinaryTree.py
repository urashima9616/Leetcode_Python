# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [1]
        max_depth = self.DFSearch(root, 1, res)
        return max(res)
    def DFSearch(self, root, k, res):
        if not root:
            return None
        left = self.DFSearch(root.left, k+1, res)
        right = self.DFSearch(root.right, k+1, res)
        if not left and not right:
            res.append(k)
        return