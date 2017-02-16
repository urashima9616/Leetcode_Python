class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res, layer = [], [root]
        while layer:
            res.append([node.val for node in layer])
            LR = [(each.left, each.right) for each in layer]
            layer = [member for group in LR for member in group if member]
        return res