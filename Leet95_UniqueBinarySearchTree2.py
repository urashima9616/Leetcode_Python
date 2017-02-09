"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        choice_pool = [i for i in xrange(n+1)]
        res = self.DFSearch(choice_pool, 1, n)
        return res

    def DFSearch(self, choice_pool, start, stop):
        if start > stop:
            return []
        elif start  == stop:
            return [TreeNode(choice_pool[start])]
        treelist = []
        for i in xrange(start, stop+1):
            leftlist = self.DFSearch(choice_pool, start, i-1)
            rightlist = self.DFSearch(choice_pool, i+1, stop)
            for left in leftlist or [None]:
                for right in rightlist or [None]:
                    subroot = TreeNode(choice_pool[i])
                    subroot.left = left
                    subroot.right = right
                    treelist.append(subroot)
        return treelist
if __name__ == '__main__':
    Solve = Solution()
    res = Solve.generateTrees(3)
    print 'hello'

