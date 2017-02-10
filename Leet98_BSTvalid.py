class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        valid = [1]
        prev = []
        self.InorderTraversal(root, prev, valid)
        if valid[0] == 1:
            return True
        else:
            return False
    def InorderTraversal(self, root, prev, valid):
        if not root:
            return 
        self.InorderTraversal(root.left, prev, valid)
        if not valid[0]:
            return False
        if not prev : # The first visited node
            prev.append(root.val)
            self.InorderTraversal(root.right, prev, valid)
        else:
            if prev[0] >= root.val:
                valid[0] = 0
                return
            else:
                prev[0] = root.val
                self.InorderTraversal(root.right, prev, valid)
        return
Solve = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
Solve.isValidBST(root)