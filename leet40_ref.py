import sys,os
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        if len(candidates)==0:
            return
        working_stack={}
        for i in xrange(index, len(candidates)):
            if working_stack.has_key(candidates[i]):
                continue
            working_stack[candidates[i]]=1
            self.dfs(candidates[i+1:], target-candidates[i], 0, path+[candidates[i]], res)
my_solution = Solution()
print my_solution.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
        
      