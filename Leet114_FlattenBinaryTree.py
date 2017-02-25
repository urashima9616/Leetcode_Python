"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.BuildFlatten(root)
    def BuildFlatten(self, root):
        if not root:
            return
        if not root.right and not root.left:
            return root
        if not root.left:
            return self.BuildFlatten(root.right)
        if not root.right:
            root.right = root.left
            root.left = None
            return self.BuildFlatten(root.right)
        anchor = root.right
        leaveleft = self.BuildFlatten(root.left)
        root.right = root.left
        root.left = None
        #plant the right subtree to the leave of subleft tree
        leaveleft.right = anchor
        #Get the leave node of right subtree
        leaveright = self.BuildFlatten(anchor)
        return leaveright
Solve = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
Solve.flatten(root)