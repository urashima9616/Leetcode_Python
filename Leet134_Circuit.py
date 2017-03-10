class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        for i in xrange(len(gas)):
            if self.DFSearch(i, i, gas, cost, tank, 1):
                return i
        return -1
            
    def DFSearch(self, target, k, gas, cost, tank, ini):
        if k == target and not ini:
            return True
        if cost[k] > tank + gas[k]:
            return False
        if k+1 >len(cost) -1:
            return self.DFSearch(target, 0, gas, cost, tank+gas[k]-cost[k], 0)
        else:
            return self.DFSearch(target, k+1, gas, cost, tank+gas[k]-cost[k], 0)
Solve = Solution()
print Solve.canCompleteCircuit([1,2], [2,1])