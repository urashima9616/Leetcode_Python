"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
Total Accepted: 90447
Total Submissions: 291389
Difficulty: Medium
Contributors: Admin
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        self.Treebuild(preorder, inorder)
    def Treebuild(self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        inPos = inorder.index(preorder[0])
        left = self.Treebuild(preorder[1:1+inPos], inorder[:inPos])
        right = self.Treebuild(preorder[1+inPos:], inorder[inPos+1:])
        root.left = left
        root.right =right
        return root
Solve = Solution()
Solve.buildTree([1,2,3,4,5,6,7,8,9,10,11], [5,4,6,3,8,7,9,2,10,1,11] )

"""
[1,2,3,4,5,6,7,8,9,10,11]
[5,4,6,3,8,7,9,2,10,1,11]
"""