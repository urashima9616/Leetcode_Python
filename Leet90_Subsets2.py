"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Total Accepted: 95727
Total Submissions: 280274
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numlen = len(nums)
        if numlen == 0:
            return [[]]
        path = []
        res = []
        idx = 1
        nums.sort()
        res.append([])
        while idx < numlen:
            self.DFSearch(nums, 0, numlen, path, res, idx)
            idx += 1
        res.append(nums)
        return res
    
    def DFSearch(self, choice_pool, start, stop, path, res, k):
        if k== 0:
            if path not in res:
                res.append(path)
            return
        for i in xrange(start, stop):
            self.DFSearch(choice_pool, i+1, stop, path + [choice_pool[i]], res,  k-1)