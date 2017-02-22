# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = self.Treebuild(inorder, postorder)
        return root
    
    def Treebuild(self, inorder, postorder):
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        inPos = inorder.index(postorder[-1])
        left = self.Treebuild(inorder[:inPos], postorder[:inPos])
        right = self.Treebuild(inorder[inPos+1:], postorder[inPos:-1])
        root.left = left
        root.right = right
        return root