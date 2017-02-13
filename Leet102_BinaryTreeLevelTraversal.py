# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        fifo = Queue.Queue()
        res = []
        k = 0
        if not root:
            return []
        fifo.put([k, root])
        prev_layer = -1
        while not fifo.empty():
            cur_layer, node = fifo.get()
            if prev_layer != cur_layer:
                res.append([node.val])
                prev_layer = cur_layer
            else:
                res[cur_layer] += [node.val]
            if node.left:
                fifo.put([cur_layer + 1, node.left])
            if node.right:
                fifo.put([cur_layer + 1, node.right])
        return res