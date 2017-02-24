# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.DFSearch(root, sum)
        
    def DFSearch(self, root, target):
        if not root:
            return False
        if target == root.val and root.left == None and root.right == None:
            return True

        return self.DFSearch(root.left, target-root.val) or self.DFSearch(root.right, target-root.val)