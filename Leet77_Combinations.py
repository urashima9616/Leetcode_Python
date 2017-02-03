"""
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
Total Accepted: 103565
Total Submissions: 272497
Difficulty: Medium
Contributors: Admin

"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        result = []
        path = [0 for i in xrange(k)]
        select_table = [0 for i in xrange(n+1)]
        self.DFS_Search(1, n, select_table, k, path, result, 0)
        return result
        
    def DFS_Search (self, low, n, select_table, k, path, result, layer):
        if k == 0:
            result.append(list(path))
            return
        if low == n:
            return 
        for i in xrange(low,n+1):
            if select_table[i] > 0:
                continue
            else:
                new_table = list(select_table) 
                new_table[i] = 1
                path[layer] = i
                self.DFS_Search(i+1, n, new_table, k-1, path, result, layer+1)
Solve = Solution()
print Solve.combine(4,2)