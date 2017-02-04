import sys,os
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            if path not in res:
                res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
my_solution = Solution()
print my_solution.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
        
      