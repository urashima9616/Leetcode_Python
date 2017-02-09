"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Total Accepted: 109402
Total Submissions: 273854
Difficulty: Medium
Contributors: Admin

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = self.DFCount(1, n)
        return res
    def DFCount(self, start, stop):
        if start > stop:
            return 1
        if start == stop:
            return 1
        sum = 0
        for i in xrange(start, stop+1):
            left = self.DFCount(start, i-1)
            right = self.DFCount(i+1, stop)
            sum += left*right
        return sum