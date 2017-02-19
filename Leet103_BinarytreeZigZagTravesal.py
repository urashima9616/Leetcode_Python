"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Total Accepted: 88494
Total Submissions: 270550
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        flag = 0
        layer = [root]
        res = []
        while root and layer :
            if flag == 0:
                #Append the current layer
                res.append([each.val for each in layer])
                cur_layer = [(each.left, each.right) for each in layer]
                layer = [group_member for group in cur_layer for group_member in group if group_member]
                flag = 1
            else:
                temp = [each.val for each in layer]
                temp.reverse()
                res.append(temp)
                cur_layer = [(each.left, each.right) for each in layer]
                layer = [group_member for group in cur_layer for group_member in group if group_member]
                flag = 0
        return res