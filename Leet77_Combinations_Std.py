"""
This gives a standardized version of backtracking for all
possible combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        choice_pool = [i for i in xrange(0,n+1)]
        path = []
        res = []
        self.DFSearch(choice_pool, 1, n+1, path, res, k)
        return res

    def DFSearch(self, choice_pool, start, stop, path, res, k):
        if k == 0:
            res.append(path)
        for i in xrange(start, stop):
            self.DFSearch(choice_pool, i+1, stop, path + [choice_pool[i]], res, k-1)
if __name__ == '__main__':
    Solve = Solution()
    print Solve.combine(4, 2)