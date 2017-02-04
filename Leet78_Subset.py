"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Total Accepted: 139704
Total Submissions: 376249
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numlen = len(nums)
        if numlen == 0:
            return [[]]
        idx = 0
        path = []
        res = []
        choice_pool = nums
        while idx < numlen+1:
            if idx == 0:
                res.append([])
                idx += 1
            else:
                self.DFSearch(choice_pool, 0, numlen, path, res, idx)
                idx += 1
        return res
            
                
    
    def DFSearch(self, choice_pool, start, stop, path, res, k):
        if k == 0:
            res.append(path)
        for i in xrange(start, stop):
            self.DFSearch(choice_pool, i+1, stop, path+[choice_pool[i]], res, k-1)
if __name__ == '__main__':
    Solve = Solution()
    print Solve.subsets([1,2,3])
