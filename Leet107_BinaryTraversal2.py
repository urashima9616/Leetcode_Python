# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layer, res = [root], []
        while root and layer:
            res.append([each.val for each in layer])
            groups = [(each.left, each.right) for each in layer]
            layer = [each for group in groups for each in group if each]
        res.reverse()
        return res