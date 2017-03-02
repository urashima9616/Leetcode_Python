"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,
"""

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return None
        rootsum = self.OptPathSum(root, res)
        return max(res)
    def OptPathSum(self, root, res):
        if not root:
            return None
        leftopt = self.OptPathSum(root.left, res)
        rightopt = self.OptPathSum(root.right, res)
        if not leftopt and not rightopt:
            res.append(root.val)
            return root.val
        elif not leftopt or not rightopt:
            branch = leftopt or rightopt
            assert(branch)
            res.append(max(branch, root.val, branch+root.val))
            return max(root.val, root.val+branch)
        else:
            res.append(max(leftopt, rightopt, root.val, leftopt+rightopt+root.val, rightopt+root.val, leftopt+root.val))
            return max(root.val + max(leftopt, rightopt), root.val)