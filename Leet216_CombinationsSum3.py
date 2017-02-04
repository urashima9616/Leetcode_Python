"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
Total Accepted: 56969
Total Submissions: 134342
Difficulty: Medium
Contributors: Admin
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0 or k ==0:
            return []
        choice_pool = [i for i in xrange(0,11)]
        path = []
        res = []
        self.DFSearch(choice_pool, 1, 10, path, res, k, n)
        return res
        
            
    def DFSearch(self, choice_pool, start, stop, path, res, k, target):
        if k == 0 and target == 0:
            res.append(path)
            return
        if target < 0 or k == 0:
            return
        for i in xrange(start, stop):
            self.DFSearch(choice_pool, i+1, stop, path+[choice_pool[i]], res, k-1, target-choice_pool[i])


Solve = Solution()
print Solve.combinationSum3(3, 9)