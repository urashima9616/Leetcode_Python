import sys,os
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #goal test
        #deque what you have 
        #expand
        #track back to the root
        #makeup cost
        #current solution 0:cost now 1:makeup now
        current_node = []
        current_node.append(target)
        res = []
        candidates.sort()
        self.DFS_search(current_node, candidates, target, res)
    def DFS_search(self, current_node, candidates, target, res):
        #Goal test part
        if current_node[0] < 0:
            return 
        elif current_node[0] == 0:
            res.append(list(current_node[1:]))
            return 
        #Add the current_sol as explored


        #Generate the new children nodes
        for each in candidates:
            next_node = current_node[:]
            next_node[0] = next_node[0]+each
            next_node.append(each)
            self.DFS_search(next_node, candidates, target, res)
my_solution = Solution()
my_solution.combinationSum([2, 3, 6, 7], 7)
        
      