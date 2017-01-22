import sys,os
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = [] 
        self.DFS_search(nums, path, result)
        return result
    def DFS_search(self, candidates, path, result):
        if len(candidates) == 0:
            result.append(path)
            return
        for  i in xrange(len(candidates)):
            if i > 0 and i < len(candidates)-1:
                new_candidates = candidates[0:i]
                new_candidates.extend(candidates[i+1:])
            elif i == 0 and i < len(candidates)-1:
                new_candidates = candidates[i+1:]
            elif i > 0 and i == len(candidates)-1:
                new_candidates = candidates[0:i]
            elif i == 0 and i == len(candidates)-1:
                new_candidates = []
            self.DFS_search(new_candidates, path+[candidates[i]], result)
my_solution = Solution()
print my_solution.permute([1, 2, 3])
        
      