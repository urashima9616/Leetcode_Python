class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        path = []
        res = []
        # Get all the number
        self.DFSearch2(root, path, 0, res)
        return sum(res)

    def DFSearch2(self, root, path, k, res):
        if len(path) > k + 1:
            path[k] = root.val
        else:
            path.append(root.val)
        if not root.left and not root.right:
            num = 0
            w = 1
            for i in xrange(k+1):
                num += w*path[k-i]
                w *= 10
            res.append(num)
            return
        if root.left:
            self.DFSearch2(root.left, path[:k+1], k+1, res)
        if root.right:
            self.DFSearch2(root.right, path[:k+1], k+1, res)
        return