# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        layer, valid = self.BalanceChk(root, 0)
        return valid
    def BalanceChk(self, root, k):
        if not root:
            return (k, True)
        left_layer, lvalid = self.BalanceChk(root.left, k+1)
        right_layer, rvalid = self.BalanceChk(root.right, k+1)
        if not lvalid or not rvalid:
            return max(left_layer, right_layer), False
        if abs(left_layer-right_layer) > 1:
            return max(left_layer, right_layer), False
        return max(left_layer, right_layer), True